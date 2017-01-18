import discord
from discord.ext import commands

class Random:
    def __init__(self, bot):
	    self.bot = bot
		
    @commands.command(pass_context=True)
    async def randomasscmd(self, ctx):
        """Some random ass fucking command."""
        okay = discord.Embed(description="Something random.", colour=discord.Colour.blue())
        okay.add_field(name="Author", value=ctx.message.author.name)
        okay.add_field(name="Author ID", value=ctx.message.author.id)
        okay.add_field(name="Author Discriminator", value=ctx.message.author.discriminator)
        okay.add_field(name="Author VoiceChannel", value=bool(ctx.message.author.voice_channel))
        okay.set_image(url=ctx.message,author.avatar_url)
		
def setup():
	n = Random(bot)
	bot.add_cog(n)
