import discord
from discord.ext import commands
import random
import os
from datetime import timedelta

# Récupération du token depuis Railway ou ton PC
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
"https://static.klipy.com/ii/935d7ab9d8c6202580a668421940ec81/9b/b4/fIkDNb6B.gif",
"https://static.klipy.com/ii/7607a26399874a14744aa5e7accfa062/b4/b4/tXYJWuWJ.gif",
"https://media.giphy.com/media/svXXBgduBsJ1u/giphy.gif",
"https://static.klipy.com/ii/da290b156d64898341638f3c299e7478/0f/b6/9Hw0gnCu.gif",
"https://static.klipy.com/ii/8ce8357c78ea940b9c2015daf05ce1a5/89/01/FcplPCAE.gif"
]

smiles = [
"https://static.klipy.com/ii/84b4c0b02782dda9051003f9e36484ec/64/c0/weFE0GJI.gif",
"https://static.klipy.com/ii/da290b156d64898341638f3c299e7478/0e/9b/U2jZgDi3.gif",
"https://static.klipy.com/ii/ce286d05b8e1a47cd4f32b0e1b6dec0e/e2/e5/3FyjzI4z.gif",
"https://static.klipy.com/ii/35ccce3d852f7995dd2da910f2abd795/0b/75/V6Ovsu0h.gif",
"https://static.klipy.com/ii/9ed0121ed465c12e1f3dda331ed33f0e/76/9b/W9OPNyQAg2ZxhZH.gif"
]

slaps = [
"https://static.klipy.com/ii/f87f46a2c5aeaeed4c68910815f73eaf/6c/76/LjmbXUjH.gif",
"https://static.klipy.com/ii/4e7bea9f7a3371424e6c16ebc93252fe/76/28/p4wVNMWzErS2h.gif",
"https://static.klipy.com/ii/4e7bea9f7a3371424e6c16ebc93252fe/95/7a/NqbXLkqTL7iDs.gif",
"https://static.klipy.com/ii/f87f46a2c5aeaeed4c68910815f73eaf/4b/2d/yQGkkMtg.gif"
]

cries = [
"https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
"https://static.klipy.com/ii/35ccce3d852f7995dd2da910f2abd795/78/a2/f1ZujK40.gif",
"https://static.klipy.com/ii/e293a233a303a98e471f78d04e13a1b0/d2/92/DKYVyKRl.gif",
"https://static.klipy.com/ii/35ccce3d852f7995dd2da910f2abd795/fd/56/CUZlujdn.gif",
"https://static.klipy.com/ii/71b2873e478b9d8d0482ea3ec777ba7f/3c/42/CVzgVx4J.gif"
]

pats = [
"https://static.klipy.com/ii/e293a233a303a98e471f78d04e13a1b0/0b/b0/Slgsc0jU.gif",
"https://static.klipy.com/ii/2711dd8a75a85be822d136ec94899b3f/ec/4d/45TvCmKY.gif",
"https://static.klipy.com/ii/e293a233a303a98e471f78d04e13a1b0/d3/81/m4XJV7yq.gif",
"https://static.klipy.com/ii/a15b48460c436e1e92c85ffc680932cc/01/76/9iMmxloS.gif"
]

# =====================
# BOT CONNECTÉ
# =====================

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    await bot.tree.sync()

# =====================
# DÉTECTION MOTS
# =====================

@bot.event
async def on_message(message):

    if message.author.bot:
        return

    contenu = message.content.lower()

    if "dianna" in contenu:
        await message.reply("Princesse Dianna tu veux dire plutôt ☺️?")

    if "kakarot" in contenu:
        await message.reply("Mon maître !")

    await bot.process_commands(message)

# =====================
# COMMANDES !
# =====================

@bot.command()
async def hug(ctx, member: discord.Member = None):
    gif = random.choice(hugs)
    if member:
        message = f"{ctx.author.mention} Fait un gros câlin à {member.mention} !"
    else:
        message = f"{ctx.author.mention} Fait un gros câlin."
    await ctx.send(message)
    await ctx.send(gif)

@bot.command()
async def smile(ctx, member: discord.Member = None):
    gif = random.choice(smiles)
    if member:
        message = f"{ctx.author.mention} Sourit pour {member.mention} !"
    else:
        message = f"{ctx.author.mention} Sourit."
    await ctx.send(message)
    await ctx.send(gif)

@bot.command()
async def slap(ctx, member: discord.Member = None):
    gif = random.choice(slaps)
    if member:
        message = f"{ctx.author.mention} Donne une claque à {member.mention} !"
    else:
        message = f"{ctx.author.mention} donne une claque dans le vide."
    await ctx.send(message)
    await ctx.send(gif)

@bot.command()
async def cry(ctx, member: discord.Member = None):
    gif = random.choice(cries)
    if member:
        message = f"{ctx.author.mention} Pleure pour {member.mention}..."
    else:
        message = f"{ctx.author.mention} Pleure..."
    await ctx.send(message)
    await ctx.send(gif)

@bot.command()
async def pat(ctx, member: discord.Member = None):
    gif = random.choice(pats)
    if member:
        message = f"{ctx.author.mention} Tapote {member.mention} !"
    else:
        message = f"{ctx.author.mention} Tapote."
    await ctx.send(message)
    await ctx.send(gif)

@bot.command()
async def coinflip(ctx):
    result = random.choice(["Pile !", "Face !"])
    await ctx.send(result)

# =====================
# MODERATION !
# =====================

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Aucune raison"):
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} a été expulsé. Raison : {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Aucune raison"):
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} a été banni. Raison : {reason}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user)
    await ctx.send(f"{user.name} a été débanni.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} messages supprimés.", delete_after=5)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member, time: int, *, raison="Aucune raison"):
    duration = discord.utils.utcnow() + timedelta(minutes=time)
    await member.timeout(duration, reason=raison)
    await ctx.send(f"{member.mention} est mute pendant {time} minutes. Raison : {raison}")

@bot.command()
@commands.has_permissions(moderate_members=True)
async def untimeout(ctx, member: discord.Member):
    await member.timeout(None)
    await ctx.send(f"{member.mention} n'est plus mute.")

# =====================
# COMMANDES /
# =====================

@bot.tree.command(name="hug", description="Faire un câlin")
async def hug_slash(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(hugs)
    msg = f"{interaction.user.mention} Fait un gros câlin à {member.mention} !" if member else f"{interaction.user.mention} Fait un gros câlin."
    await interaction.response.send_message(msg)
    await interaction.followup.send(gif)

@bot.tree.command(name="smile", description="Sourire")
async def smile_slash(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(smiles)
    msg = f"{interaction.user.mention} Sourit pour {member.mention} !" if member else f"{interaction.user.mention} Sourit."
    await interaction.response.send_message(msg)
    await interaction.followup.send(gif)

@bot.tree.command(name="slap", description="Donner une claque")
async def slap_slash(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(slaps)
    msg = f"{interaction.user.mention} Donne une claque à {member.mention} !" if member else f"{interaction.user.mention} donne une claque dans le vide."
    await interaction.response.send_message(msg)
    await interaction.followup.send(gif)

@bot.tree.command(name="cry", description="Pleurer")
async def cry_slash(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(cries)
    msg = f"{interaction.user.mention} Pleure pour {member.mention}..." if member else f"{interaction.user.mention} Pleure..."
    await interaction.response.send_message(msg)
    await interaction.followup.send(gif)

@bot.tree.command(name="pat", description="Tapoter quelqu'un")
async def pat_slash(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(pats)
    msg = f"{interaction.user.mention} Tapote {member.mention} !" if member else f"{interaction.user.mention} Tapote."
    await interaction.response.send_message(msg)
    await interaction.followup.send(gif)

@bot.tree.command(name="coinflip", description="Pile ou face")
async def coinflip_slash(interaction: discord.Interaction):
    result = random.choice(["Pile !", "Face !"])
    await interaction.response.send_message(result)

# =====================
# MODERATION /
# =====================

@bot.tree.command(name="kick", description="Expulser un membre")
async def kick_slash(interaction: discord.Interaction, member: discord.Member, reason: str = "Aucune raison"):
    if not interaction.user.guild_permissions.kick_members:
        return await interaction.response.send_message("Permission refusée.", ephemeral=True)
    await member.kick(reason=reason)
    await interaction.response.send_message(f"{member.mention} a été expulsé. Raison : {reason}")

@bot.tree.command(name="ban", description="Bannir un membre")
async def ban_slash(interaction: discord.Interaction, member: discord.Member, reason: str = "Aucune raison"):
    if not interaction.user.guild_permissions.ban_members:
        return await interaction.response.send_message("Permission refusée.", ephemeral=True)
    await member.ban(reason=reason)
    await interaction.response.send_message(f"{member.mention} a été banni. Raison : {reason}")

@bot.tree.command(name="unban", description="Débannir via ID")
async def unban_slash(interaction: discord.Interaction, user_id: str):
    if not interaction.user.guild_permissions.ban_members:
        return await interaction.response.send_message("Permission refusée.", ephemeral=True)
    user = await bot.fetch_user(int(user_id))
    await interaction.guild.unban(user)
    await interaction.response.send_message(f"{user.name} a été débanni.")

@bot.tree.command(name="clear", description="Supprimer des messages")
async def clear_slash(interaction: discord.Interaction, amount: int):
    if not interaction.user.guild_permissions.manage_messages:
        return await interaction.response.send_message("Permission refusée.", ephemeral=True)
    await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(f"{amount} messages supprimés.", ephemeral=True)

@bot.tree.command(name="timeout", description="Mute temporaire")
async def timeout_slash(interaction: discord.Interaction, member: discord.Member, time: int, raison: str = "Aucune raison"):
    if not interaction.user.guild_permissions.moderate_members:
        return await interaction.response.send_message("Permission refusée.", ephemeral=True)

    duration = discord.utils.utcnow() + timedelta(minutes=time)
    await member.timeout(duration, reason=raison)
    await interaction.response.send_message(f"{member.mention} mute pendant {time} minutes. Raison : {raison}")

@bot.tree.command(name="untimeout", description="Retirer le mute")
async def untimeout_slash(interaction: discord.Interaction, member: discord.Member):
    if not interaction.user.guild_permissions.moderate_members:
        return await interaction.response.send_message("Permission refusée.", ephemeral=True)
    await member.timeout(None)
    await interaction.response.send_message(f"{member.mention} n'est plus mute.")

# =====================
# LANCEMENT
# =====================

bot.run(TOKEN)
