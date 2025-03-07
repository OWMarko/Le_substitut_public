import discord
import asyncio
import os
from discord.ext import commands
from discord.utils import get
from discord import Intents, app_commands, guild
from discord.ui import Select, View, Button
from dotenv import load_dotenv

serveur_id = os.getenv("SERVEUR_ID")
liste_rôle_L3 = [992423654778474527,992424043783397416,995809370787020942,995809578589622413,995809902956138618,1278723729811308689,995810241562292304,995811358740328498,995811724743692349,1276608715562287177]

class Com_L3(Button):
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

class Init3(View):
    def __init__(self, roles):
        super().__init__()
        for role in roles:
            self.add_item(Com_L3(role))

class choix_L3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="choix_filière_l3", description="Commande pour choisir votre filière en L3")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def roles(self, interaction: discord.Interaction):
        guild = interaction.guild
        roles = [guild.get_role(role_id) for role_id in liste_rôle_L3]
        canal_autorise_id = 1017437929905324114 
        if interaction.channel.id != canal_autorise_id:
            await interaction.response.send_message("Vous devez utilisé la commande dans le salon se nommant choix discipline L3. Si vous ne voyez pas ce salon, cela signifie que vous avez déjà choisis votre filière.", ephemeral=True)
            return
        user_roles = interaction.user.roles
        if any(role in user_roles for role in roles):
            await interaction.response.send_message("Vous avez déjà choisis votre filière.", ephemeral=True)
            return
        view = Init3(roles)
        await interaction.response.send_message("Choisissez votre filière s'il vous plaît :", view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(choix_L3(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))
