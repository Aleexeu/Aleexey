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

@client.event
async def on_message(message):
    if message.content.lower().startswith('/test'):
        await client.send_message(message.channel, "Olá Mundo, estou vivo!")
    if message.content.lower().startswith('d!vote'):
        vote = message.content[6:].strip()
        votee = await client.send_message(message.channel,
                                          message.author.mention + " **Iniciou uma votaçãơ**\n\n➜``" + vote + "``")
        await client.delete_message(message)
        await client.add_reaction(votee, '👍')
        await client.add_reaction(votee, '👎')
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


client.run(os.getenv('TOKEN'))
