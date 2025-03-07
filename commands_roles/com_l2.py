import asyncio
import discord
import os
from discord.ext import commands
from discord.utils import get
from discord import Intents, app_commands, guild
from discord.ui import Select, View, Button
from dotenv import load_dotenv

serveur_id = os.getenv("SERVEUR_ID")
liste_rôle_L2 = [1152614301182472302,1152614647162220635,1152615099178156073,1152615394402652292,1152615629594034206,1278723608176361582,1152551677325492245,1152615870170943569,1152616036223422578,1152616317501849650,1152616647836831757]

class Com_L2(Button):
    def __init__(self, role):
        super().__init__(label=role.name, style=discord.ButtonStyle.primary)
        self.role = role

    async def callback(self, interaction: discord.Interaction):
        if self.role in interaction.user.roles:
            await interaction.user.remove_roles(self.role)
            await interaction.response.send_message(f"Votre choix a bien été retiré : {self.role.name}.", ephemeral=True)
        else:
            await interaction.user.add_roles(self.role)
            await interaction.response.send_message(f"Votre choix a bien été pris en compte : {self.role.name}.", ephemeral=True)
        await asyncio.sleep(1)
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False
        await interaction.channel.set_permissions(interaction.user, overwrite=overwrite)

class Init2(View):
    def __init__(self, roles):
        super().__init__()
        for role in roles:
            self.add_item(Com_L2(role))

class choix_L2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="choix_filière_l2", description="Commande pour choisir votre filière en L2")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def roles(self, interaction: discord.Interaction):
        guild = interaction.guild
        roles = [guild.get_role(role_id) for role_id in liste_rôle_L2]
        canal_autorise_id = 1152545720398794752 
        if interaction.channel.id != canal_autorise_id:
            await interaction.response.send_message("Vous devez utilisé la commande dans le salon se nommant choix discipline L2. Si vous ne voyez pas ce salon, cela signifie que vous avez déjà choisis votre filière.", ephemeral=True)
            return
        user_roles = interaction.user.roles
        if any(role in user_roles for role in roles):
            await interaction.response.send_message("Vous avez déjà choisis votre filière.", ephemeral=True)
            return
        view = Init2(roles)
        await interaction.response.send_message("Choisissez votre filière s'il vous plaît :", view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(choix_L2(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))


