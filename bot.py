import discord
from discord.ext import commands
from patch import lol_patch, lol_patch_link
from steam import steam_search, steam_search_price
import random

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print('Bot is activated')


@client.command()
async def patch(ctx):
    link_to_print = lol_patch_link()
    patch_to_print = '\n'.join(lol_patch())
    await ctx.send(link_to_print)
    await ctx.send("```" + patch_to_print + "```")



@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')



@client.command()
async def opgg(ctx, *, name):
    sum_name = str(name)
    sum_name = sum_name.replace(' ', '+')
    await ctx.send('https://na.op.gg/summoner/userName=' + sum_name)


@client.command()
async def steam(ctx, *, item):
    steam_game = steam_search(item)
    if steam_game is None:
        steam_game = "Can't find your game."
    # steam_game_price = steam_search_price(item)
    await ctx.send(steam_game)
    # await ctx.send(steam_game_price)


@client.command()
async def commands(ctx):
    await ctx.send('```.patch: Gives a summary of newest LoL patch notes.\n.opgg: Links the opgg of the name entered.\n.steam: Links game and price of the game entered.\n```')

Token = open("token.txt", "r").read().rstrip()
client.run('Token')
