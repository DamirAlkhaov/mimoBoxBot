import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  activity = discord.Game(name="Listening for mb!help")
  await client.change_presence(status=discord.Status.idle, activity=activity)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('mb!info'):
    user = 'This is MimoBox Bot! Running on as ' + str(client.user)
    await message.channel.send(user)

  if message.content.startswith('mb!help'):
    await message.channel.send('**MimoBox Bot Help Menu**'
    '```'
    'mb!info - gives the info about a bot'
    'mb!verify - verifies player'
    'mb!user {username} - gives info about a user'
    '```')

client.run(os.getenv('TOKEN'))