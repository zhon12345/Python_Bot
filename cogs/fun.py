# •----------Modules-----------•#
from discord.ext import commands
from aiohttp import ClientSession
import json, random, discord, asyncio, html2text

# •----------Class-----------•#


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ses = ClientSession(loop=self.client.loop)

    # •----------Methods/Functions----------•#

    async def nice(self, ctx):
        com_len = len(f"{ctx.prefix}{ctx.invoked_with} ")
        return ctx.message.clean_content[com_len:]

    # •-----------Commands----------•#

    @commands.command(
        name="coinflip",
        description="Heads or Tails?",
        aliases=["cf"],
    )
    async def coinflip(self, ctx):
        coinsides = ["Heads", "Tails"]
        await ctx.send(
            f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!"
        )
        return

    @commands.command(
        name="rate",
        description="How high are you on the ratings?",
    )
    async def rate(self, ctx):
        """ Rates what you desire """
        rate_amount = random.randint(1, 100)
        await ctx.send(
            f"I'd rate **{ctx.author.name}** a **{round(rate_amount, 4)} / 100**"
        )
        return

    @commands.command(
        name="slots",
        description="How lucky are you? Play slots to find out.",
        aliases=["slotmachine", "bet"],
    )
    async def slot(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if a == b == c:
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 matching, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")

    @commands.command(
        name="clapify",
        description="Generate clapified :clap: text :clap:",
        usage="clap <text>",
    )
    async def clap(self, ctx, msg=None):
        if not msg:
            await ctx.send("<:vError:725270799124004934> Please provide valid text.")
            return

        clapped = "👏 " + " 👏 ".join(msg.split(" ")) + " 👏"

        if len(clapped) > 900:
            await ctx.send(
                "<:vError:725270799124004934> The provided message exceeds the character limit."
            )
            return

        await ctx.send(clapped)

    @commands.command(
        name="roast",
        description="Sick of someone? Easy! Just roast them!",
        usage="roast <member>",
    )
    async def roast(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("<:vError:725270799124004934> Please provide a valid user.")
            return

        url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

        r = await self.ses.get(url)
        js = await r.text()
        resp = json.loads(js)

        if r.status != 200:
            await ctx.send(
                "<:vError:725270799124004934> An error occured, please try again!"
            )
            return

        await ctx.send(f"{member.name}, {html2text.html2text(resp['insult'])}")

    @commands.command(
        name="hack",
        description="*Fake* Hacks a user",
        usage="hack <member>",
    )
    async def hack(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send("<:vError:725270799124004934> Please provide a valid user.")
            return

        passwords = [
            "imnothackedlmao",
            "sendnoodles63",
            "ilovenoodles",
            "icantcode",
            "christianmicraft",
            "server",
            "icantspell",
            "hackedlmao",
            "WOWTONIGHT",
            "69420",
        ]

        fakeips = [
            "154.2345.24.743",
            "255.255.255.0",
            "356.653.56",
            "101.12.8.6053",
            "87.231.45.33",
            "91.55.43.8",
        ]

        sec = random.randint(1, 3)

        m = await ctx.send(f"Hacking: **{member.name}** {{0%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Searching for contacts... {{19%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Searching for any friends (if there is any) {{34%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Getting IP... {{55%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Got IP `{random.choice(fakeips)}` {{69%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Getting password... {{84%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Got password `{random.choice(passwords)}` {{99%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Hacking: **{member.name}** {{100%}}")

        await asyncio.sleep(sec)

        embed = discord.Embed(
            title=f"{member} info ",
            description=f"*Email `{member.name}@gmail.com`\nPassword `{random.choice(passwords)}`\nIP `{random.choice(fakeips)}`*",
            color=0x3498DB,
        )
        embed.set_footer(text="You've totally been hacked 😏")
        await m.edit(content=None, embed=embed)

    @commands.command(
        name="8ball",
        description="Ask the magic 8-ball for an answer.",
        aliases=["ask"],
    )
    async def eightball(self, ctx, msg=None):
        if not msg:
            await ctx.send("<:vError:725270799124004934> Please provide a valid user.")
            return

        responses = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Not in a million years",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "¯\\_(ツ)_/¯",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "No",
            "Concentrate and ask again",
            "Don't count on it",
            "An error occured, Please try again",
            "My reply is no",
            "Definetly",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful",
            "Probably",
        ]

        await ctx.send(f"{random.choice(responses)}")

    @commands.command(
        name="dice",
        description="Roll a dice and get a random number from 1 - 6.",
        aliases=["diceroll", "roll"]
    )
    async def dice(self, ctx):
        dice = random.randint(1, 6)
        await ctx.send(
            f"**{ctx.author.name}** rolled a dice and got **{dice}**!"
        )
        return

def setup(client):
    client.add_cog(Fun(client))
    print("Fun is loaded")