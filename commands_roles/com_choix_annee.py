import asyncio
import discord
import os
from discord.ext import commands
from discord.utils import get
from discord import Intents, app_commands, guild
from discord.ui import Select, View
from dotenv import load_dotenv

serveur_id = os.getenv("SERVEUR_ID")

class Com_Année_choix(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot

        options = [
            discord.SelectOption(label="L1", description="Première année de licence", emoji="🔵"),
            discord.SelectOption(label="L2", description="Deuxième année de licence", emoji="🟢"),
            discord.SelectOption(label="L3", description="Troisième année de licence", emoji="🔴"), 
            discord.SelectOption(label="Ancien.ne", description="Ancien.ne membre du serveur", emoji="🟡"),
        ]
        super().__init__(placeholder="Choisissez votre année...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        role_name = self.values[0]
        role = discord.utils.get(interaction.guild.roles, name=role_name)
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Rôle {role.name} retiré.", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Rôle {role.name} ajouté.", ephemeral=True)
        await asyncio.sleep(2)
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False
        await interaction.channel.set_permissions(interaction.user, overwrite=overwrite)
        await interaction.response.send_message(f"Votre rôle a bien été sélectionné" ,ephemeral=True)   

class Init(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.add_item(Com_Année_choix(bot))

class Comm_choix_année(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="choix_année", description="Choisissez votre année")
    @app_commands.guilds(discord.Object(id=serveur_id))
    @app_commands.checks.has_permissions(administrator=True)
    async def roles(self, interaction: discord.Interaction):
        await interaction.response.send_message("Choisissez votre année :", view=Init(self.bot))

async def setup(bot):
    await bot.add_cog(Comm_choix_année(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))