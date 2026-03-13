
import discord
from discord.ext import commands
import random
import os
from PIL import Image, ImageDraw
import aiohttp
import io

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

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

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="hug", description="Faire un câlin")
async def hug(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(hugs)

    if member:
        message = f"{interaction.user.mention} Fait un gros câlin à {member.mention} !"
    else:
        message = f"{interaction.user.mention} Fait un gros câlin."

    await interaction.response.send_message(message)
    await interaction.followup.send(gif)

@bot.tree.command(name="smile", description="Sourire")
async def smile(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(smiles)

    if member:
        message = f"{interaction.user.mention} Sourit pour {member.mention} !"
    else:
        message = f"{interaction.user.mention} Sourit."

    await interaction.response.send_message(message)
    await interaction.followup.send(gif)

@bot.tree.command(name="slap", description="Donner une claque")
async def slap(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(slaps)

    if member:
        message = f"{interaction.user.mention} Donne une claque à {member.mention} !"
    else:
        message = f"{interaction.user.mention} donne une claque dans le vide."

    await interaction.response.send_message(message)
    await interaction.followup.send(gif)

@bot.tree.command(name="cry", description="Pleurer")
async def cry(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(cries)

    if member:
        message = f"{interaction.user.mention} Pleure pour {member.mention}..."
    else:
        message = f"{interaction.user.mention} Pleure..."

    await interaction.response.send_message(message)
    await interaction.followup.send(gif)

@bot.tree.command(name="pat", description="Tapoter quelqu'un")
async def pat(interaction: discord.Interaction, member: discord.Member = None):
    gif = random.choice(pats)

    if member:
        message = f"{interaction.user.mention} Tapote {member.mention} !"
    else:
        message = f"{interaction.user.mention} Tapote."

    await interaction.response.send_message(message)
    await interaction.followup.send(gif)

@bot.tree.command(name="coinflip", description="Pile ou face")
async def coinflip(interaction: discord.Interaction):
    result = random.choice(["Pile !", "Face !"])
    await interaction.response.send_message(result)

@bot.tree.command(name="love", description="Calculer la compatibilité entre deux personnes")
async def love(interaction: discord.Interaction, user1: discord.Member, user2: discord.Member):

    percent = random.randint(0,100)

    async with aiohttp.ClientSession() as session:

        async with session.get(user1.display_avatar.url) as resp:
            avatar1 = Image.open(io.BytesIO(await resp.read())).resize((128,128))

        async with session.get(user2.display_avatar.url) as resp:
            avatar2 = Image.open(io.BytesIO(await resp.read())).resize((128,128))

    image = Image.new("RGB",(400,200),(30,30,30))

    image.paste(avatar1,(20,36))
    image.paste(avatar2,(252,36))

    draw = ImageDraw.Draw(image)

    text = f"❤️ {percent}% ❤️"

    draw.text((150,80),text,fill=(255,255,255))

    buffer = io.BytesIO()
    image.save(buffer,"PNG")
    buffer.seek(0)

    file = discord.File(buffer,filename="love.png")

    await interaction.response.send_message(f"{user1.mention} ❤️ {user2.mention}",file=file)

bot.run(TOKEN)
