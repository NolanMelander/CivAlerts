import discord
from discord.ext import commands
import asyncio
import os

# Tokens & IDS
botToken = os.environ['BOT_TOKEN']
serverID = os.environ['SERVER_ID']
chanID = os.environ['CHANNEL_ID']

# Variable
version = "v0.0.1 - Alpha"

tChannel = os.environ['CHAN']

# Bot Startup
bot = commands.Bot(command_prefix='!', description="A bot that sends reminders for players to take their turns")
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

async def info(ctx):
    channel = str(ctx.message.channel.name)
    if channel == tChannel:
        embed = discord.Embed(title="Civ Alerts", description="Reminds players to take their turns", color=0xeee657)

        # Personal Info
        embed.add_field(name="Author", value="Nolan Melander")

        # Version Info
        embed.add_field(name="Version", value=version)

        # Version Changes
        embed.add_field(name=version + " changes", value="Pre Alpha Release")

        # Footer
        embed.set_footer(text="Version" + version)

        await ctx.send(embed=embed)
