import discord
from discord.ext import commands
import os
import db

# Tokens & IDS
botToken = os.environ['BOT_TOKEN']
serverID = os.environ['SERVER_ID']
chanID = os.environ['CHANNEL_ID']

# Variable
version = "v0.0.2 - Alpha"

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
    if channel == tChannel:
        await ctx.message.delete()
        await ctx.channel.send("... Generating List Please Wait")
        leader = db.linfo()
        await ctx.channel.send("```ID | Leader | Civilization | Alt Civilization```")
        for row in leader:
            if row[3]:
                await ctx.channel.send("```{0} | {1} | {2} | {3}```".format(str(row[0]), str(row[1]), str(row[2])
                                                                             , str(row[3])))
            else:
                await ctx.channel.send("```{0} | {1} | {2} ```".format(str(row[0]), str(row[1]), str(row[2])))


@bot.command()
async def cinfo(ctx):
    channel = str(ctx.message.channel.name)
    if channel == tChannel:
        await ctx.message.delete()
        await ctx.channel.send("...Generating List Please Wait")
        civ = db.cinfo()
        await ctx.channel.send("```ID | Civilization```")
        for row in civ:
            await ctx.channel.send("```{0} | {1}```".format(str(row[0]), str(row[1])))


@bot.command()
async def uregister(ctx, userName: str = None):
    channel = str(ctx.message.channel.name)
    if channel == tChannel:
        register = True
        await ctx.message.delete()
        if userName:
            await ctx.channel.send("...Registering user " + userName)
            userid = ctx.message.author.id
            user = db.uregsiter(userid, userName)
            for row in user:
                register = False
                if row[0] == ctx.message.author.id:
                    await ctx.channel.send("You have already registered with CivAlerts")
                elif row[1] == userName:
                    await ctx.channel.send("The user name " + userName + " already exists")
            if register:
                await ctx.channel.send("...Creating new user")
                db.iuser(userid, userName)
                await ctx.channel.send("...User created with user name " + userName)
        else:
            await ctx.channel.send("Please include username with command ```!uregister userName```")


@bot.command()
async def commands(ctx):
    channel = str(ctx.message.channel.name)
    if channel == tChannel:
        await ctx.message.delete()
        embed = discord.Embed(title="Command List", description="List of bot commands", color=0xeee657)

        # Footer
        embed.set_footer(text="Version" + version)

        await ctx.send(embed=embed)


bot.run(botToken)
