# Import Discord Package
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ';')

# The event that makes the bot be online, with the game, and the Print command in console.
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(name="todd jokes. prefix is ';'"))
    print('Logan is ready to pretend to be active.')

# This is the latency command. It tells you the latency.
@client.command()
async def ping(ping):
        await ping.send(f'Pong! {round(client.latency * 1000)}ms')

# This is the main command, the Nigger command. It posts a funny.
@client.command()
async def nigger(nigger):
        await nigger.send('Logan (<@620732485612994631>) pretending to be active https://tenor.com/view/brick-gif-20174929')

# Logan is very gay.
@client.command()
async def gay(gay):
    await gay.send('I am Logan and I am very gay <@620732485612994631>')

# MASS ping of Logan.
@client.command()
async def p(pinglol):
    await pinglol.send('<@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631> <@620732485612994631>')

# Logan is so funny!
@client.command()
async def funny(funny):
    await funny.send('okay funny boy <@620732485612994631>')

# Client run command.
client.run('ClientID')

# And this is the Loganisanigger bot!
