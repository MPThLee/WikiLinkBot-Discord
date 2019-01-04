import discord
import asyncio
import logging
import sys
import re
import setting

logging.basicConfig(level=logging.INFO)

TOKEN = setting.TOKEN
BASEURL = setting.BASEURL
INTERWIKI = setting.INTERWIKI

client = discord.Client()

linkRegex = re.compile(r'\[\[(.+?)(#.*)?(?:\?.+?)?(#.+)?\]\]') # remove Query strings.
def sgr(s):
    return str(s or '').replace(' ', '_')

# https://github.com/Rapptz/discord.py/issues/1249
# Use rewrite branch on Python>=3.7
# Install Rewrite branch: python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/async.zip#egg=discord.py
async def send_message(message: discord.Message, msg: str):
    if sys.version_info >= (3, 7):
        await message.channel.send(msg)
    else:
        await client.send_message(message.channel, msg)

def link(arg: str):
    split = arg.split(':', 1)
    interwiki = INTERWIKI.get(split[0].lower(), BASEURL)
    if interwiki == BASEURL:
        return '{}{}'.format(BASEURL, arg)

    return '{}{}'.format(interwiki, split[1])


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if linkRegex.search(message.content):
        for i in linkRegex.finditer(message.content):
            if i[1] is None:
                return
            
            if i[2] is not None:
                title = sgr(i[1])+sgr(i[2])
            elif i[3] is not None:
                title = sgr(i[1])+sgr(i[3])
            else:
                title = sgr(i[1])

            msg = '[[{}]]: {}'.format(title, link(title))
            
            await send_message(message, msg)

client.run(TOKEN)