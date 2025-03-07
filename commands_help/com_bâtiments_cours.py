import discord
import os
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv

serveur_id = os.getenv("SERVEUR_ID")

class Com_bâtiments_cours(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="bâtiments_cours", description="Commande à utiliser afin de connaître le chemin vers un bâtiment de cours")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def bâtiments_cours(self, interaction: discord.Interaction):
        
        bouton_BU = Button(label="BU Science", style=discord.ButtonStyle.primary, emoji="📚")
        bouton_Chimie = Button(label="Bâtiment C (salle C..)", style=discord.ButtonStyle.primary, emoji="🧪")
        bouton_M = Button(label="Bâtiment M (salle M..)", style=discord.ButtonStyle.primary, emoji="📐")
        bouton_Physique = Button(label="Bâtiment Physique (salles P...)", style=discord.ButtonStyle.primary, emoji="⚛️")
        bouton_STerre = Button(label="Bâtiment R (Science Naturelle)", style=discord.ButtonStyle.primary, emoji="🪨")
        bouton_PV = Button(label="Petit-Valrose", style=discord.ButtonStyle.primary, emoji="🛕")
        bouton_SCL = Button(label="Labo langue", style=discord.ButtonStyle.primary, emoji="🌐") 
        bouton_SV = Button(label="Bâtiment Q (Science de la Vie)", style=discord.ButtonStyle.primary, emoji="🐢")

        async def bouton_callback_bu(interaction):
            embed = discord.Embed(
                title="BU Science", 
                description="La bibliothèque universitaire de Valrose se trouve en haut du campus, entre le Grand Château et Montebello.",
                color=discord.Color.gold()
                )
            embed.set_image(url="https://maphub.net/media/images/g/do/gdogn8sj9vqvacrz/1024_768.jpg")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        async def bouton_callback_chimie(interaction):
            embed = discord.Embed(
                title="Bâtiment Chimie",
                description="Suivre le chemin principal jusqu'à trouver des bacs de compostage. Ce bâtiment abrite les salles C mais aussi le FabLab et le local du BDE",
                color=discord.Color.gold()
                )
            embed.set_image(url="https://lh5.googleusercontent.com/p/AF1QipPVPs6R1gnz3uzA24cCXM20qmNoccyntmDmEBAG=w750-h401-p-k-no")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        async def bouton_callback_M(interaction):
            embed = discord.Embed(
                title="Bâtiment M",
                description="Monter tout en haut des escaliers... Ce bâtiment abrite les salles M ainsi que l'espace co-working avec des fauteuils confortables.",
                color=discord.Color.gold()
                )
            embed.set_image(url="https://maphub.net/media/images/f/p3/fp3nbhlieshmedqq/1024_768.jpg")
            await interaction.response.send_message(embed = embed,ephemeral = True)
        
        async def bouton_callback_physique(interaction):
            embed = discord.Embed(
                title="Bâtiment Physique",
                description="Ce bâtiment se trouve à mi-chemin du bâtiment M. Pour le reconnaître, il suffit de chercher un bâtiment un peu vieux. Il abrite les salles P.",
                color=discord.Color.gold()
                )
            embed.set_image(url="https://lh5.googleusercontent.com/p/AF1QipNbwtzQQc5PnTj7Bf6jMyhuGZyDOO1-xj_vegd5=w750-h1235-p-k-no")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        async def bouton_callback_sterre(interaction):
            embed = discord.Embed(
                title="Bâtiment R (Science Naturelle)",
                description="Prendre le chemin de droite dès l'entrée du campus, le petit chemin qui monte (celui de gauche).",
                color=discord.Color.gold()
                )
            embed.set_image(url="https://maphub.net/media/images/u/c4/uc4df4hxjlu9hskd/1024_768.jpg")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        async def bouton_callback_pv(interaction):
            embed = discord.Embed(
                title="Petit Valrose",
                description="Le Petit Valrose est le premier bâtiment du campus, il se situe sur la grande avenue Joseph Vallot. Vous y trouverez les salles informatiques pour vos TP, le CRL, le grand amphi de Valrose mais aussi le service d'orientation, le service ERASMUS et bien plus encore.",
                color=discord.Color.gold()
                )
            embed.set_image(url="https://maphub.net/media/images/s/og/sogp7y3vvoa7uzys/1024_768.jpg")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        async def bouton_callback_scl(interaction):
            embed = discord.Embed(
                title="Labo langue",
                description="Pour trouver le laboratoire de langue, il suffit de continuer tout droit lorsqu'on rentre dans le campus. Lorsque tu dépasses la fontaine, vous verrez une intersection entre 2 chemins. Prenez celui qui monte à droite. Celui de gauche vous mène au bâtiment Chimie et vers le grand Château.",
                color=discord.Color.gold()
                )
            embed.set_image(url="https://cdn.discordapp.com/attachments/1014848698368397323/1276535071553224827/IMG20231110101319.jpg?ex=66c9e16d&is=66c88fed&hm=9ddb572f0d00e83135f90b4d2b28b96c24a000b6350d753a2669401bea5111af&")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        async def bouton_callback_sv(interaction):
            embed = discord.Embed(
                title="Bâtiment Q (Science de la Vie)",
                description="Prendre le chemin de droite dès l'entrée du campus, ensuite le petit chemin qui monte (gauche), monter les escaliers. Lorsque vous verrez 2 amphis côte à côte, continuer sur la route pendant 20 mètres.",
                color=discord.Color.gold()
                )
            embed.set_image(url="https://maphub.net/media/images/u/c4/uc4df4hxjlu9hskd/1024_768.jpg")
            await interaction.response.send_message(embed = embed,ephemeral = True)

        bouton_BU.callback = bouton_callback_bu
        bouton_Chimie.callback = bouton_callback_chimie
        bouton_M.callback = bouton_callback_M
        bouton_Physique.callback = bouton_callback_physique
        bouton_STerre.callback = bouton_callback_sterre
        bouton_PV.callback = bouton_callback_pv
        bouton_SCL.callback = bouton_callback_scl
        bouton_SV.callback = bouton_callback_sv

        view = View()
        view.add_item(bouton_BU)
        view.add_item(bouton_Chimie)
        view.add_item(bouton_M)
        view.add_item(bouton_Physique)
        view.add_item(bouton_STerre)
        view.add_item(bouton_PV)
        view.add_item(bouton_SCL)
        view.add_item(bouton_SV)

        await interaction.response.send_message("Où voulez-vous aller ? N'oubliez pas qu'il existe une carte : https://maphub.net/CampusValrose/campus-valrose", view = view, ephemeral = True)

async def setup(bot):
    await bot.add_cog(Com_bâtiments_cours(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))
