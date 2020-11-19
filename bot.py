import os, discord
from pathlib import Path
from dotenv import load_dotenv
from discord.ext import commands

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = commands.Bot(
    command_prefix=os.getenv('BOT_PREFIX'),
    owner_id=os.getenv('BOT_OWNER'),
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

client.run(os.getenv('BOT_TOKEN'))