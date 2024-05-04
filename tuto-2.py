import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f"Le bot est connecté en tant que {bot.user.name} !")

@bot.command()
async def ping(ctx):
    latence = round(bot.latency * 1000)
    await ctx.reply(f"La latence du bot est de {latence}ms")

@bot.command()
async def stats(ctx):
    guild = ctx.guild
    nom = guild.name
    membres = guild.members_count
    salons = len(guild.text_channels) + len(guild.voice_channels)
    await ctx.reply(f"Le serveur {nom} possede {membres}\nIl possede aussi {salons}")
    
bot.run("TOKEN_DU_BOT")