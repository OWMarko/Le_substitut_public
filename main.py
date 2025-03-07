import discord
import os
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
from discord import Intents, app_commands, guild
from itertools import cycle
from dotenv import load_dotenv

intents = discord.Intents().all()
intents.message_content = True
intents.guilds = True
intents.members = True

load_dotenv(dotenv_path=".env")

bot_id = os.getenv("BOT_ID")
serveur_id = os.getenv("SERVEUR_ID")
bot_token = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix="/", intents=intents, application_id = bot_id)
bot_statuses = cycle(["remplacer OWM","rendre Valrose meilleur"])
serveur_id = 758327235056107612

@tasks.loop(minutes=30)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté")
    print(f"L'ID du bot est : {bot.user.id}")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=serveur_id))
        print(f'Commandes syncro : {len(synced)}')
    except Exception as problemes_slash_commands:
        print(problemes_slash_commands)
    change_bot_status.start()

async def load_extensions():
    for foldername in os.listdir("."):
        if foldername.startswith("commands_") and os.path.isdir(foldername):
            for filename in os.listdir(f"./{foldername}"):
                if filename.endswith(".py"):
                    try:
                        await bot.load_extension(f"{foldername}.{filename[:-3]}")
                        print(f"Les commandes de {filename} dans {foldername} ont été chargées")
                    except Exception as problemes_coms:
                        print(f"Echec du chargement : {filename} dans {foldername}: {problemes_coms}")


bot.setup_hook = load_extensions

async def main():
    async with bot:
        await load_extensions()
        await bot.start(bot_token)

asyncio.run(main())
