import discord

# Create a new bot instance
client = discord.Client()

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

# Replace YOUR_TOKEN with your bot's token
client.run('MTA2MjM1MzgwNTQ1NjQ0MTM2NQ.Gf87W6.cwRKES9eFhtaguBmCmTi6D2SHuG3N16yZ-tMUA')
