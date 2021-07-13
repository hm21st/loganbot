# Import Discord Package
import discord
from discord.ext import commands
import random

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
    
# Website command.
@client.command()
async def website(ctx):
    await ctx.send('https://loganbot.carrd.co/')

# Random Vault Videos
@client.command(aliases=['vault', 'test'])
async def _vault(ctx):
    responses = ['https://cdn.discordapp.com/attachments/760253455629025301/760254401335525416/video0-2.mp4',
                  'https://cdn.discordapp.com/attachments/750076863371673780/752826481129947186/video-1599550804.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/762525574391529524/video0.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/762534065542397982/among_us_meme.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/763562905153044500/20200710-002635-720x1152.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/763562906016546868/20200710-002357-720x1152.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/763581854678253568/video0-28.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/763584037146984479/what_youre_missing_out_on.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/765076386003681317/video0-4.mov',
                  'https://cdn.discordapp.com/attachments/760253455629025301/765080073513467964/video0-2.mov',
                  'https://cdn.discordapp.com/attachments/760253455629025301/765080434081398784/video0-1.mov',
                  'https://cdn.discordapp.com/attachments/760253455629025301/765080453606277140/video0_26.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/765781968503701514/IMG_1558.MP4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/766862938047774740/video0-3.mov',
                  'https://cdn.discordapp.com/attachments/760253455629025301/767233266636816475/video0-45.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/768887789978255360/video0.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/770019245232488478/video0-2.mov',
                  'https://cdn.discordapp.com/attachments/606704596437565442/745778709373517844/video0.mov',
                  'https://cdn.discordapp.com/attachments/861685788755099668/861843112762015794/video0_17.mp4',
                  'https://cdn.discordapp.com/attachments/764166471785775155/863992149267841024/chicken.mp4',
                  'https://cdn.discordapp.com/attachments/589796596749828117/863847499492360232/video0.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/863089022679384074/video0_20.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/862418221961183242/video0_19.mp4',
                  'https://cdn.discordapp.com/attachments/589796640257474590/862181069800341534/sus-1.mp4',
                  'https://cdn.discordapp.com/attachments/722873081231704145/861377438419517440/video0.mov',
                  'https://cdn.discordapp.com/attachments/589796596749828117/851341696398655538/video0-13.mp4',
                  'https://cdn.discordapp.com/attachments/763157201489494027/779774319747137586/video0-3.mp4',
                  'https://cdn.discordapp.com/attachments/722873081231704145/859644848549789706/video0_2.mp4',
                  'https://cdn.discordapp.com/attachments/722873081231704145/859988764037742613/video0.mp4',
                  'https://cdn.discordapp.com/attachments/722873081231704145/859991691527323679/video0.mp4',
                  'https://cdn.discordapp.com/attachments/733025795915776140/832082112361791498/video0.mp4',
                  'https://cdn.discordapp.com/attachments/664991463158841375/812446242398928916/a96e2b5b9041b5dbc8794a5c3c8ea4f73fccfa96b9aa4897b3f19a37ec7a23e6_1.mp4',
                  'https://cdn.discordapp.com/attachments/764166471785775155/833152493985857606/video0.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/859927267399696394/video0_16.mp4',
                  'https://cdn.discordapp.com/attachments/764166471785775155/859211795746521128/fnf.mp4',
                  'https://cdn.discordapp.com/attachments/724376239971893248/858838794164633650/clown.mp4',
                  'https://cdn.discordapp.com/attachments/801810744374198353/816853170923110470/video0.mov',
                  'https://cdn.discordapp.com/attachments/760253455629025301/858144850649415710/video0.mp4',
                  'https://cdn.discordapp.com/attachments/848731017412870185/857034033887313960/video0.mp4',
                  'https://cdn.discordapp.com/attachments/822878306197438494/856952377201786890/video0-7-2.mp4',
                  'https://cdn.discordapp.com/attachments/788886308675780630/857087996721758208/video0_42.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/857068110754349066/video0_15.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/856725763779592212/video0_14.mp4',
                  'https://cdn.discordapp.com/attachments/762038440417165372/856692337869455370/video0.mp4',
                  'https://cdn.discordapp.com/attachments/839537514090987520/856692545487634462/video0.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/856385076765130752/video0_15.mp4',
                  'https://cdn.discordapp.com/attachments/788886308675780630/856296619593695253/video0.mp4',
                  'https://cdn.discordapp.com/attachments/788886308675780630/856266250677125141/video0_5_1.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/854230687984648222/AMONG_US_POOP_1.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/854229545904373801/video0.mov',
                  'https://cdn.discordapp.com/attachments/760253455629025301/854229343404294194/video0.mp4',
                  'https://cdn.discordapp.com/attachments/775564104886648842/817461947049574460/video0.mp4',
                  'https://cdn.discordapp.com/attachments/760253455629025301/854085403690270740/video0.mov',
                  'https://cdn.discordapp.com/attachments/760253455629025301/853699399742128138/video0_13.mp4',
                  'https://cdn.discordapp.com/attachments/825782329384763412/852540772431691776/Dream_Face.mp4']
    await ctx.send(f'Video: {random.choice(responses)}')

# Client run command.
client.run('ClientID')

# And this is the Loganisanigger bot!
