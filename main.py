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
        await client.change_presence(game=discord.Game(name="e cagando!"))
        await asyncio.sleep(5)
        # Ele vai esperar 60 segundos para mudar para o proximo status
        await client.change_presence(game=discord.Game(name="e matando meu pai/Nitroo!"))
        await asyncio.sleep(5)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="fui desenvolvido pelo Nitroo#4025!"))
        await asyncio.sleep(5)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="e olhando meu criador me dando comandos!"))
        await asyncio.sleep(5)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="ajuda ? eu posso te ajudar /help <-"))
        await asyncio.sleep(5)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo

@client.event
async def on_message(message):
    if message.content.lower().startswith('/help'):
        await client.send_message(message.channel, "{},\nMeus comandos abaixo,\n \n \nAdmins:\n/ban (para banir o player),\n/say (para escrever algo.)\n \n \nMembros:\n/botinfo (para ver minhas configurações.)\n/help (para você ver meus comandos)\n/juntarnomes (para juntar um nick com o outro)!".format(message.author.mention))
    if message.content.lower().startswith('/botinfo'):
        embedbot = discord.Embed(
            title='**🤖 Informações do Bot**',
            color=0x00a3cc,
            description='\n'
        )
        embedbot.set_thumbnail(url="https://www.google.com.br/imgres?imgurl=https%3A%2F%2Fabrilsuperinteressante.files.wordpress.com%2F2016%2F03%2Fcachorro.png&imgrefurl=https%3A%2F%2Fsuper.abril.com.br%2Fideias%2Fpare-de-tratar-seu-cachorro-como-se-ele-fosse-um-lobo%2F&docid=6cnBCiMF7Dnm_M&tbnid=TQzry5QTmwCo1M%3A&vet=10ahUKEwjk0d786Z3eAhVMHpAKHfLIAHQQMwiGAigBMAE..i&w=1024&h=682&hl=pt-BR&gl=br&bih=657&biw=1024&q=cachorro&ved=0ahUKEwjk0d786Z3eAhVMHpAKHfLIAHQQMwiGAigBMAE&iact=mrc&uact=8")  # Aqui você coloca a url da foto do seu bot!
        embedbot.add_field(name='`💮 | Nome`', value=client.user.name, inline=True)
        embedbot.add_field(name='`◼ | Id bot`', value=client.user.id, inline=True)
        embedbot.add_field(name='💠 | Criado em', value=client.user.created_at.strftime("%d %b %Y %H:%M"))
        embedbot.add_field(name='📛 | Tag', value=client.user)
        embedbot.add_field(name='‍💻 | Servidores', value=len(client.servers))
        embedbot.add_field(name='👥 | Usuarios', value=len(list(client.get_all_members())))
        embedbot.add_field(name='‍⚙️ | Programador', value="`Nitroo#4025`")  # Aqui você coloca seu nome/discord
        embedbot.add_field(name='🐍 Python  | Version',
                           value="`3.6.6`")  # Aqui você coloca a versão do python que você está utilizando!
        embedbot.set_footer(
            text="Comando usado por {} as {} Hrs".format(message.author, datetime.datetime.now().hour),
            icon_url=message.author.avatar_url)

        await client.send_message(message.channel, embed=embedbot)
        await client.send_message(message.channel, embed=embe)
    if message.content.lower().startswith('/say'):
        if message.author.server_permissions.administrator:
            try:
                msg = str(message.content).replace("/say ", "")
                if len(msg) >= 1:
                    embed = discord.Embed(description=msg, color=0xFF8000)
                    await client.send_message(message.channel, embed=embed)
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


client.run(os.getenv('TOKEN'))
