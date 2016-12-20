import discord

class Joinmsg:
    """docstring for join message."""
    def __init__(self, bot):
        self.bot = bot

    async def on_server_join(self, server):
        await self.bot.send_message(server, """**▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬
 Hi! My name is Brooklyn! 
I was made to fill your discord with music and joy!
My command affix is r!!, for all my  commands do r!!help!
Don't be afraid to type r!!support and join that server!
Well, that's it! I hope you enjoy me in your server!
▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬**""")

def setup(bot):
    n = Joinmsg(bot)
    bot.add_cog(n)
