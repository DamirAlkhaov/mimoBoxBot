import discord
import os
import requests
import json
from datetime import datetime
from ping import ping

client = discord.Client()

def get_UserInfo(id, user):
  url = os.getenv('GetUserById') + id
  response = requests.get(url)
  json_Data = json.loads(response.text)
  if 'username' in json_Data:
    join_date = json_Data['created']
    join_date_short = join_date[:10]
    infoGet = 'Username: ' + json_Data['username'] + '\n Join Date: ' + join_date_short
    embed = discord.Embed(title = json_Data['username'], description = infoGet, color = discord.Colour.green())
    embed.set_footer(text = 'Request by: ' + user.name + ' | ' + str(datetime.now()), icon_url = user.avatar_url)
    return(embed)
  else:
    infoGet = 'Error '+ json_Data['status'] +' : ' + json_Data['message']
    embed = discord.Embed(title = "Error "+ json_Data['status'], description = json_Data['message'], color = discord.Colour.red())
    return(embed)
  

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
    embed = discord.Embed(title = 'Commands', color = discord.Colour.red())
    embed.add_field(name="User Commands:", value="**mb!info (id)**: Gives info about a MimoBox User.")
    await message.channel.send(embed=embed)
  
  if message.content.startswith('mb!info'):
    chosen_id = message.content.split('mb!info ',1)[1]
    gotten_info = get_UserInfo(chosen_id, message.author)
    if gotten_info:
      await message.channel.send(embed=gotten_info)
    else:
      await message.channel.send("Error : ID doesn't exist")
  
ping()
client.run(os.getenv('TOKEN'))
