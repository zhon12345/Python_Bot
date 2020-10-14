import os
import json
import discord
from discord.ext import commands

client = commands.Bot(
    command_prefix="-", owner_id=450846017890549761, case_insensitive=True
)
config = json.load(open("config.json"))
client.config_token = config["token"]


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="-help"))
    print(f"Logged in as {client.user.name}")
    print(f"Prefix: {client.command_prefix}")
    client.remove_command("help")
    for extensions in os.listdir("./cogs"):
        if extensions.endswith(".py"):
            client.load_extension(f"cogs.{extensions[:-3]}")


client.run(client.config_token)