# •----------Modules-----------•#
import discord, time
from datetime import datetime
from discord.ext import commands
from aiohttp import ClientSession

start_time = datetime.utcnow()

# •----------Class-----------•#


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

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
        name="about",
        description="Returns the bot's about page.",
        usage="about"
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
        usage="help [command]"
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

                embed.add_field(name=f'{cog} ({len(cog_commands)})', value=commands_list, inline=False)

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f"Information for {command.name} command",
                description=f"**❯ Name:** {command.name}\n**❯ Category:** {command.cog_name}\n**❯ Description:** {command.description}\n**❯ Usage:** {self.client.command_prefix}{command.usage}\n**❯ Aliases:** `{'`, `'.join(command.aliases) if command.aliases else '`None`'}`",
                color=0x3498DB,
                timestamp=datetime.utcnow(),
            )
            embed.set_footer(
                text="Syntax: <> = required, [] = optional",
                icon_url=self.client.user.avatar_url
            )

            await ctx.send(embed=embed)

    @commands.command(
        name="uptime",
        description="Displays the bot's uptime",
        usage="uptime"
    )
    async def uptime(self, ctx):
        msg = await ctx.send("⏳ Loading....")
        embed = discord.Embed(
            title="📥 Online for",
            description=f"**{parseDur(start_time)}**",
            color=0x3498DB,
        )
        await msg.edit(content="⏳ Loading....", embed=embed)


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


def setup(client):
    client.add_cog(Info(client))
    print("Info is loaded")