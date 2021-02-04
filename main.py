import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  activity = discord.Game(name="Listening for mb!help")
  await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('mb!info'):
    user = 'This is MimoBox Bot! Thank you for asking @' + str(message.author)
    await message.channel.send(user)

  if message.content.startswith('mb!help'):
    await message.channel.send('**MimoBox Bot Help Menu**'
    '```'
    'mb!info - gives the info about a bot'
    'mb!love - gives you lots of love!'
    
    '```')
  if message.content.startswith('mb!love'):
    user = 'I love you alot @' + str(message.author) + '!'
    await message.channel.send(user)

client.run(os.getenv('TOKEN'))
