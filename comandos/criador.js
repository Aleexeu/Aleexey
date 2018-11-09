const Discord = require("discord.js");

exports.run = (bot,message,args) => {
    let embed = new Discord.RichEmbed()

    .setTitle("CRIADOR")
    .setColor("RANDOM")
    .setDescription(`Oi, eu sou o ${bot.user.username}!\n\n\n Bom meu pai se chama vitor mais o discord dele é Nitroo#4025, quer sugerir algum comando para mim ? entre em contato via discord com ele ele, ele vende bots mais ele não é o melhor ele só sabe o basico, é isso obrigado por ler e tchau!!`)
    .setFooter(`Nitroo#4025`, bot.user.displayAvatarURL);

    message.channel.send(embed);
}

exports.help = {
    name: "criador"
}