import disnake
from disnake.ext import commands
from disnake import Embed
import requests

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Boosty developer: https://boosty.to/mao-mao")
    print("GitHub: https://github.com/rinnyuwu")
    print("Donation Alerts: https://www.donationalerts.com/r/rinnyuwu")

@bot.slash_command(name="info", description="Get information about a Minecraft server")
async def info(interaction: disnake.AppCmdInter, ip: str):
    url = f"https://api.mcsrvstat.us/3/{ip}"
    response = requests.get(url)
    data = response.json()

    if data["online"]:
        embed = Embed(
            title=f"Information about {ip}",
            color=disnake.Color.blue()
        )

        embed.add_field(name="IP Address", value=f"```{data['ip']}:{data['port']}```", inline=False)
        embed.add_field(name="Description", value=f"```{''.join(data['motd']['clean'])}```", inline=False)
        embed.add_field(name="Core", value=f"```{data['software']}```", inline=True)
        embed.add_field(name="Version", value=f"```{data['version']}```", inline=True)
        embed.add_field(name="Players", value=f"```{data['players']['online']} / {data['players']['max']}```", inline=True)
        await interaction.response.send_message(embed=embed)
    else:
        embed = Embed(
            title=f"Information about {ip}",
            description="The server is offline or doesn't exist.",
            color=disnake.Color.red()
        )

        await interaction.response.send_message(embed=embed)

bot.run("INSERT-TOKEN") # To run the bot, you'll need a token which you get by creating an application in the Discord Developer Portal (https://discord.com/developers/)
                        # Replace INSERT-TOKEN with your token here
                        # Make sure the token remains confidential and is not published in public sources
