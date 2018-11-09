const Discord = require("discord.js");

module.exports.run = async (bot, message, args) => {
    let bUser = message.guild.member(message.mentions.users.first() || message.guild.members.get(args[0]));
    if(!bUser) return message.channel.send("Não consigo encontrar usuário!");
    let bReason = args.join(" ").slice(22);
    if(!message.member.hasPermission("BAN_MEMBERS")) return message.channel.send("Infelizmente você não tem permissão!");
    if(bUser.hasPermission("BAN_MEMBERS")) return message.channel.send("Essa pessoa não pode ser chutada!");

    let banEmbed = new Discord.RichEmbed()
    .setDescription("BAN")
    .setColor("#bc0000")
    .addField("Usuário banido:", `${bUser} ID ${bUser.id}`)
    .addField("Staff que baniu:", `<@${message.author.id}> ID ${message.author.id}`)
    .addField("Banido no chat:", message.channel)
    .addField("Time", message.createdAt)
    .addField("Motivo:", bReason);

    let incidentchannel = message.guild.channels.find(`name`, "💧ᴘᴜɴɪçᴏᴇs");
    if(!incidentchannel) return message.channel.send("Não encontrei o canal #💧ᴘᴜɴɪçᴏᴇs.");

    message.guild.member(bUser).ban(bReason);
    incidentchannel.send(banEmbed);


    return;
  }

exports.help = {
    name: "ban"
}
