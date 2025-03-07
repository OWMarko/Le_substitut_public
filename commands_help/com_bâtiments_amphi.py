import discord
import os
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View

serveur_id = os.getenv("SERVEUR_ID")

class Com_bâtiments_amphi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="bâtiments_amphi", description="Connaître le chemin vers un bâtiment de cours")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def bâtiments_amphi(self, interaction: discord.Interaction):

        bouton_PV = Button(label="Amphi PV", style=discord.ButtonStyle.primary)
        bouton_M = Button(label="Amphi H. Point Carré (M)", style=discord.ButtonStyle.primary)
        bouton_P1 = Button(label="Amphi Physique 1", style=discord.ButtonStyle.primary)
        bouton_P2 = Button(label="Amphi Physique 2", style=discord.ButtonStyle.primary)
        bouton_SN = Button(label="Amphi Science Naturelle (SN)", style=discord.ButtonStyle.primary)
        bouton_BIOLGEOL = Button(label="Amphi Biol & Géol", style=discord.ButtonStyle.primary)
        bouton_Chimie = Button(label ="Amphi Chimie", style = discord.ButtonStyle.primary)

        async def bouton_callback_PV(interaction):
            embed = discord.Embed(
                title="Amphi PV",
                description="Cet amphi se situe au rez-de-chaussée du PV. Lorsque vous rentrez dans le bâtiment continuez tout droit et vous verrez deux grandes portes à votre gauches.",
                color=discord.Color.orange()
                )
            embed.set_image(url="https://maphub.net/media/images/s/og/sogp7y3vvoa7uzys/1024_768.jpg")
            await interaction.response.send_message(embed=embed, ephemeral = True)

        async def bouton_callback_M(interaction):
            embed = discord.Embed(
                title="Amphi H. Point Carré (M)",
                description="Il se situe au niveau des distributeurs automatiques du bâtiment M. Pour s'y rendre, prenez les escaliers et marcher jusqu'à apercevoir le bâtiment Fizeau. Le bâtiment M se situe derrière le beau bâtiment Fizeau (Labo de Physique).",
                color=discord.Color.orange()
                )
            embed.set_image(url="https://maphub.net/media/images/f/p3/fp3nbhlieshmedqq/1024_768.jpg")
            await interaction.response.send_message(embed=embed, ephemeral = True)

        async def bouton_callback_P1(interaction):
            embed = discord.Embed(
                title="Amphi Physique 1",
                description="Suivre le chemin principale, lorsque vous voyez la première intersection, prenez les escaliers et monter jusqu'à la route. Tournez votre tête à gauche, vous verrez un mur avec des dessins, l'amphi est ici.",
                color=discord.Color.orange()
                )
            embed.set_image(url="https://lh5.googleusercontent.com/p/AF1QipP5FZZZrrtrvjzkKYapHp2gWweRUhnT_bMCht3R=w750-h1235-p-k-no")
            await interaction.response.send_message(embed=embed, ephemeral = True)

        async def bouton_callback_P2(interaction):
            embed = discord.Embed(
                title="Amphi Physique 2",
                description="Suivre le chemin principale, lorsque vous voyez la première intersection, prenez les escaliers et monter jusqu'à la route. Tournez votre tête à gauche, vous verrez un mur avec des dessins, l'amphi est ici.",
                color=discord.Color.orange()
                )
            embed.set_image(url="https://maphub.net/media/images/j/sw/jsws1uj8cgqqcqmw/1024_768.jpg")
            await interaction.response.send_message(embed=embed, ephemeral = True)

        async def bouton_callback_BIOLGEOL(interaction):
            embed = discord.Embed(
                title="Amphi Biol & Géol",
                description="Prendre le chemin de droite dès l'entrée du campus, ensuite le petit chemin qui monte (gauche), monter les escaliers. Lorsque vous verrez 2 amphis côte à côte, c'est ici.",
                color=discord.Color.orange()
                )
            embed.set_image(url="https://maphub.net/media/images/u/c4/uc4df4hxjlu9hskd/1024_768.jpg")
            await interaction.response.send_message(embed=embed, ephemeral = True)

        async def bouton_callback_Chimie(interaction):
            embed = discord.Embed(
                title="Amphi Chimie",
                description="Dès l'entrée dans le campus, continuer tout droit. Lorsque vous passerez la fontaine et le lac, vous verrez sur votre droite des escaliers menant vers le haut. Suivez les et vous serez devant l'amphi Chimie.",
                color=discord.Color.orange()
                )
            embed.set_image(url="https://lh5.googleusercontent.com/p/AF1QipNvFCwReEYU6LJUP0Yy3TMo_ExvHqiAxCUIBumC=w750-h1235-p-k-no")
            await interaction.response.send_message(embed=embed, ephemeral = True)

        async def bouton_callback_SN(interaction):
            embed = discord.Embed(
                title="Amphi Science Naturelle (SN)",
                description="Prendre le chemin de droite dès l'entrée du campus, ensuite le petit chemin qui monte (gauche), monter les escaliers. Lorsque vous verrez 2 amphis côte à côte, c'est ici.",
                color=discord.Color.orange()
                )
            embed.set_image(url="https://lh5.googleusercontent.com/p/AF1QipOL7j2Sl9wHqkgUfk39huyoS04hnnu7uBbLZ6au=w750-h1235-p-k-no")
            await interaction.response.send_message(embed=embed, ephemeral = True)

        bouton_PV.callback = bouton_callback_PV
        bouton_M.callback = bouton_callback_M
        bouton_P1.callback = bouton_callback_P1
        bouton_P2.callback = bouton_callback_P2
        bouton_SN.callback = bouton_callback_SN
        bouton_BIOLGEOL.callback = bouton_callback_BIOLGEOL
        bouton_Chimie.callback = bouton_callback_Chimie

        view = View()
        view.add_item(bouton_PV)
        view.add_item(bouton_M)
        view.add_item(bouton_P1)
        view.add_item(bouton_P2)
        view.add_item(bouton_SN)
        view.add_item(bouton_Chimie)
        view.add_item(bouton_BIOLGEOL)

        await interaction.response.send_message("Où voulez-vous aller ? N'oubliez pas qu'il existe une carte : https://maphub.net/CampusValrose/campus-valrose", view=view, ephemeral = True)

async def setup(bot):
    await bot.add_cog(Com_bâtiments_amphi(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))

