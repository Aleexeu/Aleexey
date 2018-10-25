import discord
import asyncio
import random
import datetime
import os
import time
from discord.ext import commands

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
        await client.change_presence(game=discord.Game(name="o desenvolvimento de mais comandos 🔧"))
        await asyncio.sleep(10)
        # Ele vai esperar 60 segundos para mudar para o proximo status
        await client.change_presence(game=discord.Game(name="e ajudando pessoas 👌"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="⭐Fui desenvolvido pelo Nitroo#4025!"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="e olhando meu criador me dando comandos!"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="ajuda ? eu posso te ajudar /help <-"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(
            game=discord.Game(name="🤩 meu criador joga entre 2 jogos minecraft e braains.io!"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="🤩 meu sonho é ficar famoso."))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(
            game=discord.Game(name="😸 Digite /help para você saber os comandos que você pode usar!!."))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="Meu criador está desenvolvendo música para mim.❤️️"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(
            game=discord.Game(name="💚 meu criador está online adicione ele no discord: Nitroo#4025"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(
            game=discord.Game(name="🚀 quer indicar um comando para mim ? Adicione meu criador Nitroo#4025"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo
        await client.change_presence(game=discord.Game(name="🚀 um jogo aleatorio"))
        await asyncio.sleep(10)
        # Depois que esperar 60 segundos ele n vai ter mais oq mudar de status, voltando para o primeiro e refazendo o ciclo


@client.event
async def on_member_join(member):
    cargo = discord.utils.get(member.server.roles, name="Membro")
    await client.add_roles(member, cargo)


@client.event
async def on_message(message):
    if message.content.lower().startswith('/avatar'):
        xtx = message.content.split(' ')
        if len(xtx) == 1:
            useravatar = message.author
            avatar = discord.Embed(
                title="Avatar de: {}".format(useravatar.name),
                color=0xff6e00,
                description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
            )

            avatar.set_image(url=useravatar.avatar_url)
            avatar.set_footer(text="Pedido por {}#{}".format(useravatar.name, useravatar.discriminator))
            await client.send_message(message.channel, embed=avatar)
        else:
            try:
                useravatar = message.mentions[0]
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=0xff6e00,
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)

            except IndexError:
                a = len(prefixo) + 7
                uid = message.content[a:]
                useravatar = message.server.get_member(uid)
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=0xff6e00,
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)
    if message.content.lower().startswith('/ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="🏓 Pong!", color=0x000000,
                                   description='Meu tempo de resposta é `{}ms`!'.format(round((t2 - t1) * 1000)))
        await client.send_message(message.channel, f"{message.author.mention}", embed=ping_embed)
    if message.content.lower().startswith('/abraçar'):
        try:
            hugimg = ['http://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705',
                      'http://media1.tenor.com/images/949d3eb3f689fea42258a88fa171d4fc/tenor.gif?itemid=4900166',
                      'http://media1.tenor.com/images/11889c4c994c0634cfcedc8adba9dd6c/tenor.gif?itemid=5634578',
                      'http://media1.tenor.com/images/d7529f6003b20f3b21f1c992dffb8617/tenor.gif?itemid=4782499',
                      'https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif?itemid=9200935',
                      'https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/tenor.gif?itemid=11074788',
                      'https://media1.tenor.com/images/3c83525781dc1732171d414077114bc8/tenor.gif?itemid=7830142']
            hug = random.choice(hugimg)
            hugemb = discord.Embed(title='Abraço :heart:',
                                   description='**{}** Ele(a) recebeu um abraço de **{}**! Casal Fofo! :heart_eyes: '
                                   .format(message.mentions[0].name, message.author.name), color=0xff6e00)
            hugemb.set_image(
                url=hug)
            hugemb.set_footer(text="MitologyCraft BOT © 2018")
            await client.send_message(message.channel, embed=hugemb)
        except IndexError:
            await client.send_message(message.channel, 'Você precisa mencionar um usuário específico para abraçar!')
    if message.content.lower().startswith('/help'):
        await client.send_message(message.channel,
                                  "{} <a:YeetusDeletusDance:504759030858907650>,\nMeus comandos abaixo,\n \n \nAdmins:\n/ban (para banir o player),\n/say (para escrever algo.)\n \n \nMembros:\n/help (para você ver meus comandos)\n/juntarnomes (para juntar um nick com o outro)!\n/abraçar (abraçar sua amiga ou amigo <3).\n/ping (para você ver meu tempo de resposta.).\n/serverinfo (para você ver as configuraçoes do server discord.).\n/avatar (para ver o seu avatar ou o avatar de alguém).".format(
                                      message.author.mention))
    if message.content.lower().startswith("/serverinfo"):
        horario = datetime.datetime.now().strftime("%H:%M:%S")
    embed = discord.Embed(title="\n",
                          description="Abaixo está as informaçoes principais do servidor!")
    embed.set_thumbnail(url=message.server.icon_url)
    embed.set_footer(text="{} • {}".format(message.author, horario))
    embed.add_field(name="Nome:", value=message.server.name, inline=True)
    embed.add_field(name="Dono:", value=message.server.owner.mention)
    embed.add_field(name="ID:", value=message.server.id, inline=True)
    embed.add_field(name="Cargos:", value=str(len(message.server.roles)), inline=True)
    embed.add_field(name="Canais de texto:", value=str(
        len([c.mention for c in message.server.channels if c.type == discord.ChannelType.text])),
                    inline=True)
    embed.add_field(name="Canais de voz:", value=str(
        len([c.mention for c in message.server.channels if c.type == discord.ChannelType.voice])),
                    inline=True)
    embed.add_field(name="Membros:", value=str(len(message.server.members)), inline=True)
    embed.add_field(name="Bots:",
                    value=str(len([a for a in message.server.members if a.bot])),
                    inline=True)
    embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"),
                    inline=True)
    embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
    await client.send_message(message.channel, embed=embed)
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
        canal = client.get_channel('504732378846199820')
        embed = discord.Embed(colour=0xFFA500, description="+ 1 banido")
        embed.add_field(name='`👤 | Úsuario banido:`', value=banido.content)
        await client.send_message(canal, embed=embed)

client.run(os.getenv('TOKEN'))
