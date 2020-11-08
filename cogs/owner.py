# •----------Modules-----------•#
import discord
from datetime import datetime
from discord.ext import commands
from aiohttp import ClientSession

# •----------Class-----------•#


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    # •-----------Commands----------•#

    @commands.command(
        name="shutdown",
        description="Closes connection between discord and shuts the bot down.",
        usage="shutdown",
    )
    async def shutdown(self, ctx):
        if ctx.author.id != self.client.owner_id:
            return

        await ctx.send('⚙ Shutting down...')
        await self.client.logout()

    @commands.command(
        name="dm",
        description="Direct message a specified user as the bot.",
        aliases=["message"],
        usage="dm <user> <text>",
    )
    async def dm(self, ctx, member: discord.Member = None, *, msg: str = None):
        if ctx.author.id != self.client.owner_id:
            return

        if not member:
            await ctx.send("<:vError:725270799124004934> Please provide a valid user.")
            return

        if not msg:
            await ctx.send("<:vError:725270799124004934> Please provide valid text.")
            return

        try:
            await member.send(msg)
            await ctx.send(
                f"<:vSuccess:725270799098970112> Successfully DMed `{member}`"
            )
        except:
            await ctx.send(
                "<:vError:725270799124004934> An error occured, please try again!"
            )

    @commands.command(
        name="say",
        description="Make the bot say whatever you want.",
        aliases=["imitate"],
        usage="say <text>",
    )
    async def say(self, ctx, *, msg: str = None):
        if ctx.author.id != self.client.owner_id:
            return

        if not msg:
            await ctx.send("<:vError:725270799124004934> Please provide valid text.")
            return

        await ctx.send(msg)

    @commands.command(
        name="test",
        description="Checks if the bot is working.",
        usage="test",
    )
    async def test(self, ctx):
        e = discord.Embed(
            title=f"I am working!",
            color=0x3498DB,
        )
        e.set_image(url="https://media.giphy.com/media/gw3IWyGkC0rsazTi/200.gif")

        await ctx.send(embed=e)


def setup(client):
    client.add_cog(Owner(client))
    print("Owner is loaded")