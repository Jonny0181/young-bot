import discord

class Joinmsg:
    """docstring for join message."""
    def __init__(self, bot):
        self.bot = bot

    async def on_server_join(self, server):
        await self.bot.send_message(server, """**:wave: Hi! My name is Brooklyn, I am here because someone in your server has added me. I was made to fill your discord with music and joy!
My command affix is `r!!`, for all my  commands do `r!!help`!
If you need help with anything please don't be afraid to type `r!!support` and join that server!
Well, that's it! I hope you enjoy me in your server! :white_check_mark:**""")

def setup(bot):
    n = Joinmsg(bot)
    bot.add_cog(n)
