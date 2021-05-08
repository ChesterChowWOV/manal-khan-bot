
from keep_alive import keep_alive
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="ChesterWOV#2768"))
        
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$rules'):
		await message.channel.send('<#815504635468447794>')
		
	if message.content.startswith('$custom-invite'):
		await message.channel.send('https://dsc.gg/manal-khan')

	if message.content.startswith('Fk'):
		await message.channel.send('Hmm, is that the short form of fuc*?')
		
	if message.content.startswith('fk'):
	  await message.channel.send('Hmm, is that the short form of fuc*?')
	 
	if message.content.startswith('$credits'):
	  await message.channel.send('Developer: ChesterWOV#2768; On repl.it')
	if message.content.startswith('$help'):
	  await message.channel.send('https://discord.com/channels/815504104561311744/839846055465844786/840163478358589456')
	if message.content.startswith('&:£')
	for x in range(3):
	  await message.channel.send('HEY @everyone MAKE THE SERVER ALIVE')
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(os.getenv('TOKEN'))
