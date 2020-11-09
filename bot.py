import os, json, discord
from functions import get
from discord.ext import commands

config = get("config.json")

client = commands.Bot(
    command_prefix=config.prefix,
    owner_id=config.owner_id,
    case_insensitive=True,
    help_command=None,
    intents=discord.Intents.all(),
)

@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Game(name=f"{client.command_prefix}help")
    )
    print(f"Logged in as {client.user.name}")
    print(f"Prefix: {client.command_prefix}")
    for extensions in os.listdir("./cogs"):
        if extensions.endswith(".py"):
            client.load_extension(f"cogs.{extensions[:-3]}")


client.run(config.token)