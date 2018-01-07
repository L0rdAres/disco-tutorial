from disco.bot import Plugin
from disco.types.message import MessageEmbed
from datetime import datetime
from random import randint
from disco import client

class TutorialPlugin(Plugin):
    @Plugin.listen('GuildCreate')
    def listen_server(self, event):
        owner = event.owner.user
        #owner.open_dm().send_message('Hello {}'.format(owner.username))
        #client.Client.api.channels_messages_create('399370072612667394', 'Guild Owners DM Sent to {}!'.format(owner.username))

    @Plugin.command('test')
    def command_test(self, event):
        embed = MessageEmbed()

        #sets the title of the embed
        embed.title = 'This is a test embed'
        embed.set_author(name= 'LordAres#4401', url= 'https://blog.ares.party', icon_url= 'https://blog.ares.party/content/images/2018/01/pfp.gif')
        embed.url = 'https://discordapp.com'
        embed.description = 'This is an embed'
        #Inline field 1
        embed.add_field(name='Why does Ares break shit?', value='Well. Becuase he can and he does :stuck_out_tongue:')
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