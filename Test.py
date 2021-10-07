import asyncio
import discord

client = discord.Client()

token = "TOKEN HERE"

@client.event

async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("================")

    await client.change_presence(game=discord.Game(name="반갑습니다 :D", type=1))

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel

    if message.content.startswith('!커맨드'):
        await client.send_message(channel,'커맨드')

    else :
        await client.send_message(channel, "<@"+id+">님이 \""+message.content+"\"라고 말하였습니다.")

client.run(token)
                            
