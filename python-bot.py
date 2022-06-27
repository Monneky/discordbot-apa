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

    if message.content.startswith('Yip Yip'):
        await message.channel.send('Hello!')
    elif message.content.startswith('yip yip'):
        await message.channel.send('hello!')

client.run(TOKEN)