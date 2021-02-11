import discord
import os
import requests
import json

client = discord.Client()

def get_UserInfo(id):
  url = os.getenv('GetUserById') + id
  response = requests.get(url)
  json_Data = json.loads(response.text)
  if 'username' in json_Data:
    join_date = json_Data['created']
    join_date_short = join_date[:10]
    infoGet = 'Username: ' + json_Data['username'] + ', Join Date: ' + join_date_short
    return(infoGet)
  else:
    infoGet = 'Error '+ json_Data['status'] +' : ' + json_Data['message']
    return(infoGet)
  

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  activity = discord.Activity(type=discord.ActivityType.watching, name='for mb!help')
  await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  

  if message.content.startswith('mb!help'):
    await message.channel.send('**MimoBox Bot Help Menu**'
    '```'
    'mb!info - gives the info about a bot'
    'mb!love - gives you lots of love!'
    
    '```')
  
  if message.content.startswith('mb!info'):
    chosen_id = message.content.split('mb!info ',1)[1]
    gotten_info = get_UserInfo(chosen_id)
    if gotten_info:
      await message.channel.send(gotten_info)
    else:
      await message.channel.send("Error : ID doesn't exist")
  

client.run(os.getenv('TOKEN'))
