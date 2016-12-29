import discord
from discord.ext import commands
from cogs.utils.chat_formatting import pagify

class Testing:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def listservers(self):
        """List servers the bot is in."""
        e = [e.name for e in bot.servers]
        msg = "\n".format(("\n".join(e)))
        something = pagify(msg, ["\n"])
        for page in something:
            self.bot.say(page)

def setup(bot):
    n = Testing(bot)
    bot.add_cog(n)
