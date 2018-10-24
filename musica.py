import asyncio
import discord
from discord.ext import commands
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')
# PR#0001

def __init__(self, bot):
        self.bot = bot

class VoiceEntry:
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = ' {0.title} enviado por {0.uploader} e solicitado por {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [Duração: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    @property
    def player(self):
        return self.current.player

    def skip(self):
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Tocando Agora' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()
class Music:
    """Comandos relacionados à voz.
     Funciona em vários servidores de uma só vez. -- PR
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def entrar(self, ctx):
        """Evoca o bot para se juntar ao seu canal de voz."""
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            await self.bot.say('Tem certeza de que você está em um canal?')
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        """comando pra tocar uma música
         Este comando também procura automaticamente no YouTube.
         A lista de sites suportados pode ser encontrada aqui:
         https://rg3.github.io/youtube-dl/supportedsites.html
        """
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            await self.bot.say("Carregando a música, por favor, seja paciente ..")
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'Ocorreu um erro ao processar este pedido: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            await self.bot.say('Enfileirado ' + str(entry))
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def volume(self, ctx, value : int):
        """Define o volume da música atualmente sendo reproduzida. --PR"""

        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            await self.bot.say('Definir o volume para {:.0%}'.format(player.volume))
    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        """Retoma a música atualmente reproduzida."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(pass_context=True, no_pm=True)
    async def parar(self, ctx):
        """Pára a reprodução de áudio e deixa o canal de voz.
         Isso também limpa a fila.
        """
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            await self.bot.say("Limpou a fila e desconectou do canal de voz ")
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    async def pular(self, ctx):
        """Pular música
        """

        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            await self.bot.say('Não está tocando nenhuma música agora...')
            return
        state.skip()
        

    @commands.command(pass_context=True, no_pm=True)
    async def np(self, ctx):
        """Mostra informações sobre a música que esta sendo reproduzida. """

        state = self.get_voice_state(ctx.message.server)
        if state.current is None:
            await self.bot.say('Não tocando nada.')
        else:
            await self.bot.say('Tocando agora {} '.format(state.current))
            
def setup(bot):
    bot.add_cog(Music(bot))
    print('Modulo de musica carregado! ')
