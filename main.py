import discord
import os
from dotenv import load_dotenv, find_dotenv

# BASEDIR = os.path.abspath(os.path.dirname('StarbitBot'))
# load_dotenv(os.path.join(BASEDIR, '.env'))
load_dotenv(find_dotenv())

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')
M_ID = os.getenv('M_ID')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# REACTION ROLES
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == int(M_ID):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '♀️':
            role = discord.utils.get(guild.roles, name='She/Her')
            # print("She/Her Role")
        elif payload.emoji.name == '♂️':
            role = discord.utils.get(guild.roles, name='He/Him')
        elif payload.emoji.name == '⚧':
            role = discord.utils.get(guild.roles, name='They/Them')
        elif payload.emoji.name == '🎥':
            role = discord.utils.get(guild.roles, name='movies')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.add_roles(role)
                print("Done.")
            else: 
                print("Member not found.")
        else:
            print("Role not found.")
    else:
        print(message_id)
        print(M_ID)

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == M_ID:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == '♀️':
            role = discord.utils.get(guild.roles, name='She/Her')
        elif payload.emoji.name == '♂️':
            role = discord.utils.get(guild.roles, name='He/Him')
        elif payload.emoji.name == '⚧':
            role = discord.utils.get(guild.roles, name='They/Them')
        elif payload.emoji.name == '🎥':
            role = discord.utils.get(guild.roles, name='movies')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                # the only change lmao
                await member.remove_roles(role)
                print("Done.")
            else: 
                print("Member not found.")
        else:
            print("Role not found.")

# COMMANDS
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# print(TOKEN)
# print(M_ID)
client.run(TOKEN)
