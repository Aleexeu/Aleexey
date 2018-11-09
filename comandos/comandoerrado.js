const Discord = require("discord.js");

exports.run = (bot,message,args) => {
    let embed = new Discord.RichEmbed()

    .setTitle("Não encontrado!")
    .setColor("d! ?")
    .setDescription(`b! é o k7, o bagulho é d!help`)

    message.channel.send(embed);
}

exports.help = {
    name: ""
}
