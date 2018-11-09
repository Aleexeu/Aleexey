const Discord = require("discord.js");

exports.run = (bot,message,args) => {
    let gAvatar = message.guild.iconURL;
    let embed = new Discord.RichEmbed()

    .setColor("RANDOM")
    .setDescription(`Oi, eu sou o ${bot.user.username}! Aqui está meus comandos.\n \n \n|Administrador|:\n \nd!ban [PARA BANIR UM MEBRO QUE NÃO ENTÁ OBEDECENDO AS REGRAS].\n \nd!say [PARA ENVIAR UMA MENSAGEM].\n \nd!kick [PARA CHUTAR A PESSOA PRA FORA DO SERVIDOR DISCORD].\n \nd!tempmute [@usuário 10s/10h/10d motivo].\n \n \n|MEMBROS|:\n \nd!help [PARA VOCÊ VER MEUS COMANDOS].\n \nd!serverinfo [PARA VOCÊ VER AS INFORMAÇÕES DO SERVIDOR DISCORD].\n \nd!memes [EM DESENVOLVIMENTO].\n \nd!ping [PARA VER O PING DO BOT].\n \nd!criador [PARA SABER QUEM ESTÁ ME DESENVOLVENDO/CRIO].\n \nd!time [PARA VER QUANTO TEMPO EU ESTOU ONLINE].\n \nd!sugestão [PARA ENVIAR UMA SUGESTÃO].\n \nd!avatar [PARA VER O SEU AVATAR OU AVATAR DE OUTRA PESSOA].\n \nd!userinfo [PARA SABER AS INFORMAÇÕES DO PLAYER].\n \n \nO bot ainda está em desenvolvimento então temos poucos comandos.`)

    message.author.send(embed);
    message.reply('**olhe na sua DM** :wink:');
}

exports.help = {
    name: "help"
}
