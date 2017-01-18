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
        okay.add_field(name="Author Nickname", value=ctx.message.author.nick)
        okay.add_field(name="Author Deafened", value=ctx.message.author.self_deaf)
        okay.add_field(name="Author Muted", value=ctx.message.author.self_mute)
        okay.add_field(name="Author Status", value=ctx.message.author.status)
        okay.add_field(name="Author TopRole", value=ctx.message.author.top_role)
        await self.bot.say(embed=okay)
		
def setup(bot):
	n = Random(bot)
	bot.add_cog(n)
