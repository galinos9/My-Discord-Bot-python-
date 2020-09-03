import discord
from discord.ext import commands
import random
import os
import time
from datetime import datetime, timedelta


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	print('Bot is Ready')
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="type help"))

@client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in Client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await Client.delete_messages(mgs)

@client.event
async def on_message(message):
	if str(message.channel) == "test" and message.content != "":
		await message.channel.purge(limit=1)
	if message.author == client.user:
		return
	if message.content.startswith("!dice"):
		min = 1
		max = 6
		await message.channel.send(random.randint(min, max))
	if message.content.startswith("!coin"):
		min = 1
		max = 2
		results = random.randint(min, max)
		if results == 1:
			await message.channel.send("Korwna")
		else:
			await message.channel.send("Gramma")
	if message.content.startswith("!poutsa"):
		min = 0
		max = 30
		results = random.randint(min, max)
		await message.channel.send("Τον εχω " + str(results) + " εκ.")
	if message.content.startswith("!kota"):
		await message.channel.send("katholou kota")
	if message.content.startswith("!bigbrother"):
		await message.channel.send("https://www.skaitv.gr/show/psuchagogia/big-brother/sezon-2020-2021")
	if message.content.startswith("help"):
		await message.channel.send("!dice  !coin  !poutsa  !kota  !gay  !game  !bigbrother  ")
	if message.content.startswith("!gay"):
		min = 0
		max = 100
		results = random.randint(min, max)
		await message.channel.send("Ειμαι " + str(results) + "% πουστρα.")
	if message.content.startswith("!gaming"):
		three_hours_from_now = (datetime.now() + timedelta(hours=3)).strftime('%H:%M:%S')
		await message.channel.send("Θα παιξεις μεχρι " + three_hours_from_now + ".")
	if message.content.startswith("!game"):
		min = 1
		max = 3
		results = random.randint(min, max)
		if results == 1:
			await message.channel.send("LOL")
		elif results == 2:
			await message.channel.send("LITE")
		else:
			await message.channel.send("RL")
			




client.run(os.environ['DISCORD_TOKEN'])