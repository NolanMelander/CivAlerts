import discord
from discord.ext import commands
import asyncio
import os
import db

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


@bot.command()
async def info(ctx):
    channel = str(ctx.message.channel.name)
    if channel == tChannel:
        embed = discord.Embed(title="Civ Alerts", description="Reminds players to take their turns", color=0xeee657)

        # Personal Info
        embed.add_field(name="Author", value="Nolan Melander")

        # Version Info
        embed.add_field(name="Version", value=version)

        # Version Changes
        embed.add_field(name=version + " changes", value="Pre Alpha Release", inline=False)

        # Footer
        embed.set_footer(text="Version" + version)

        await ctx.send(embed=embed)


@bot.command()
async def linfo(ctx):
    channel = str(ctx.message.channel.name)
    db.db_test()
    if channel == tChannel:
        embed = discord.Embed(title="Leader List", description="List of Leaders", color=0xeee657)

        # Civ Info
        embed.add_field(name="Leader", value="# | Leader | Civilization")
        # Footer
        embed.set_footer(text="Version" + version)

        await ctx.send(embed=embed)


@bot.command()
async def cinfo(ctx):
    channel = str(ctx.message.channel.name)
    if channel == tChannel:
        embed = discord.Embed(title="Civilization List", description="List of Civilizations", color=0xeee657)

        # Civ Info
        embed.add_field(name="Civilization", value="# | Civilization")
        # Footer
        embed.set_footer(text="Version" + version)

        await ctx.send(embed=embed)


@bot.command()
async def commands(ctx):
    channel = str(ctx.message.channel.name)
    if channel == tChannel:
        embed = discord.Embed(title="Command List", description="List of bot commands", color=0xeee657)

        # Footer
        embed.set_footer(text="Version" + version)

        await ctx.send(embed=embed)


bot.run(botToken)
