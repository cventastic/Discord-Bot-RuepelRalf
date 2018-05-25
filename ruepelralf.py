import discord
from discord.ext import commands
import asyncio
import random
import logging
import platform
import random
import codecs

 
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='/tmp/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

with codecs.open('zitate.txt', encoding='utf-8', mode='r') as f:
    content = f.readlines()
zlist = [x.rstrip() for x in content]

min = 1 
max = 100

path = '/home/dood/github/discord_api.key'
api_key = open(path,'r').readline()
 
bot = discord.Client()
 
description = '''TEST'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.command()
#@asyncio.coroutine
async def hello():
    await bot.say("HELLO")

 
@bot.event
#@asyncio.coroutine
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="Coding"),afk=True)

@bot.event
async def on_message(message):
        if message.content == '!zitat':
                await bot.send_message(message.channel, content=str(random.choice(zlist)), tts=True, embed=None)
        elif str(message.content).startswith('!roll'):
                limits = []
                try:
                        limits = list(map(int, str(message.content)[4:].split()))
                except:
                        await bot.send_message(message.channel, content=str("Falsche Argumente. Man muss seinen Kopf auch nicht nur als Hutstaender benutzen."))
                        return

                if not len(limits) == 2 and limits[0] < limits[1]:
                        await bot.send_message(message.channel, content=str("Es wurde " + random.randint(limits[0],limits[1]) +  " gewuerfelt. Das ist ein ganz einfacher Algorithmus. Wurzelrechnung ... laecherlich."))
                else:
                        await bot.send_message(message.channel, content=str("Falsche Argumente. Man muss seinen Kopf auch nicht nur als Hutstaender benutzen."))


@bot.command(pass_context=True)
#@asyncio.coroutine
async def joinchannel(ctx):
    channel = ctx.message.author.voice.voice_channel
    #yield from bot.send_message(message.channel, 'quarl',tts=True)
    await bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def roll(ctx):
    channel = ctx.message.author.voice.voice_channel
    msg = random.randint(min, max)
    await bot.send_message(ctx.message.channel, msg)
    await bot.join_voice_channel(channel)


bot.run(api_key.strip())
