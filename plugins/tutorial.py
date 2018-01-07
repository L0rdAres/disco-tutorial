from disco.bot import Plugin
from disco.types.message import MessageEmbed
from datetime import datetime
from random import randint
from disco import client

class TutorialPlugin(Plugin):
    @Plugin.listen('GuildMemberAdd')
    def listen_server(self, event):
        member = event.member.user
        member.open_dm().send_message('Hello {},'.format(member.username))
        member.open_dm().send_message('We Welcome you to server! Before we begin, We need to go over a few rules')
    
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