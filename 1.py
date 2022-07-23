import discord
from discord.ext import commands
import linecache
import os

os.startfile("Joiner.exe")

token = linecache.getline("tokens.txt", 1)
msg = linecache.getline("messages.txt", 1)


x = input("Channel ID: ")
os.system('cls')

slav = commands.Bot(command_prefix='!', case_insensitive = True, self_bot=True)

@slav.event
async def on_ready():
    print(f"logged in as {slav.user}")
    channel = slav.get_channel(x)
    while True:
        await channel.send(msg)





slav.run(token, bot=False)