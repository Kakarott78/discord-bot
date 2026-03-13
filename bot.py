import discord
from discord.ext import commands
from discord import app_commands
import random
import os
import aiohttp
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =====================
# GIFS
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
# BOT READY
# =====================

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Connecté en tant que {bot.user}")

# =====================
# COMMANDES
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
    result = random.choice(["Pile", "Face"])
    await ctx.send(f"La pièce tombe sur : **{result}**")

# =====================
# COMMANDE LOVE IMAGE
# =====================

@bot.tree.command(name="love", description="Voir la compatibilité entre deux personnes")
async def love(interaction: discord.Interaction, user1: discord.Member, user2: discord.Member):

    percent = random.randint(0, 100)

    async with aiohttp.ClientSession() as session:
        async with session.get(user1.display_avatar.url) as r:
            avatar1 = Image.open(BytesIO(await r.read())).resize((180,180)).convert("RGBA")

        async with session.get(user2.display_avatar.url) as r:
            avatar2 = Image.open(BytesIO(await r.read())).resize((180,180)).convert("RGBA")

    width = 800
    height = 300

    background = Image.new("RGBA",(width,height),(0,0,0,0))
    draw = ImageDraw.Draw(background)

    for y in range(height):
        r = int(80 + (y/height)*40)
        g = int(120 + (y/height)*60)
        b = 200
        draw.line((0,y,width,y),fill=(r,g,b))

    def round_avatar(img):
        mask = Image.new("L", img.size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((0,0,img.size[0],img.size[1]),fill=255)

        result = Image.new("RGBA",img.size)
        result.paste(img,(0,0),mask)
        return result

    avatar1 = round_avatar(avatar1)
    avatar2 = round_avatar(avatar2)

    background.paste(avatar1,(80,60),avatar1)
    background.paste(avatar2,(540,60),avatar2)

    heart = Image.new("RGBA",(140,120),(0,0,0,0))
    heart_draw = ImageDraw.Draw(heart)

    heart_draw.polygon([
        (70,110),
        (10,50),
        (30,10),
        (70,40),
        (110,10),
        (130,50)
    ], fill=(255,80,120))

    background.paste(heart,(330,90),heart)

    try:
        font = ImageFont.truetype("arial.ttf",40)
    except:
        font = ImageFont.load_default()

    text = f"{percent}%"

    bbox = draw.textbbox((0,0),text,font=font)
    tw = bbox[2]-bbox[0]

    draw.text((400-tw/2,130),text,fill="white",font=font)

    buffer = BytesIO()
    background.save(buffer,"PNG")
    buffer.seek(0)

    file = discord.File(buffer,"love.png")

    await interaction.response.send_message(file=file)

# =====================
# LANCEMENT
# =====================

bot.run(TOKEN)
