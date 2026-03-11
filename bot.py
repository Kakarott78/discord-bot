import discord
from discord.ext import commands
import random
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

hugs = [
"https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
"https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif"
]

smiles = [
"https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
"https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif"
]

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def hug(ctx):
    await ctx.send(random.choice(hugs))

@bot.command()
async def smile(ctx):
    await ctx.send(random.choice(smiles))

bot.run(TOKEN)
