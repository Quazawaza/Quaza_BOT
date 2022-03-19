import discord
import random
import os
import asyncio
from datetime import datetime, time, timedelta
from discord.utils import get
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix="$")
PAPAJ = time(21, 37, 0)
channel_id = 954742894206545950 # Put your channel id here

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

async def called_once_a_day():  # Fired every day
    await bot.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
    channel = bot.get_channel(channel_id) # Note: It's more efficient to do bot.get_guild(guild_id).get_channel(channel_id) as there's less looping involved, but just get_channel still works fine
    await channel.send("Papież pedał dzieci jebał")
    await channel.send(file=discord.File('.\Pope\Pope.jpg'))

async def background_task():
    now = datetime.utcnow()
    if now.time() > PAPAJ:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start 
    while True:
        now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
        target_time = datetime.combine(now.date(), PAPAJ)  # 6:00 PM today (In UTC)
        seconds_until_target = (target_time - now).total_seconds()
        await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
        await called_once_a_day()  # Call the helper function that sends the message
        tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
        seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration


if __name__ == "__main__":
    bot.loop.create_task(background_task())


client.run('TOKEN') 