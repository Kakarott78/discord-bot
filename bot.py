import discord
from discord.ext import commands
import random
import os

# On récupère le token depuis Railway
TOKEN = os.getenv("TOKEN")

# On active les intents pour lire les messages
intents = discord.Intents.default()
intents.message_content = True

# On crée le bot avec préfixe "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# =====================
# LISTES DE GIFS
# =====================

# GIFs pour !hug
hugs = [
    "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
    "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
    "https://media.giphy.com/media/svXXBgduBsJ1u/giphy.gif",
    "https://media.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif"
]

# GIFs pour !smile
smiles = [
    "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
    "https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif",
    "https://media.giphy.com/media/l4FGI8GoTL7N4DsyI/giphy.gif",
    "https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif"
]

# =====================
# ÉVÉNEMENT DE CONNEXION
# =====================

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

# =====================
# COMMANDES DU BOT
# =====================

# !hug
@bot.command()
async def hug(ctx, member: discord.Member):
    gif = random.choice(hugs)
    await ctx.send(f"{ctx.author.mention} fait un gros calin a {member.mention}")
    await ctx.send(gif)

# !smile
@bot.command()
async def smile(ctx, member: discord.Member):
    gif = random.choice(smiles)
    await ctx.send(f"{ctx.author.mention} sourit pour {member.mention}")
    await ctx.send(gif)

# =====================
# LANCEMENT DU BOT
# =====================

bot.run(TOKEN)
