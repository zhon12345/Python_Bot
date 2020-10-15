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
        aliases=["commands", "command"],
        usage="cog",
    )
    async def help(self, ctx, cog="all"):
        help_embed = discord.Embed(
            title=f"{self.client.user.name}'s Commands",
            description=f"This server's prefix is `{self.client.command_prefix}`.",
            color=0x3498DB,
            timestamp=datetime.utcnow(),
        )
        help_embed.set_footer(
            text=f"Requested by {ctx.message.author.name}",
        )

        cogs = [c for c in self.client.cogs.keys()]
        if cog == "all":
            for cog in cogs:
                cog_commands = self.client.get_cog(cog).get_commands()
                commands_list = ""

                for comm in cog_commands:
                    commands_list += f"`{comm.name}` "

                help_embed.add_field(name=cog, value=commands_list, inline=False)
            pass
        else:
            lower_cogs = [c.lower() for c in cogs]
            if cog.lower() in lower_cogs:
                commands_list = self.client.get_cog(
                    cogs[lower_cogs.index(cog.lower())]
                ).get_commands()
                help_text = ""

                for command in commands_list:
                    help_text += (
                        f"```{command.name}```\n" f"**{command.description}**\n\n"
                    )

                    if len(command.aliases) > 0:
                        help_text += (
                            f'**Aliases :** `{"`, `".join(command.aliases)}`\n\n'
                        )
                    else:
                        help_text += "\n"

                    help_text += (
                        f"Format: `{self.client.command_prefix}"
                        f' {command.name} {command.usage if command.usage is not None else ""}`\n\n'
                    )

                help_embed.description = help_text
            else:
                await ctx.send(
                    "Invalid cog specified.\nUse `help` command to list all cogs."
                )
                return

        await ctx.send(embed=help_embed)
        return

    @commands.command(
        name="uptime",
        pass_context=True,
    )
    async def uptime(self, ctx):

        now = datetime.utcnow()
        delta = now - start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days:
            time_format = (
                "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
            )
        else:
            time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."

        uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

        msg = await ctx.send("⏳ Loading....")
        embed = discord.Embed(
            title="📥 Online for",
            description=f"{format(uptime_stamp)}",
            color=0x3498DB,
        )
        await msg.edit(content="⏳ Loading....", embed=embed)

    @commands.command(
        name="randomfact",
        description="Get a random fact from the internet."
    )
    async def randomfact(self, ctx):
        url = f"https://useless-facts.sameerkumar.website/api"
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                fact = r["data"]
                embed = discord.Embed(
                    colour=ctx.author.colour, timestamp=ctx.message.created_at
                )
                embed.add_field(name="**Fun Fact**", value=fact, inline=False)
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))
    print("Info is loaded")