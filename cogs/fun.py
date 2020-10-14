import random
import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

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


def setup(client):
    client.add_cog(Fun(client))
    print("Fun is loaded")