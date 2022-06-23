## Appa bot
import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello') or message.content.startwith("hello"):
        await message.channel.send('Hello!')

client.run(TOKEN)