const Discord = require("discord.js");
var randomPuppy = require("random-puppy")

module.exports.run = async (bot, message, args) => {
    let member = message.mentions.users.first() || bot.users.get(args[0]) || message.author;
    let avatar = member.displayAvatarURL;
    if (avatar.endsWith(".gif")) {
        avatar = `${member.displayAvatarURL}?size=2048`
    }
    message.channel.send({
        embed: {
            title: `Avatar de: ${member.tag}`,
            description: `Link para baixar o perfil do ${member.tag} logo abaixo!\n[Link Direto](${avatar})`,
            image: {
                url: avatar
            }
        }
    })
}

exports.help = {
    name: "avatar"
}