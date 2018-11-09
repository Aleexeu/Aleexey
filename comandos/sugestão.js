const Discord = require("discord.js");

exports.run = (client, message, args) => {
    let suggestmessage = args.join(" ").slice(0);
    let suggestchannel = message.guild.channels.find(c => c.name == "💧sᴜɢᴇsᴛᴏᴇs");

    if (!suggestmessage) {
        return message.reply("Porfavor, insira sua sugestão!")
    }

    let embed = new Discord.RichEmbed()
        .addField("**Sugestão**", `${suggestmessage}`)
        .setFooter(`Sugestão enviado(a) por: ${message.author.tag}`)
        .setTimestamp()
    suggestchannel.send({
        embed
    }).then(msg => {
        msg.react("✅").then(r => msg.react("❎"))
    });


    message.reply(`Sua sugestão foi enviada com sucesso!`)
    return;
}

exports.help = {
    name: "sugestão"
}
