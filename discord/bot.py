import discord
from config import *
import asyncio
from discord.ext import commands
from apikey import kluch
import requests
import json
import string

bot = commands.Bot(command_prefix='#',
description='''Every Nansense Project, every command has an info function''')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    game = discord.Game("#help")
    await bot.change_presence(activity=game, status=discord.Status.dnd)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def apex(ctx, username=None):
    """Checks your stats in apex legends"""
    
    # Check if user has provided username
    if not username:
        await ctx.send("Please give me an Origin username")
        await ctx.send("`usage: #apex username`")
        return

    # If user provides info as input, print information about the command
    elif str(username) == "info":
        await ctx.send("The #apex function was added on 20.06.2020 as an excercise in requests, json, dicts, lists and if statements  ")
    else:
        r = requests.get("https://public-api.tracker.gg/v2/apex/standard/profile/5/{}".format(username), headers={"TRN-Api-Key": str(kluch)})       

        # Check if the account exists or not
        if str(r) == "<Response [200]>":
            print("Account Exists")
            # Variables for easier json scraping
            naenae = r.json()["data"]
            legend = naenae["segments"]     
            legendname = legend[1]["metadata"]["name"]

            # Trying to see if you have the kills banner on 
            if "kills" in legend[1]["stats"].keys():
                kills = legend[1]["stats"]["kills"]["value"]
                await ctx.send("Your last played legend is: {}".format(legendname))      
                await ctx.send("Your kills with {} are: {}".format(legendname, int(kills)))
                return
            else:
                return await ctx.send("You don't have the kills banner on {}".format(legendname))
        else:
            await ctx.send("Account doesn't exist or API error")
            print("Account doesn't exist or API error")
            return

@bot.command()
async def emojitalk(ctx, userSays=None, AsAList=False):

    alphabet = list(string.ascii_lowercase)
    discord = [str(f":regional_indicator_{i}:") for i in alphabet]
    disctionary = dict(zip(alphabet, discord))
    print(userSays)
    await ctx.send(userSays)
    if not userSays:
        await ctx.send("Please say something")
        return
    else:
        userList = [char for char in userSays]
        print(userList)
        for word in userList:
            finalResult = disctionary[word]
            finalList = []
            finalList.append(str(finalResult))
            if AsAList is True:
                await ctx.send(finalList)
                asyncio.sleep(2)
            else:
                finalString='  '.join(finalList)
                await ctx.send(finalString)
        return
        
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(bot.start(TOKEN))
except KeyboardInterrupt:
    loop.run_until_complete(bot.logout())
finally:
    loop.close()
