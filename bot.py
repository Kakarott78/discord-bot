import os
import discord
from discord.ext import commands

# Récupérer le token depuis Railway
TOKEN = os.getenv("TOKEN")

# Intents nécessaires
intents = discord.Intents.default()
intents.message_content = True

# Création du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Quand le bot est prêt
@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

# Commande ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong ! 🏓")

# Commande smile
@bot.command()
async def smile(ctx):
    await ctx.send("😊")

# Commande hug
@bot.command()
async def hug(ctx, member: discord.Member):
    await ctx.send(f"{ctx.author.mention} fait un câlin à {member.mention} 🤗")

# Lancer le bot
bot.run(TOKEN)
