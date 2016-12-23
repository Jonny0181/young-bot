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
        
    async def on_server_join(self, message):
        invite = self.bot.create_invite(message.server)
        reqid = message.server.id
        icon = message.server.icon_url
        name = message.server.name
        bot.get_channel(id="261088497543151617")
        data = discord.Embed(description="Brooklyn has joined a new server!", colour=0x3498DB)
        data.add_field(name="Server", value=name)
        data.add_field(name="Invite", value=invite)
        data.add_field(name="ID", value=reqid)
        data.add_field(name="Total servers now", value="{}".format(len(self.bot.servers)))
        if message.server.icon_url:
            data.set_author(name=name, icon=icon)
            data.set_thumbnail(url=icon)
        else:
            data.set_author(name=message.server.name)
        await self.bot.send_message(message.channel, embed=data)

def setup(bot):
    n = Joinmsg(bot)
    bot.add_cog(n)
