import discord
import os
from discord.ext import commands
from discord import Intents, Embed, Object
from discord import app_commands
from dotenv import load_dotenv

serveur_id = os.getenv("SERVEUR_ID")

class Com_ping_bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="ping_latence", description="Affiche la latence du bot")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def ping(self, interaction: discord.Interaction):
        ping_embed = Embed(title="Ping", color=discord.Color.random())
        ping_embed.add_field(name=f"{self.bot.user.name} a une latence de :", value=f'{round(self.bot.latency * 1000)} ms.', inline=False)
        ping_embed.set_footer(text=f'Demandé par {interaction.user.name}.', icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed = ping_embed, ephemeral = True)

async def setup(bot):
    await bot.add_cog(Com_ping_bot(bot))
    await bot.tree.sync(guild=Object(id=serveur_id))
