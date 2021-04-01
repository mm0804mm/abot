import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, '섹스!!!!')

    elif message.contet.startswith('!say'):
        await client.send_message(message.channel, msg.content)

client.run('ODI3MjExMjg3ODEzMjkyMDYy.YGXuiw.ZRiv8LHsvAu_CX_GyFdNiWkbeXc')