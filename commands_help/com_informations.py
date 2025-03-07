import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
serveur_id = os.getenv("SERVEUR_ID")

class Com_Informations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    class RoleSelect(discord.ui.Select):
        def __init__(self):
            options = [
                discord.SelectOption(
                    label="Scolarité", 
                    description = "Informations sur la scolarité.",
                    emoji="🏰"
                    ),
                discord.SelectOption(
                    label="CRL",
                    description="Centre Ressource Linguistique",
                    emoji="🌐"
                    ),
                discord.SelectOption(
                    label="Centre de santé universitaire",
                    description="Spécialiste, psy, gynécologie, conduites addictives...",
                    emoji="🆘"
                    ),
                discord.SelectOption(
                    label="Aide Sociale",
                    description="Aide financière, juridique...",
                    emoji="⛑️"
                    ),
            ]
            super().__init__(placeholder="Je vous écoute.", min_values=1, max_values=1, options=options)

        async def callback(self, interaction: discord.Interaction):
            if self.values[0] == "Scolarité":
                embed = discord.Embed(
                    title="Scolarité",
                    description="Numéro de téléphone : +33 4 89 15 00\n\n"
                                "Horaires : Du lundi au vendredi → 8h à 12h - 13h à 16h\n\n"
                                "Localisation 26/08-16/09 : Hall PV\n\n"
                                "Localisation 16/09-04/07 : Petit-château\n\n"
                                "Mail Portail SV L1/L2 : Samira.LAMKHANTAR@univ-cotedazur.fr ou Mélissa.BOURGEOIS@univ-cotedazur.fr\n\n"
                                "Mail Portail SV L3 : Sophie.ROBINI@univ-cotedazur.fr\n\n"
                                "Mail Portail S&T L1/L2 : Marine.GAMET@univ-cotedazur.fr ou Myriam.PORCU@univ-cotedazur.fr\n\n"
                                "Mail Portail S&T L3 : Marion.OLIVIER@univ-cotedazur.fr\n\n"
                                "Pour plus d'informations : https://univ-cotedazur.fr/portails/portail-sciences-de-la-vie/contacts",
                    color=discord.Color.purple()
                )

            elif self.values[0] == "CRL":
                embed = discord.Embed(
                    title="Centres de Ressources en Langues",
                    description="Les CRL servent à faciliter l’apprentissage d’une langue. Chaque campus (Valrose, SJA, Carlone…) possède son propre CRL, mais vous pouvez aussi accéder à ceux des autres campus. Les CRL vous proposent de nombreuses ressources pour l’apprentissage de nombreuses langues comme l’anglais, l’arabe, l’espagnol, l’italien, et bien plus encore."
                                "C’est dans ces lieux que les étudiants de L1 doivent faire les 10 heures d’anglais obligatoires par semestre.\n\n"
                                "Vous pouvez consulter les différents horaires et informations sur les CRL des campus sur : https://univ-cotedazur.fr/formation/reussir-ses-etudes/scl/crl/les-crl-par-campus.",
                    color=discord.Color.blue()
                )

            elif self.values[0] == "Centre de santé universitaire":
                embed = discord.Embed(
                    title="Centre de santé",
                    description="Le Centre de santé universitaire de l’Université de Nice se situe à SJA (campus Éco-Gestion). Vous pouvez prendre rendez-vous avec un médecin généraliste (ils peuvent aussi être vos médecins référents à la CPAM), un gynécologue, un infirmier, ou des spécialistes dans le domaine de la psychologie ou des addictions.\n\n"
                                 "Pour plus d'information : https://univ-cotedazur.fr/vie-des-campus/sante-aide-sociale\n\n Pour prendre rendez-vous : https://www.doctolib.fr/centre-de-sante/nice/centres-de-sante-universitaire-csu-cote-d-azur/booking/specialities?profile_skipped=true&bookingFunnelSource=external_referral.",
                    color=discord.Color.green()
                )

            elif self.values[0] == "Aide Sociale":
                embed = discord.Embed(
                    title="Aide financière / Aide Juridique / Aide sociale",
                    description="L’Université Côte d’Azur met à disposition plusieurs équipes pour vous aider dans vos démarches financières, juridiques et autres.\n\n"
                                 "Pour prendre rendez-vous pour une aide financière : https://univ-cotedazur.fr/vie-des-campus/sante-aide-sociale/aides-sociales/aide-financiere\n\n"
                                 "Pour prendre rendez-vous pour une aide juridique : https://univ-cotedazur.fr/vie-des-campus/sante-aide-sociale/aides-sociales/acces-aux-droits\n\n"
                                 "Pour prendre rendez-vous avec une assistante sociale : https://univ-cotedazur.fr/apercu/294754/?EXT=core.",
                    color=discord.Color.red()
                )

            await interaction.response.send_message(embed = embed, ephemeral=True)

    class RoleSelectView(discord.ui.View):
        def __init__(self):
            super().__init__()
            self.add_item(Com_Informations.RoleSelect())

    @app_commands.command(name="informations_services", description="Des questions sur la scolarité ? Le centre de santé ? Ou bien sur le CRL ?")
    @app_commands.guilds(discord.Object(id=serveur_id))
    async def informations_services(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=Com_Informations.RoleSelectView(), ephemeral= True)

async def setup(bot):
    await bot.add_cog(Com_Informations(bot))
    await bot.tree.sync(guild=discord.Object(id=serveur_id))
