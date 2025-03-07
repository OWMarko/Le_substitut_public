import discord
import os
from discord.ext import commands
from discord.utils import get
from discord import Intents, app_commands, guild
from dotenv import load_dotenv

serveur_id = os.getenv("SERVEUR_ID")

class Com_modo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='ton_id', description='Obtient ton ID d\'utilisateur')
    @app_commands.guilds(discord.Object(id=serveur_id))
    @app_commands.checks.has_permissions(administrator=True)
    async def userid(self, interaction: discord.Interaction):
        author_id = interaction.user.id
        await interaction.response.send_message(f'Ton ID est : {author_id}')

    @app_commands.command(name='interdit_salon', description='Interdire un rôle d\'accéder à un salon')
    @app_commands.guilds(discord.Object(id=serveur_id))
    @app_commands.checks.has_permissions(administrator=True)
    async def prohibit(self, interaction: discord.Interaction, channel: discord.TextChannel, role: discord.Role):
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False
        await channel.set_permissions(role, overwrite=overwrite)
        await interaction.response.send_message(f"Le rôle {role.name} a été interdit d'accéder à {channel.name}")

    @app_commands.command(name='son_id', description='Obtenir l\'ID d\'un utilisateur')
    @app_commands.guilds(discord.Object(id=serveur_id))
    @app_commands.checks.has_permissions(administrator=True)
    async def get_id(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"L'ID de {member.name} est {member.id}")

    @app_commands.command(name='retirer_rôle', description='retirer un rôle')
    @app_commands.guilds(discord.Object(id=serveur_id))
    @app_commands.checks.has_permissions(administrator=True)
    async def retirer_role(self,interaction : discord.Interaction, utilisateur : discord.Member, role : discord.Role) :
        print("Commande retirer_role appelée")
        try:
            await utilisateur.remove_roles(role)
            await interaction.response.send_message(f'Le rôle {role.name} a été retiré de {utilisateur.name}')
        except Exception as problemes_retirer_rôle:
            print(f"Erreur lors du retrait du rôle : {problemes_retirer_rôle}")
            await interaction.response.send_message(f"Erreur : {problemes_retirer_rôle}")
        
    @app_commands.command(name='ajouter_rôle', description='ajouter un rôle')
    @app_commands.guilds(discord.Object(id = serveur_id))
    @app_commands.checks.has_permissions(administrator = True)
    async def ajouter_role(self,interaction : discord.Interaction, user : discord.Member, role : discord.Role) :
        print("Commande ajouter_role appelée")
        try :
            await user.add_roles(role)
            await interaction.response.send_message(f'Le rôle {role.name} a été ajouté à {user.name}')
        except Exception as problemes_ajouter_role:
            print(f'Erreur lors du ajout du rôle: {problemes_ajouter_role}')

async def setup(bot):
    await bot.add_cog(Com_modo(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))