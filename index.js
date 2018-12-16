const Discord = require("discord.js");
const config = require("./config.json");
const fs = require("fs");
const bot = new Discord.Client();
bot.commands = new Discord.Collection();

bot.on('guildMemberAdd', member => 
    member.addRole("502505240931860480")
);

bot.on('guildMemberAdd', member => {
    if (member.guild.id !== "500828289150222337") return;
    let avatar = member.user.avatarURL
    let embed = new Discord.RichEmbed()
        .setColor('RANDOM')
        .setThumbnail(avatar)
        .setTitle("**bem-vindo**")
        .addField('<a:9756_AppJedi:523862164587675657>  Bem vindo(a)!', `Bem vindo(a) <@${member.id}> Ao servidor inscrito lindo!`)
        .setFooter(`ID so usuário ${member.id}`, bot.user.displayAvatarURL)
        .setTimestamp()
    bot.channels.get('517158113128874007').send({embed})

});

bot.on("guildMemberRemove", async member => {
    if (member.guild.id !== "500828289150222337") return;
    let avatar = member.user.avatarURL
    let embed = new Discord.RichEmbed()
        .setColor('RANDOM')
        .setThumbnail(avatar)
        .addField('Saida!', `Infelizmente um membro saiu, mais um dia ele volta, nick dele é <@${member.id}>`)
        .setFooter(`ID so usuário ${member.id}`, bot.user.displayAvatarURL)
        .setTimestamp()
    bot.channels.get('517158113128874007').send({embed})

});

fs.readdir("./comandos", (err, files) => {
    if(err) console.error(err);

    let arquivojs = files.filter(f => f.split(".").pop() == "js");
    arquivojs.forEach((f,i) => {
        let props = require(`./comandos/${f}`);
        console.log(`comando ${f} carregado com sucesso.`)
        bot.commands.set(props.help.name, props);
    });
});

bot.on("message", async message => {
    if (!message.member.hasPermission("ADMINISTRATOR")) return; {
  if (message.content.startsWith('https://discord.gg/')) {
        message.delete();
        return message.channel.send(`
<a:Alerta:501028184641241108> Alerta, o ${message.author} está tentando divulgar outro grupo discord! 
<a:Alerta:501028184641241108>`);
        
    }
  } 

});

bot.on('ready', () =>{
    let status = [
        {name: '🍪 Ajuda?│ d!help', type: 'STREAMING', url: 'https://twitch.tv/biscoito'},
        {name: 'humildade pros amigos | Bl3an3k_', type: 'LISTENING'},
        {name: 'Bl3an3k_ no meu coração ❤', type: 'PLAYING'},
        {name: 'os videos do Bl3an3k_ ❤', type: 'WATCHING'},
        {name: 'Fui crado no dia 9 de novembro!', type: 'WATCHING'},
      ];
      
      //STREAMING = Transmitindo
      //LISTENING = Ouvindo
      //PLAYING = Jogando
      //WATCHING = Assistindo
      
        function setStatus() {
            let randomStatus = status[Math.floor(Math.random() * status.length)];
            bot.user.setPresence({game: randomStatus});
        }
      
        setStatus();
        setInterval(() => setStatus(), 10000);  //10000 = 10Ms = 10 segundos
});

bot.on('message', message => {
    if(message.author.bot) return;
    if(message.channel.type === "dm") return;

    let prefix = config.prefix;
    let messageArray = message.content.split(" ");
    let command = messageArray[0];
    let args = messageArray.slice(1);

    if(!message.content.startsWith(prefix)) return;

    let arquivocmd = bot.commands.get(command.slice(prefix.length));
    if(arquivocmd) arquivocmd.run(bot,message,args);
});

bot.login(process.env.BOT_TOKEN);
