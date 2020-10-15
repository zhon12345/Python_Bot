# •----------Modules-----------•#
import discord
from datetime import datetime
from discord.ext import commands

# •----------Class-----------•#


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # •-----------Commands----------•#

    @commands.command(
        name="avatar",
        description="Get the avatar of the message author or a specified user.",
        usage="avatar (member)",
        aliases=["av", "icon", "pfp"],
    )
    async def avatar(self, ctx, member: discord.Member = None):

        member = ctx.author if not member else member

        e = discord.Embed(
            title=f"{member}'s Avatar",
            url=str(member.avatar_url),
            timestamp=datetime.utcnow(),
            color=0x3498DB,
        )
        e.set_footer(text=f"Requested by {ctx.message.author}")
        e.set_image(url=str(member.avatar_url))

        await ctx.send(embed=e)


def setup(client):
    client.add_cog(Misc(client))
    print("Misc is loaded")