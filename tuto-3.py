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
async def userinfo(ctx, membre: discord.Member):
    nom = membre.name
    userid = membre.id
    date = membre.created_at
    join = membre.joined_at
    avatar = membre.avatar
    await ctx.reply(f"Le membre {nom} avec l'id {userid} a cree son compte le {date}\nIl a rejoin le serveur {join}")
    await ctx.reply(avatar)
    
bot.run("TOKEN_DU_BOT")