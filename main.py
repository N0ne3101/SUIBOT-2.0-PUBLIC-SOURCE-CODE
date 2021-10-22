import discord
import os
from discord.ext import commands
from discord.ext.commands.core import command


chungChannel = 764510929500373023


client = commands.Bot(command_prefix='s+')
client.remove_command('help')


@client.event
async def on_ready():
    print('Running')

for filename in os.listdir('./Moderator'):
    if filename.endswith('.py'):
        client.load_extension(f'Moderator.{filename[:-3]}')

for filename in os.listdir('./AIchat'):
    if filename.endswith('.py'):
        client.load_extension(f'AIchat.{filename[:-3]}')

# for filename in os.listdir('./Hentai'):
#     if filename.endswith('.py'):
#         client.load_extension(f'Hentai.{filename[:-3]}')

for filename in os.listdir('./Music'):
    if filename.endswith('.py'):
        client.load_extension(f'Music.{filename[:-3]}')

# for filename in os.listdir('./DevZone'):
#     if filename.endswith('.py'):
#         client.load_extension(f'DevZone.{filename[:-3]}')


client.run("token")