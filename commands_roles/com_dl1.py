import asyncio
import discord
import os
from discord.ext import commands
from discord.utils import get
from discord import Intents, app_commands, guild
from discord.ui import Select, View
from dotenv import load_dotenv


serveur_id = os.getenv("SERVEUR_ID")
liste_rôle_DL1 = [1152911313534722048, 1152911686228004914, 1152912334055022622, 1152912645448532039]

class Com_DL1(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot

        options = [
            discord.SelectOption(label="DL1 MI", description="Première année de double licence mathématique-informatique", emoji="🖥️"),
            discord.SelectOption(label="DL1 MP", description="Première année de double licence mathématique-physique", emoji="⚛️"),
            discord.SelectOption(label="DL1 C-SV", description="Première année de double licence physique-chimie", emoji="🧪"),
            discord.SelectOption(label="DL1 M-SV", description="Première année de double licence mathématique-science de la vie", emoji="🪝"),
        ]
        super().__init__(placeholder="Veuillez choisir s'il vous plaît.", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        role_name = self.values[0]
        role = discord.utils.get(interaction.guild.roles, name=role_name)
        if role:
            await interaction.user.add_roles(role)
            await interaction.followup.send(f"Votre choix a bien été pris en compte : {role.name}.", ephemeral=True)
        else:
            await interaction.followup.send("Ce choix n'existe pas, contactez un administrateur s'il vous plaît.", ephemeral=True)
        await asyncio.sleep(3)
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False
        await interaction.channel.set_permissions(interaction.user, overwrite=overwrite)

class InitDL1(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.add_item(Com_DL1(bot))

class choix_DL1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="choix_filière_dl1", description="Commande pour choisir votre filière en DL1")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def roles(self, interaction: discord.Interaction):
        guild = interaction.guild
        roles = [guild.get_role(role_id) for role_id in liste_rôle_DL1]
        canal_autorise_id = 1152545626110824568
        if interaction.channel.id != canal_autorise_id:
            await interaction.response.send_message("Vous devez utiliser la commande dans le salon se nommant choix discipline L1. Si vous ne voyez pas ce salon, cela signifie que vous avez déjà choisi votre filière.", ephemeral=True)
            return
        user_roles = interaction.user.roles
        if any(role in user_roles for role in roles):
            await interaction.response.send_message("Vous avez déjà choisi votre filière.", ephemeral=True)
            return
        view = InitDL1(self.bot)
        await interaction.response.send_message("Si vous êtes en double licence :", view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(choix_DL1(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))
