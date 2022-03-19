import discord
from discord.utils import get
from discord.ext import commands

client = discord.Client()

furry_detector = ["UwU", "OwO","x3","rawr","Rawr","QwQ","TwT","Hewoo","hewoo"]
furry_mention = ["furry","Furry","furras","Furras","furas","Furas"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$hewo'):
        await message.channel.send('Hewooo UwU')

    if any(word in msg for word in furry_detector):
        await message.reply(f"furry detected:{message.author.mention}")

    if any(word in msg for word in furry_mention):
        user_id = "<@517065945366265866>"
        await message.reply(f"did someone mention {user_id} here?")

client.run('TOKEN_HERE') 