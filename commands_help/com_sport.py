import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
serveur_id = int(os.getenv("SERVEUR_ID"))

class Com_Sport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="sport", description="Infrastructures sportives et 70 activités proposées sur les différents campus.")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def aide_sociale(self, interaction: discord.Interaction):
        aide_embed = discord.Embed(
            title="Le sport à l'université ⚽",
            description="Tous les étudiantes et étudiants inscrits à Université Côte d'Azur peuvent bénéficier des infrastructures sportives et des 70 activités proposées sur les différents campus.\n\n"
                        "Comment s'inscrire ? : Dès que votre inscription pédagogique est réalisée, vous pouvez vous inscrire aux activités sportives proposées par la Direction de la Vie Universitaire.\nLe lien : https://sport.univ-cotedazur.fr/fr/\n\n"
                        "De plus vous pouvez gagner des points sur votre moyenne général (+0,25 par semestre) en pratiquant une activité sportive dans le cadre du Bonus Sport. Renseignements et retrait dans le bureau des sports de votre campus de rattachement. Par exemple, un étudiant en Lettres prendra sa carte au Bureau des Sports du campus Carlone.",
            color=discord.Color.dark_grey()
        )
        await interaction.response.send_message(embed=aide_embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Com_Sport(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))