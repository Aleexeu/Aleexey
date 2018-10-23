import discord
import asyncio
import random
import datetime
import os

client = discord.Client()


@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')

@client.event
async def on_ready():
    while True:
        await client.change_presence(game=discord.Game(name="MINECRAFT"))
        await asyncio.sleep(5)
        # Ele vai esperar 60 segundos para mudar para o proximo status
        await client.change_presence(game=discord.Game(name="BRAAINS.IO"))
        await asyncio.sleep(5)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo

@client.event
async def on_message(message):
    if message.content.lower().startswith('/test'):
        await client.send_message(message.channel, "Olá Mundo, estou vivo!")
    if message.content.lower().startswith('/say'):
        if message.author.server_permissions.administrator:
            try:
                msg = str(message.content).replace("/say ", "")
                if len(msg) >= 1:
                    await client.delete_message(message)
                else:
                    await client.send_message(message.channel, "Digite algo!")
            # se o bot nao puder apagar a msg do seu comando
            except discord.Forbidden:
                msg = str(message.content).replace("/say ", "")
                await client.send_message(message.channel, msg)
        else:
            await client.send_message(message.channel, "Sem permissão!")
    if message.content.lower().startswith('/juntarnomes'):
        try:
            cont = message.mentions[0].name
            cont2 = message.mentions[1].name
            cont3 = len(cont2)
            cont4 = cont3 - 4
            cont5 = cont[0:4]
            cont6 = cont2[cont4:cont3]
            cont7 = cont5 + cont6
            await client.send_message(message.channel,
                                      "Junção do nome de {} com {} = **{}**".format(message.mentions[0].mention,
                                                                                    message.mentions[1].mention, cont7))
        except IndexError:
            await client.send_message(message.channel,
                                      "{} Você não mencionou dois usuarios".format(message.author.mention))
    if message.content.startswith("/ban"):
        if not message.author.server_permissions.ban_members:
            return await client.send_message(message.channel,
                                             "Você não tem permissão para executar esse comando bobinho(a)!")
        try:
            user = message.mentions[0]
            banido = await client.send_message(message.channel,
                                               "O usuario(a) <@{}> foi banido com sucesso do servidor.".format(user.id))
            await client.ban(user, delete_message_days=1)
        except IndexError:
            await client.send_message(message.channel, "Você deve especificar um usuario para banir!")
        except discord.Forbidden:
            await client.send_message(message.channel,
                                      "Não posso banir o usuário, o cargo dele está acima de mim ou não tenho permissão para banir membros!")
        canal = client.get_channel('503616605088120853')
        embed = discord.Embed(colour=0xFFA500, description="+ 1 banido")
        embed.add_field(name='`👤 | Úsuario banido:`', value=banido.content)
        await client.send_message(canal, embed=embed)
       


players = {}
COR = 0xF7FE2E

@client.event
async def on_ready():
    print(client.user.name)
    print("===================")

@client.event
async def on_message(message):
    if message.content.startswith('!entrar'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "O bot ja esta em um canal de voz")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('!sair'):
        try:
            mscleave = discord.Embed(
                title="\n",
                color=COR,
                description="Sai do canal de voz e a musica parou!"
            )
            voice_client = client.voice_client_in(message.server)
            await client.send_message(message.channel, embed=mscleave)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "O bot não esta em nenhum canal de voz.")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))

    if message.content.startswith('!play'):
        try:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb.add_field(name="Enviado em:", value="`{}`".format(player.uploaded_date))
                    mscemb.add_field(name="Enviado por:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Duraçao:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.send_message(message.channel, embed=mscemb)
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))

            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb2 = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb2.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb2.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb2.add_field(name="Enviado em:", value="`{}`".format(player.upload_date))
                    mscemb2.add_field(name="Enviado por:", value="`{}`".format(player.uploader))
                    mscemb2.add_field(name="Duraçao:", value="`{}`".format(player.duration))
                    mscemb2.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb2.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.send_message(message.channel, embed=mscemb2)
                except Exception as error:
                    await client.send_message(message.channel, "Error: [{error}]".format(error=error))
        except Exception as e:
            await client.send_message(message.channel, "Error: [{error}]".format(error=e))




    if message.content.startswith('!pause'):
        try:
            mscpause = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscpause)
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))
    if message.content.startswith('!resume'):
        try:
            mscresume = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscresume)
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))


client.run(os.getenv('TOKEN'))
