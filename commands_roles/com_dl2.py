import asyncio
import discord
import os
from discord.ext import commands
from discord.utils import get
from discord import Intents, app_commands
from discord.ui import Select, View
from dotenv import load_dotenv

load_dotenv()
serveur_id = int(os.getenv("SERVEUR_ID"))
liste_rôle_DL2 = [1152920186870050826, 1152920439069347902, 1152925252372926485, 1152925960883146793]

class Com_discipline_DL2(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        options = [
            discord.SelectOption(label="DL2 MI", description="Deuxième année de double licence mathématique-informatique", emoji="🖥️"),
            discord.SelectOption(label="DL2 MP", description="Deuxième année de double licence mathématique-physique", emoji="⚛️"),
            discord.SelectOption(label="DL2 C-SV", description="Deuxième année de double licence physique-chimie", emoji="🧪"),
            discord.SelectOption(label="DL2 M-SV", description="Deuxième année de double licence mathématique-science de la vie", emoji="🪝"),
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

class InitDL2(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.add_item(Com_discipline_DL2(bot))

class choix_DL2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="choix_filière_dl2", description="Commande pour choisir votre filière en DL2")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def roles(self, interaction: discord.Interaction):
        guild = interaction.guild
        roles = [guild.get_role(role_id) for role_id in liste_rôle_DL2]
        canal_autorise_id = 1152545720398794752
        if interaction.channel.id != canal_autorise_id:
            await interaction.response.send_message("Vous devez utiliser la commande dans le salon se nommant choix discipline L2. Si vous ne voyez pas ce salon, cela signifie que vous avez déjà choisi votre filière.", ephemeral=True)
            return
        user_roles = interaction.user.roles
        if any(role in user_roles for role in roles):
            await interaction.response.send_message("Vous avez déjà choisi votre filière.", ephemeral=True)
            return
        view = InitDL2(self.bot)
        await interaction.response.send_message("Si vous êtes en double licence :", view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(choix_DL2(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))
