import asyncio
import discord
import random
import psutil
import datetime
import time
import copy
from discord.ext import commands
wrap = "```py\n{}\n```"
starttime = time.time()
class Info:
    def __init__(self, bot):
	    self.bot = bot

    def fetch_joined_at(self, user, server):
        """Just a special case for someone special :^)"""
        if user.id == "96130341705637888" and server.id == "133049272517001216":
            return datetime.datetime(2016, 1, 10, 6, 8, 4, 443000)
        else:
            return user.joined_at

    @commands.command(pass_context=True)
    async def support(self, ctx):
        """Support server."""
        await self.bot.whisper("Here is my support server! https://discord.gg/fmuvSX9")

    @commands.command(pass_context=True)
    async def stats(self, ctx):
        """Shows stats."""
        text_channels = 0
        voice_channels = 0 
        mem_v = psutil.virtual_memory()
        cpu_p = psutil.cpu_percent(interval=None, percpu=True)
        cpu_usage = sum(cpu_p)/len(cpu_p)
        online = len([e.name for e in self.bot.get_all_members() if not e.bot and e.status == discord.Status.online])
        idle = len([e.name for e in self.bot.get_all_members() if not e.bot and e.status == discord.Status.idle])
        dnd = len([e.name for e in self.bot.get_all_members() if not e.bot and e.status == discord.Status.dnd])
        offline = len([e.name for e in self.bot.get_all_members() if not e.bot and e.status == discord.Status.offline])
        seconds = time.time() - starttime
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        w, d = divmod(d, 7)
        t1 = time.perf_counter()
        await self.bot.type()
        t2 = time.perf_counter()
        data = discord.Embed(description="Showing stats for {}.".format(self.bot.user.name), colour=discord.Colour.red())
        data.add_field(name="Owner", value="Yσυηg Sιηαтяα™#5484\n146040787891781632")
        data.add_field(name="Ping", value="{}ms".format(round((t2-t1)*1000)))
        data.add_field(name="Servers", value=len(self.bot.servers))
        data.add_field(name="Api version", value=discord.__version__)
        data.add_field(name="Users", value="{} Online<:vpOnline:212789758110334977>\n{} Idle<:vpAway:212789859071426561>\n{} Dnd<:vpDnD:236744731088912384>\n{} Offline<:vpOffline:212790005943369728>".format(online, idle, dnd, offline))
        data.add_field(name="Channels", value="{} Voice Channels\n{} Text Channels".format(len([e for e in self.bot.get_all_channels() if e.type == discord.ChannelType.voice]), len([e for e in self.bot.get_all_channels() if e.type == discord.ChannelType.text])))
        data.add_field(name='CPU usage', value='{0:.1f}%'.format(cpu_usage))
        data.add_field(name='Memory usage', value='{0:.1f}%'.format(mem_v.percent))
        data.add_field(name="Commands", value="{0} active modules, with {1} commands...".format(len(self.bot.cogs), len(self.bot.commands)))
        data.add_field(name='Uptime', value="%d Weeks," % (w) + " %d Days," % (d) + " %d Hours,"
                                   % (
                h) + " %d Minutes," % (m) + " and %d Seconds!" % (s))
        data.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        data.set_thumbnail(url=ctx.message.author.avatar_url)
        await self.bot.say(embed=data)

    @commands.command(pass_context=True, no_pm=True)
    async def serverinfo(self, ctx):
        """Shows servers informations"""
        server = ctx.message.server
        mfa_level = server.mfa_level
        vl = server.verification_level
        total = len([e.name for e in server.members if not e.bot])
        bots = len([e.name for e in server.members if e.bot])
        text_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.text])
        voice_channels = len(server.channels) - text_channels
        passed = (ctx.message.timestamp - server.created_at).days
        created_at = ("**Created {}. {} days ago.**"
                      "".format(server.created_at.strftime("%d %b %Y %H:%M"),
                                passed))

        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        x = -1
        emojis =  []
        while x < len([r for r in ctx.message.server.emojis]) -1:
            x = x + 1
            emojis.append("<:{}:{}>".format([r.name for r in ctx.message.server.emojis][x], [r.id for r in ctx.message.server.emojis][x]))

        data = discord.Embed(
            description=created_at,
            colour=discord.Colour(value=colour))
        data.add_field(name="Info", value=str("**Region:** {0.region}\n**Id:** {0.id}".format(server)))
        data.add_field(name="Users", value="**Humans:** {}\n**Bots:** {}".format(total, bots))
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Verification Level", value=vl)
        data.add_field(name="Require 2FA", value=bool(mfa_level))
        data.add_field(name="Default Channel", value=server.default_channel.mention)
        data.add_field(name="Roles", value=len(server.roles))
        data.set_footer(text="Owner: {}".format(str(server.owner)))

        if server.icon_url:
            data.set_author(name=server.name, url=server.icon_url)
            data.set_thumbnail(url=server.icon_url)
        else:
            data.set_author(name=server.name)
        if server.emojis:
            data.add_field(name="Emotes", value=" ".join(emojis))
        else:
            data.add_field(name="Emotes", value="None")

        try:
            await self.bot.say(embed=data)
        except discord.HTTPException:
            await self.bot.say("Your server perm's are fucked. I need `embed links`.")

    @commands.command(pass_context=True, no_pm=True)
    async def userinfo(self, ctx, *, user: discord.Member=None):
        """Shows userss informations"""
        author = ctx.message.author
        server = ctx.message.server

        if not user:
            user = author

        roles = [x.name for x in user.roles if x.name != "@everyone"]

        joined_at = self.fetch_joined_at(user, server)
        since_created = (ctx.message.timestamp - user.created_at).days
        since_joined = (ctx.message.timestamp - joined_at).days
        user_joined = joined_at.strftime("%d %b %Y %H:%M")
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        member_number = sorted(server.members,
                               key=lambda m: m.joined_at).index(user) + 1

        created_on = "{}\n({} days ago)".format(user_created, since_created)
        joined_on = "{}\n({} days ago)".format(user_joined, since_joined)

        game = "Chilling in {} status".format(user.status)

        if user.game is None:
            pass
        elif user.game.url is None:
            game = "**Playing:** {}".format(user.game)
        else:
            game = "**Streaming:** [{}]({})".format(user.game, user.game.url)

        if roles:
            roles = sorted(roles, key=[x.name for x in server.role_hierarchy
                                       if x.name != "@everyone"].index)
            roles = ", ".join(roles)
        else:
            roles = "None"

        data = discord.Embed(description=game, colour=user.colour)
        data.add_field(name="Name", value=ctx.message.author.name)
        data.add_field(name="ID", value=ctx.message.author.id)
        data.add_field(name="Color", value=ctx.message.author.colour)
        data.add_field(name="Discriminator", value=ctx.message.author.discriminator)
        data.add_field(name="VoiceChannel", value=bool(ctx.message.author.voice_channel))
        data.add_field(name="Nickname", value=ctx.message.author.nick)
        data.add_field(name="Deafened", value=ctx.message.author.self_deaf)
        data.add_field(name="Muted", value=ctx.message.author.self_mute)
        data.add_field(name="Status", value=ctx.message.author.status)
        data.add_field(name="Top Role", value=ctx.message.author.top_role)
        data.add_field(name="Joined Discord on", value=created_on)
        data.add_field(name="Joined this server on", value=joined_on)
        data.add_field(name="All Roles", value=roles, inline=False)
        data.set_footer(text="Member Number: {}"
                             "".format(member_number))
        if user.avatar_url:
            name = str(user)
            name = " ~ ".join((name, user.nick)) if user.nick else name
            data.set_author(name=name, url=user.avatar_url)
            data.set_thumbnail(url=ctx.message.author.avatar_url)
        else:
            data.set_author(name=user.name)

        try:
            await self.bot.say(embed=data)
        except discord.HTTPException:
            await self.bot.say("Your server perm's are fucked. I need `embed links`.")

    @commands.command(pass_context=True)
    async def serveremotes(self, ctx):
        """ServerEmote List"""
        server = ctx.message.server

        list = [e for e in server.emojis if not e.managed]
        emoji = ''
        for emote in list:
            emoji += "<:{0.name}:{0.id}> ".format(emote)
        try:
            await self.bot.say(emoji)
        except:
            await self.bot.say("Server has no emotes.")

    @commands.command(pass_context=True)
    async def inrole(self, ctx, *, rolename):
        """Check members in the role specified."""
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        server = ctx.message.server
        message = ctx.message
        channel = ctx.message.channel
        await self.bot.send_typing(ctx.message.channel)
        therole = discord.utils.find(lambda r: r.name.lower() == rolename.lower(), ctx.message.server.roles)
        if therole is not None and len([m for m in server.members if therole in m.roles]) < 50:
            await asyncio.sleep(1) #taking time to retrieve the names
            server = ctx.message.server
            member = discord.Embed(description="**{1} users found in the {0} role.**\n".format(rolename, len([m for m in server.members if therole in m.roles])), colour=discord.Colour(value=colour))
            member.add_field(name="Users", value="\n".join(m.display_name for m in server.members if therole in m.roles))
            await self.bot.say(embed=member)
        elif len([m for m in server.members if therole in m.roles]) > 50:
            awaiter = await self.bot.say("Getting Member Names")
            await asyncio.sleep(1)
            await self.bot.edit_message(awaiter, " :raised_hand: Woah way too many people in **{0}** Role, **{1}** Members found\n".format(rolename,  len([m.mention for m in server.members if therole in m.roles])))
        else:
            embed=discord.Embed(description="**Role was not found**", colour=discord.Colour(value=colour))
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def emotes(self, ctx):
        """ServerEmote List"""
        server = ctx.message.server

        list = [e for e in server.emojis if not e.managed]
        emoji = ''
        for emote in list:
            emoji += "<:{0.name}:{0.id}> ".format(emote)
        try:
            await self.bot.say(emoji)
        except:
            await self.bot.say("Server has no emotes. :shrug:")

    @commands.command(pass_context=True, no_pm=True)
    async def avatar(self, ctx, *, user: discord.Member=None):
        """Retrieves a users avatar."""
        data = discord.Embed(description="{}, here is {}'s avatar. :writing_hand::skin-tone-3:".format(ctx.message.author.name, user.name), colour=user.colour)
        data.set_image(url=user.avatar_url)
        await self.bot.say(embed=data)

    @commands.command(pass_context=True)
    async def mods(self, ctx):
        """Shows mods in the server."""
        colour = "".join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        server = ctx.message.server
        one = [e.mention for e in server.members if e.permissions_in(ctx.message.channel).manage_messages and not e.bot and e.status == discord.Status.online]
        two = [e.mention for e in server.members if e.permissions_in(ctx.message.channel).manage_messages and not e.bot and e.status == discord.Status.idle]
        three = [e.mention for e in server.members if e.permissions_in(ctx.message.channel).manage_messages and not e.bot and e.status == discord.Status.dnd]
        four = [e.mention for e in server.members if e.permissions_in(ctx.message.channel).manage_messages and not e.bot and e.status == discord.Status.offline]
        embed = discord.Embed(description="Listing mods for this server.", colour=discord.Colour(value=colour))
        if one:
            embed.add_field(name="Online", value=":green_heart: {0}".format((" \n:green_heart: ".join(one)).replace("`", "")), inline=False)
        else:
            embed.add_field(name="Offline", value=":green_heart: None", inline=False)
        if two:
            embed.add_field(name="Idle", value=":yellow_heart: {0}".format((" \n:yellow_heart: ".join(two)).replace("`", "")), inline=False)
        else:
            embed.add_field(name="Idle", value=":yellow_heart: None", inline=False)
        if three:
            embed.add_field(name="Dnd", value=":heart: {0}".format((" \n:heart: ".join(three)).replace("`", "")), inline=False)
        else:
            embed.add_field(name="Dnd", value=":heart: None", inline=False)
        if four:
            embed.add_field(name="Offline", value=":black_heart: {0}".format((" \n:black_heart: ".join(four)).replace("`", "")), inline=False)
        else:
            embed.add_field(name="Offline", value=":black_heart: None", inline=False)
        if server.icon_url:
            embed.set_author(name=server.name, url=server.icon_url)
            embed.set_thumbnail(url=server.icon_url)
        else:
            embed.set_author(name=server.name)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def admins(self, ctx):
        """Shows mods in the server."""
        colour = "".join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        server = ctx.message.server
        one = [e.mention for e in server.members if e.permissions_in(ctx.message.channel).administrator and not e.bot and e.status == discord.Status.online]
        two = [e.mention for e in server.members if e.permissions_in(ctx.message.channel).administrator and not e.bot and e.status == discord.Status.idle]
        three = [e.mention for e in server.members if e.permissions_in(ctx.message.channel).administrator and not e.bot and e.status == discord.Status.dnd]
        four = [e.mention for e in server.members if e.permissions_in(ctx.message.channel).administrator and not e.bot and e.status == discord.Status.offline]
        embed = discord.Embed(description="Listing admins for this server.", colour=discord.Colour(value=colour))
        if one:
            embed.add_field(name="Online", value=":green_heart: {0}".format((" \n:green_heart: ".join(one)).replace("`", "")), inline=False)
        else:
            embed.add_field(name="Offline", value=":green_heart: None", inline=False)
        if two:
            embed.add_field(name="Idle", value=":yellow_heart: {0}".format((" \n:yellow_heart: ".join(two)).replace("`", "")), inline=False)
        else:
            embed.add_field(name="Idle", value=":yellow_heart: None", inline=False)
        if three:
            embed.add_field(name="Dnd", value=":heart: {0}".format((" \n:heart: ".join(three)).replace("`", "")), inline=False)
        else:
            embed.add_field(name="Dnd", value=":heart: None", inline=False)
        if four:
            embed.add_field(name="Offline", value=":black_heart: {0}".format((" \n:black_heart: ".join(four)).replace("`", "")), inline=False)
        else:
            embed.add_field(name="Offline", value=":black_heart: None", inline=False)
        if server.icon_url:
            embed.set_author(name=server.name, url=server.icon_url)
            embed.set_thumbnail(url=server.icon_url)
        else:
            embed.set_author(name=server.name)
        await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        """Shows how long the bot has been online."""
        seconds = time.time() - starttime
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        w, d = divmod(d, 7)
        await self.bot.say("Brooklyn has been up for %d Weeks," % (w) + " %d Days," % (d) + " %d Hours,"
                                   % (
                h) + " %d Minutes," % (m) + " and %d Seconds!" % (s))

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """Pong."""
        channel = ctx.message.channel
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        em = discord.Embed(description="**Pong: {}ms! :ping_pong:**".format(round((t2-t1)*100)), colour=discord.Colour(value=colour))
        await self.bot.say(embed=em)

    @commands.command()
    async def invite(self):
        """Sends invite link for bot."""
        await self.bot.say("Check your pms fam.")
        await self.bot.whisper("**Here is my invite link.**\nhttps://discordapp.com/oauth2/authorize?client_id=226132382846156800&scope=bot&permissions=-1")

    @commands.command(pass_context=True)
    async def roles(self, ctx):
        """States roles from highest to lowest"""
        colour = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)
        list=discord.Embed(description="**Role list for {}.**".format(ctx.message.server.name), colour=discord.Colour(value=colour))
        list.add_field(name="▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬", value=", ".join([x.name for x in ctx.message.server.role_hierarchy if x.name != "@everyone"]))
        await self.bot.say(embed=list)

    @commands.command(pass_context=True)
    async def roleid(self, ctx, rolename):
        """Gives the id of a role, must use quotes."""
        channel = ctx.message.channel
        server = ctx.message.server
        channel = ctx.message.channel
        await self.bot.send_typing(ctx.message.channel)

        role = self._role_from_string(server, rolename)

        if role is None:
            await self.bot.say(embed=discord.Embed(description='Cannot find role!', colour=discord.Colour.red()))
            return

        await self.bot.say(embed=discord.Embed(description=':white_check_mark: **Role id of {} is `{}`**'.format(rolename, role.id), colour=discord.Colour.green()))

    @commands.command(pass_context=True)
    async def roleinfo(self, ctx, rolename):
        """Gives you information about a role."""
        server = ctx.message.server
        role = self._role_from_string(server, rolename)
        since_created = (ctx.message.timestamp - role.created_at).days
        created_on = "{} days ago".format(since_created)
        if role is None:
            embed=discord.Embed(description="**Cannot find role!**", colour=discord.Colour.red())
            await self.bot.say(embed=embed)
            return
        data = discord.Embed(title="Role Information", colour=role.colour)
        data.add_field(name="Name", value=role.name)
        data.add_field(name="Id", value=role.id)
        data.add_field(name="Color", value=role.colour)
        data.add_field(name="Permissions", value=role.permissions.value)
        data.add_field(name="Created on", value=created_on)
        await self.bot.say(embed=data)

    @commands.command(pass_context=True, no_pm=True, hidden=True)
    async def perms(self, ctx):
        user = await self._prompt(ctx, "Mention a user...")
        try:
            if user.mentions is not None:
                user = user.mentions[0]
        except:
            try:
                user = discord.utils.get(ctx.message.server.members, name=str(user.content))
            except:
                return await self.bot.say("User not found!:x:")
        perms = iter(ctx.message.channel.permissions_for(user))
        perms_we_have = "```diff\n"
        perms_we_dont = ""
        for x in perms:
            if "True" in str(x):
                perms_we_have += "+\t{0}\n".format(str(x).split('\'')[1])
            else:
                perms_we_dont += ("-\t{0}\n".format(str(x).split('\'')[1]))
        await self.bot.say("{0}{1}```".format(perms_we_have, perms_we_dont))

    async def _prompt(self, ctx, msg: str):
        await self.bot.say(msg)
        msg = await self.bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
        return msg

    def _role_from_string(self, server, rolename, roles=None):
        if roles is None:
            roles = server.roles
        role = discord.utils.find(lambda r: r.name.lower() == rolename.lower(),
                                  roles)
        return role

def setup(bot):
	bot.add_cog(Info(bot))
