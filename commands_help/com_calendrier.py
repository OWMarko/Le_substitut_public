import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

serveur_id = os.getenv("SERVEUR_ID")

class Com_calendrier(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="calendrier", description="Affiche le calendrier de l'année")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def calendrier(self, interaction: discord.Interaction):
        ping_embed = discord.Embed(
            title="Calendrier de l'année scolaire 2024-2025 de l'Université Nice Côte d'Azur",
            description="À télécharger ou à visualiser",
            color=discord.Color.from_rgb(64, 224, 208)
        )
        ping_embed.add_field(
            name="🌍",
            value="Lien pour voir : https://univ-cotedazur.fr/portails/portail-sciences-de-la-vie/documents-utiles/calendrier\n\nLien pour le télécharger : https://univ-cotedazur.fr/medias/fichier/calendrier-valrose-24-25-valrose_1720189503477-pdf?ID_FICHE=1031402&INLINE=FALSE"
        )
        ping_embed.set_footer(
            text=f"Demandé par {interaction.user.name}.",
            icon_url=interaction.user.avatar.url
        )
        await interaction.response.send_message(embed = ping_embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Com_calendrier(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))
