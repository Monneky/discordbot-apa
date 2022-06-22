## Appa bot
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startwith('$hello'):
        await message.channel.send('hello!')
        
client.run(os.getenv('OTg5MjE2NDMyMjg4MDYzNTY4.G2eMNW.XvjwXPA4jU4Qg2wIFPHtl7KHNRXWt43cTq8egU'))