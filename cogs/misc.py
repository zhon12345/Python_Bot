# •----------Modules-----------•#
import discord
from datetime import datetime
from discord.ext import commands
from aiohttp import ClientSession

# •----------Class-----------•#


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # •-----------Commands----------•#

    @commands.command(
        name="avatar",
        description="Get the avatar of the message author or a specified user.",
        usage="avatar [member]",
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

    @commands.command(
        name="randomfact",
        description="Get a random fact from the internet.",
        usage="randomfact"
    )
    async def randomfact(self, ctx):
        url = f"https://useless-facts.sameerkumar.website/api"
        async with ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                fact = r["data"]
                embed = discord.Embed(
                    colour=0x3498DB, timestamp=ctx.message.created_at
                )
                embed.add_field(name="**Fun Fact**", value=fact, inline=False)
                embed.set_footer(text=f"Requested by {ctx.message.author}")
                await ctx.send(embed=embed)
    
    @commands.command(
        name="embed",
        description="Get a example embed.",
        usage="embed"
    )
    async def embed(self, ctx):
        embed = discord.Embed(
            title="title ~~(did you know you can have markdown here too?)~~",
            url="https://discordpy.readthedocs.io/en/latest/index.html",
            description="this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```",
            colour=0x0099ff,
            timestamp=datetime.utcfromtimestamp(1603423631)
        )
        embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_author(name="author name",url="https://discordpy.readthedocs.io/en/latest/index.html")
        embed.set_footer(text="footer text", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

        embed.add_field(name="🤔",value="some of these properties have certain limits...",inline=False)
        embed.add_field(name="😱",value="try exceeding some of them!",inline=False)
        embed.add_field(name="🙄",value="an informative error should show up, and this view will remain as-is until all issues are fixed",inline=False)
        embed.add_field(name="<:thonking:733624898819457087>",value="these last two",inline=True)
        embed.add_field(name="<:thonking:733624898819457087>",value="are inline fields",inline=True)

        await ctx.send(content="this `supports` __a__ **subset** *of* ~~markdown~~ 😃 ```js\nfunction foo(bar) {\n  console.log(bar);\n}\n\nfoo(1);```",embed=embed)


def setup(client):
    client.add_cog(Misc(client))
    print("Misc is loaded")