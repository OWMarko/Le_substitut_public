import discord
import os
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv

serveur_id = os.getenv("SERVEUR_ID")

class Com_bâtiments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="bâtiments", description="Commande à utiliser afin de connaître le chemin vers un bâtiment")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def bâtiments(self, interaction: discord.Interaction):

        boutonGC = Button(label="Grand Château", style=discord.ButtonStyle.primary, emoji="🏰")
        boutonMiam = Button(label="Restaurant Universitaire (RU)", style=discord.ButtonStyle.primary, emoji="🍜")
        boutonInfirmerie = Button(label="Infirmerie", style=discord.ButtonStyle.primary, emoji="⚕️")
        boutonScolarité = Button(label="Petit Château, la scolarité", style=discord.ButtonStyle.primary, emoji="🎓")

        async def boutonGC_callback(interaction):
            embed = discord.Embed(
                title="Grand Château", 
                description="Le Grand Château est le beau bâtiment que vous pouvez apercevoir au milieu du campus. Pour y accéder, vous avez plusieurs chemins possibles. Le plus simple est de suivre la route qui se trouve à votre gauche dès que vous entrez sur le campus",
                color=discord.Color.blue()
            )
            embed.set_image(url="https://maphub.net/media/images/r/u6/ru65900wa3opdwsj/1024_768.jpg")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        async def boutonMiam_callback(interaction):
            embed = discord.Embed(
                title="Restaurant Universitaire de 11h30 à 13h45", 
                description="Au premier étage de la résidence universitaire Montebello. Vous pouvez les appeler au : 04 92 07 77 17", 
                color=discord.Color.green()
            )
            embed.set_image(url="https://admin-v2.crous-mobile.fr//media/house/20221116_8c12da9_kpe19mys64kfif4[1].jpg")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        async def boutonInfirmerie_callback(interaction):
            embed = discord.Embed(
                title="Infirmerie", 
                description="L'infirmerie se trouve derrière le bâtiment de Chimie. Il suffit de suivre le chemin principale et prendre à droite au niveau du bâtiment de chimie. Le service médical est dans une petite maisonnette.",
                color=discord.Color.dark_red()
            )
            await interaction.response.send_message(embed = embed,ephemeral = True)
            
        async def boutonScolarité_callback(interaction):
            embed = discord.Embed(
                title="Petit Château, scolarité",
                description="Un des bâtiments incontournables du campus. Continuez tout droit depuis l'entrée du campus et tournez à droite lors de la première intersection.",
                color=discord.Color.orange()
            )
            embed.set_image(url="https://maphub.net/media/images/m/lg/mlg6mekx4gt9rzqi/1024_768.jpg")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        boutonGC.callback = boutonGC_callback
        boutonMiam.callback = boutonMiam_callback
        boutonInfirmerie.callback = boutonInfirmerie_callback
        boutonScolarité.callback = boutonScolarité_callback

        view = View()
        view.add_item(boutonGC)
        view.add_item(boutonMiam)
        view.add_item(boutonInfirmerie)
        view.add_item(boutonScolarité)

        await interaction.response.send_message("Vous êtes perdu ? :", view=view, ephemeral = True)

async def setup(bot):
    await bot.add_cog(Com_bâtiments(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))
