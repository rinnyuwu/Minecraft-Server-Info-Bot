# Minecraft Server Info Bot

This Discord bot provides users with detailed information about a Minecraft server. By using a simple slash command, users can fetch live data such as the server's status, version, number of players, and more.

## Features
- Server Status: Get live information about a Minecraft server.
- Server Information: Displays details like IP address, version, core, and players.
- Offline Handling: If the server is offline, the bot will notify the user that the server is unavailable.

![msedge_MTRRTItie4](https://github.com/user-attachments/assets/ec62b74f-a182-4650-b82e-5dc9ee38a53a)

## Requirements
- Programming Language: Python
- Required Libraries: disnake (for interacting with Discord's API), requests (for fetching Minecraft server data)
Install the required libraries using pip:
```
pip3 install disnake requests
```

## Setup
1. Create a bot on Discord:
- Go to the [Discord Developer Portal](https://discord.com/developers/applications).
- Create a new application, then a bot, and obtain the bot token.
- Replace the placeholder `INSERT-TOKEN` in the code with your bot token.
2. Install Dependencies:
- On your machine, make sure Python 3.8+ is installed. You can check this by running:
```
python --version
```
- Install pip if it’s not installed:
```
sudo apt install python3-pip
```
- Install the required libraries with pip:
```
pip3 install disnake requests
```

## Run the bot:
- You can run the bot using the following command:
```
python3 app.py
```
Make sure you are in the same directory where the app.py file is located or provide the full path to it.

## How to Use
- Deploy: Clone the repository and configure your bot.
- Run: Launch the bot on your server.
- Interaction: Use the slash command `/info <server-ip>` to get detailed information about a Minecraft server.

## Links
[Boosty developer](https://boosty.to/mao-mao)

[GitHub](https://github.com/rinnyuwu)

[Donation Alerts](https://www.donationalerts.com/r/rinnyuwu)
