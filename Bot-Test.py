import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = discord.Client(intents=intents)

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    

client.run('MTA2MjM1MzgwNTQ1NAghhjzhjFAWFjQ0MTM2NQ.Gf87W6.cwRKES9gSgeFhtaguBmCmTi6D2SHuG3N16yZ-tMUA')
