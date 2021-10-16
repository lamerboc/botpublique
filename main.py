import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix = "!", description = "Robot discord") 

@bot.event()
async def on_ready()
    print("Je suis connecter sur discord | Prêt a etre utiliser !")
    
@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou !")

@bot.command()
@commands.has_permissions(administrateur=True)
async def warn(ctx, user, *reason)
    await ctx.send(f"Je viens de avertir {user} pour la raison : {reason}")

bot.run("LOGIN.TOKEN.BOT.DISCORD")
