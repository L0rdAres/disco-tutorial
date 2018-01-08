from disco.bot import Plugin
from disco.types.message import MessageEmbed
from datetime import datetime
from random import randint
from disco import client

class TutorialPlugin(Plugin):
    @Plugin.listen('GuildMemberAdd')
    def listen_server(self, event):
        #Looks like we have a new user!
        member = event.member.user
        print(event.member.guild_id)
        if event.member.guild_id == 308697555359760384:
            print('New member dected! Begin Sending DM')
            #This sends the DM to the new user as it should hopefully
            member.open_dm().send_message('Hello {}, \nWe Welcome you to **Game Center Central**! \n'.format(member.username) +
                                         'Before you start chatting, we need to go over a few rules. \n**1.)** Show respect to other members including Server Admins, Mods, Partnered Streamers, and regular members.\n**2.)** Fire off role commands in <#325424576043679754> - This is to help to prevent <#325409734792445952> from getting spammed with bot commands. \n**3.)** When getting tech support always remain calm and try rebooting your computer.\n**4.)** Please do not ping the whole Mod role, if you are needing help please DM <@343849499455913994> ,that will get you in contact with a mod faster than pinging them.\n**5.)** Try not to ping Ares when he is DND, or Offline. Chances is that he is doing something super important. \n**6.)** When going to grab food always go for Chicken nuggets and fries. \n**7.)** Follow Discord ToS and Guidelines.\n**8.)** No Discord Invite Links.\n'+
                                         '**Discord`s Terms and Serivces and Guildelines** \nhttps://discordapp.com/terms \nhttps://discordapp.com/guidelines \nIf you need any help at anytime, please feel free to contact the mods!')
            print('DM Sent! Now waiting for new members!')
    
    @Plugin.command('test')
    def command_test(self, event):
        embed = MessageEmbed()

        #sets the title of the embed
        embed.title = 'Game Center Central'
        embed.set_author(name= 'Game Center Central', url= 'https://discord.ares.party', icon_url= 'https://blog.ares.party/content/images/2018/01/pfp.gif')
        embed.description = 'A server built on on the topics of games and other things.'
        #Inline field 1
        embed.add_field(name='Why is our server different', value='Well, Its different in many ways.')
        #Inline field 2
        embed.add_field(name= 'What does ares break?', value= 'Everything.')
        #Inline field 3
        embed.add_field(name='Can I break things with Ares', value= 'Pls no, We dont need more shit broken kthx.')
        #timestap
        embed.timestamp = datetime.utcnow().isoformat()
        #footer
        embed.set_footer(text='This is the fucking footer you dumb ass.')
        #color
        embed.color = randint(0, 16777215)
        event.msg.reply(embed=embed)

    @Plugin.command('emoji', '<emoji:str...>')
    def command_emoji(self, event, emoji):
        event.msg.reply(emoji)

    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('pong!')

    @Plugin.command('echo', '<content:str...>')
    def on_echo_command(self, event, content):
        event.msg.reply(content)

    @Plugin.command('anthem')
    def command_anthem(self, event):
        event.msg.reply('https://www.youtube.com/watch?v=f2dJxFIV28Y')

    @Plugin.listen('GuildMemberAdd')
    def on_member_add(self, event):
        member = event.member.user
        self.bot.client.api.channels_messages_create(
            399370072612667394,
            '{}, has Joined the server. <a:partyitup:399752483595091972>'.format(member)
        )
    
    @Plugin.listen('GuildMemberRemove')
    def on_member_remove(self, event):
        member = event.user
        self.bot.client.api.channels_messages_create(
            399370072612667394,
            '{} has left the server. <a:blobwave:399753441628651531>'.format(member)
        )

    #B1nzy pls fix soon
    #@Plugin.listen('GuildBanAdd')
    #def on_member_ban(self, event):
        #member = event.user
        #self.bot.client.api.channels_messages_create(
            #399370072612667394,
            #'{} has been banned on the server. <a:partyhell:399756419181838336>'.format(member.name)
        #)