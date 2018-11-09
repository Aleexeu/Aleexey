const Discord = require("discord.js");

exports.run = (bot,message,args) => {
    let embed = new Discord.RichEmbed()

    .setTitle("Não encontrado!")
    .setColor("d! ?")
    .setDescription(`Infelizmente não entendi o comando!\n Digite: d!help`)

    message.channel.send(embed);
}

exports.help = {
    name: ""
}
