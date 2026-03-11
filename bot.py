import discord
from discord.ext import commands
import random
import os

# Récupération du token depuis Railway
TOKEN = os.getenv("TOKEN")

# Intents nécessaires
intents = discord.Intents.default()
intents.message_content = True

# Création du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# =====================
# LISTES DE GIFS
# =====================

hugs = [
"https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
"https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif",
"https://media.giphy.com/media/svXXBgduBsJ1u/giphy.gif",
"https://media.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif"
]

smiles = [
"https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
"https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif",
"https://media.giphy.com/media/l4FGI8GoTL7N4DsyI/giphy.gif",
"https://media.giphy.com/media/3o6Zt6ML6BklcajjsA/giphy.gif"
]

# =====================
# BOT CONNECTÉ
# =====================

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

# =====================
# COMMANDES
# =====================

# Commande !hug
@bot.command()
async def hug(ctx, member: discord.Member):
    gif = random.choice(hugs)
    message = f"{ctx.author.mention} Fait un gros câlin à {member.mention} !"
    await ctx.send(message)
    await ctx.send(gif)

# Commande !smile
@bot.command()
async def smile(ctx, member: discord.Member):
    gif = random.choice(smiles)
    message = f"{ctx.author.mention} Sourit pour {member.mention} !"
    await ctx.send(message)
    await ctx.send(gif)

# Lancement du bot
bot.run(TOKEN)
