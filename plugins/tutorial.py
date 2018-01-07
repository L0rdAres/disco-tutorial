from disco.bot import Plugin
from disco.types.message import MessageEmbed
from datetime import datetime
from random import randint

class TutorialPlugin(Plugin):
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
