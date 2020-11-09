# •----------Modules-----------•#
import discord, time, platform, psutil, os, math
from datetime import datetime
from cpuinfo import get_cpu_info
from discord.ext import commands
from aiohttp import ClientSession

start_time = datetime.utcnow()

# •----------Class-----------•#


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.process = psutil.Process(os.getpid())

    # •-----------Commands----------•#

    @commands.command(
        name="ping",
        description="Returns the bot's latency and API ping.",
        aliases=["latency"],
    )
    async def pong(self, ctx):
        start = datetime.timestamp(datetime.now())

        msg = await ctx.send("🏓 Pinging....")
        embed = discord.Embed(
            title=" 🏓 Pong!",
            description=f"Latency: {round((datetime.timestamp(datetime.now()) - start ) * 1000) }ms\nAPI Latency: {round(self.client.latency * 1000)}ms",
            color=0x3498DB,
        )
        await msg.edit(content="🏓 Pinging....", embed=embed)
        return

    @commands.command(
        name="uptime", description="Displays the bot's uptime", usage="uptime"
    )
    async def uptime(self, ctx):
        msg = await ctx.send("⏳ Loading....")
        embed = discord.Embed(
            title="📥 Online for",
            description=f"**{parseDur(start_time)}**",
            color=0x3498DB,
        )
        await msg.edit(content="⏳ Loading....", embed=embed)

    @commands.command(
        name="about", description="Returns the bot's about page.", usage="about"
    )
    async def about(self, ctx):
        embed = discord.Embed(
            description=f"Hello! I'm **{self.client.user.name}**, A simple Python Discord bot!\nCreated and maintained by `zhon12345#8585`.\nBuilt using [Python](https://www.python.org/) and [Discord.py](https://discordpy.readthedocs.io/en/latest/)",
            color=0x3498DB,
            timestamp=datetime.utcnow(),
        )
        embed.add_field(
            name="Need some help?",
            value="Join our [Discord Server](https://discord.gg/jMpw3jw)",
            inline=False,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.name}",
        )
        await ctx.send(embed=embed)
        return

    @commands.command(
        name="help",
        description="Returns the help page!",
        aliases=["commands"],
        usage="help [command]",
    )
    async def help(self, ctx: commands.Context, *, cmd=""):
        cmd = cmd.lower().strip()
        command = next(
            (c for c in self.client.commands if cmd == c.name or cmd in c.aliases), None
        )
        if not command:
            embed = discord.Embed(
                title=f"{self.client.user.name}'s Commands",
                description=f"This server's prefix is `{self.client.command_prefix}`.\nFor more info on a specific command, type`{self.client.command_prefix}help <command>`.",
                color=0x3498DB,
                timestamp=datetime.utcnow(),
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.name}",
            )
            cogs = [c for c in self.client.cogs.keys()]
            for cog in cogs:
                cog_commands = self.client.get_cog(cog).get_commands()
                commands_list = ""

                for comm in cog_commands:
                    commands_list += f"`{comm.name}` "

                embed.add_field(
                    name=f"{cog} ({len(cog_commands)})",
                    value=commands_list,
                    inline=False,
                )

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f"Information for {command.name} command",
                description=f"**❯ Name:** {command.name}\n"
                f"**❯ Category:** {command.cog_name}\n"
                f"**❯ Description:** {command.description}\n"
                f"**❯ Usage:** {self.client.command_prefix}{command.usage}\n"
                f"**❯ Aliases:** `{'`, `'.join(command.aliases) if command.aliases else '`None`'}`",
                color=0x3498DB,
                timestamp=datetime.utcnow(),
            )
            embed.set_footer(
                text="Syntax: <> = required, [] = optional",
                icon_url=self.client.user.avatar_url,
            )

            await ctx.send(embed=embed)

    @commands.command(
        name="botinfo",
        description="Displays indept information about the bot.",
        aliases=["bot", "bi"],
        usage="botinfo",
    )
    async def botinfo(self, ctx):
        channels = []
        for channel in self.client.get_all_channels():
            channels.append(channel.name) 
        embed = discord.Embed(
            title="Bot Information",
            color=ctx.guild.me.color,
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(
            name="<:documents:773950876347793449> General ❯",
            value=f"> **\\👑 Owner: `{await self.client.fetch_user(self.client.owner_id)}`**\n"
            f"> **\\🌐 Servers: `{len(self.client.guilds)}` Servers**\n"
            f"> **\\👥 Users: `{len(self.client.users)}` Users**\n"
            f"> **\\📺 Channels: `{len(channels)}` Channels**\n"
            f"> **\\💬 Commands: `{len([x.name for x in self.client.commands])}` Commands**\n"
            "\u200b",
            inline=False,
        )
        embed.add_field(
            name="<:documents:773950876347793449> System ❯",
            value=f"> **<:python:775179429940559912> Python: `v{platform.python_version()}`**\n"
            f"> **<:discordpy:775222608412278784> Discord.py: `v{discord.__version__}`**\n"
            f"> **\\🖥 Platform: `{platform.system()}`**\n"
            f"> **\\📊 Memory: `{self.process.memory_full_info().rss / 1024**2:.2f} MB Used`**\n"
            f"> **\\💻 CPU: `{get_cpu_info()['brand_raw']}`**\n"
            "\u200b",
            inline=False,
        )
        embed.add_field(
            name="<:documents:773950876347793449> Othes ❯",
            value=f"> **<:online:745651877382717560> Uptime: {parseDur(start_time)}**\n"
            f"> **\\📅 Created: `{self.client.user.created_at.strftime('%B %d %Y, %X')}` | `{(datetime.utcnow() - self.client.user.created_at).days}` day(s) ago**\n",
            inline=False,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.name}",
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="serverinfo",
        description="Displays information about the server.",
        aliases=["guildinfo", "server", "guild", "si", "gi"],
        usage="serverinfo",
    )
    async def serverinfo(self, ctx):
        embed = discord.Embed(
            title="Guild Information",
            color=0x3498DB,
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(
            name="<:documents:773950876347793449> General ❯",
            value=f"> **<:card:773965449402646549> Guild Name: `{ctx.guild.name}`**\n"
            f"> **\\📇 Guild ID: `{ctx.guild.id}`**\n"
            f"> **\\👦 Guild Icon: {f'[`Click here!`]({ctx.guild.icon_url})' if ctx.guild.icon_url else '`None`'}**\n"
            f"> **\\👑 Guild Owner: {ctx.guild.owner.mention}**\n"
            f"> **\\🌐 Region: `{str(ctx.guild.region).title()}`**\n"
            f"> **\\✅ Verification Level: `{str(ctx.guild.verification_level).title()}`**\n"
            f"> **\\📅 Created: `{ctx.guild.created_at.strftime('%B %d %Y, %X')}` | `{(datetime.utcnow() - ctx.guild.created_at).days}` day(s) ago**\n"
            "\u200b",
            inline=False,
        )
        embed.add_field(
            name="<:documents:773950876347793449> System ❯",
            value=f"> **\\👥 Member Count: `{ctx.guild.member_count - len([m.bot for m in ctx.guild.members if m.bot])}` Users `{len([m.bot for m in ctx.guild.members if m.bot])}` Bots **\n"
            f"> **\\💬 Channel Count: `{len(ctx.guild.text_channels)}` Text `{len(ctx.guild.voice_channels)}` Voice**\n"
            f"> **<:emojis:774070456059822090> Emoji Count: `{len(ctx.guild.emojis) - len([e.animated for e in ctx.guild.emojis if e.animated])}` Regular `{len([e.animated for e in ctx.guild.emojis if e.animated])}` Animated**\n"
            f"> **<:tier:774071372942147594> Guild Boost Tier: `Tier {ctx.guild.premium_tier}`**\n"
            f"> **<:boost:774071372644483082> Guild Boost Count: `{ctx.guild.premium_subscription_count}` Boost(s)**\n"
            "\u200b",
            inline=False,
        )
        embed.add_field(
            name="<:documents:773950876347793449> Presence ❯",
            value=f"> **<:online:745651877382717560> Online: `{len([m.status for m in ctx.guild.members if m.status == discord.Status.online ])}`**\n"
            f"> **<:idle:773964101390958632> Idle: `{len([m.status for m in ctx.guild.members if m.status == discord.Status.idle ])}`**\n"
            f"> **<:dnd:773964313630998538> Do Not Disturb: `{len([m.status for m in ctx.guild.members if m.status == discord.Status.dnd ])}`**\n"
            f"> **<:offline:745651876552376402> Offline: `{len([m.status for m in ctx.guild.members if m.status == discord.Status.offline ])}`**\n",
            inline=False,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.name}",
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="userinfo",
        description="Displays information about the server.",
        aliases=["user", "ui"],
        usage="userinfo",
    )
    async def userinfo(self, ctx, member: discord.Member = None, *, msg=None):
        member =  member if member else self.client.fetch_user(msg) if member else ctx.author
        embed = discord.Embed(
            title="User Information",
            color=member.color,
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(
            name="<:documents:773950876347793449> User ❯",
            value=f"> **<:card:773965449402646549> Username: `{member}`**\n"
            f"> **\\📇 User ID: `{ctx.guild.id}`**\n"
            f"> **\\👦 Avatar: {f'[`Click here!`]({member.avatar_url})'}**\n"
            f"> **\\📛 Badges: {badges(member)}**\n"
            f"> **<:online:745651877382717560> Status: {status(member.status)}**\n"
            f"> **\\📅 Created: `{member.created_at.strftime('%B %d %Y, %X')}` | `{(datetime.utcnow() - member.created_at).days}` day(s) ago**\n"
            "\u200b",
            inline=False,
        )
        embed.add_field(
            name="<:documents:773950876347793449> Member ❯",
            value=f"> **<:card:773965449402646549> Display Name: `{member.display_name}`**\n"
            f"> **\\🥇 Highest Role: {member.top_role.mention if member.top_role else '`None`'}**\n"
            f"> **\\🏅 Roles: `{len(member.roles) - 1}` Roles**\n"
            f"> **\\📥 Joined: `{member.joined_at.strftime('%B %d %Y, %X')}` | `{(datetime.utcnow() - member.joined_at).days}` day(s) ago**\n",
            inline=False,
        )
        embed.set_footer(
            text=f"Requested by {ctx.message.author.name}",
        )
        await ctx.send(embed=embed)


# •----------Functions-----------•#
def parseDur(time):
    now = datetime.utcnow()
    delta = now - time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "`{d}` days, `{h}` hours, `{m}` minutes, `{s}` seconds"
    elif hours:
        time_format = "`{h}` hours, `{m}` minutes, `{s}` seconds"
    elif minutes:
        time_format = "`{m}` minutes, `{s}` seconds"
    else:
        time_format = "`{s}` second(s)"

    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

    return format(uptime_stamp)

def status(memberStatus):
    if memberStatus == discord.Status.online:
        return "<:online:745651877382717560> `Online`"
    elif memberStatus == discord.Status.idle:
        return "<:idle:773964101390958632> `Idle`"
    elif memberStatus == discord.Status.dnd:
        return "<:dnd:773964313630998538> `Do Not Disturb`"
    else :
        return "<:offline:745651876552376402> `Offline`"

def badges(member):
    if member.public_flags.staff:
        return "<:staff:773961079495196753>"
    elif member.public_flags.partner:
        return "<:partner:773961079185080362>"
    elif member.public_flags.hypesquad:
        return "<:hypesquad:773961079508303892>"
    elif member.public_flags.bug_hunter:
        return "<:bug:773961078245818389>"
    elif member.public_flags.hypesquad_bravery:
        return "<:brave:773961077938454568>"
    elif member.public_flags.hypesquad_brilliance:
        return "<:brillance:773961078114615366>"
    elif member.public_flags.hypesquad_balance:
        return "<:balance:773961077607628810>"
    elif member.public_flags.early_supporter:
        return "<:early:773961079100932166>"
    elif member.public_flags.bug_hunter_level_2:
        return "<:bug2:773961078677045289>"
    elif member.public_flags.verified_bot:
        return "<:verifiedbot:773961079583670322>"
    elif member.public_flags.verified_bot_developer:
        return "<:earlydev:773961079200940074>"
    else:
        return "`None`"
        

def setup(client):
    client.add_cog(Info(client))
    print("Info is loaded")