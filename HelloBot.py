import discord
import time


client = discord.Client()

@client.event
async def on_message(message):
	# stops self replies
	if message.author == client.user:
		return


	if message.content.upper().startswith('!HELLO'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)



@client.event
async def on_ready():
	print('Logged in as')
	print('Name: {}'.format(client.user.name))
	print('ID: {}'.format(client.user.id))
	print('at {}'.format(time.strftime('%c')))
	print('------')

client.run('token')

