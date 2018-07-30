import discord
from discord.ext.commands import Bot
import asyncio
from random import randint
import urllib.request as request
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup


BOT_PREFIX = ("!")
TOKEN = "token"

client = Bot(command_prefix = BOT_PREFIX)

@client.command(description = "Returns the square of an input number")
async def square(num):
	squared_num = int(num) * int(num)
	await client.say(str(num) + " squared is " + str(squared_num))
	

@client.command(description = "Returns a number from 1-6 at random simulating a die roll")
async def roll():
	await client.say(randint(1,6))

@client.command(description = "Returns weather for an input zip code")
async def weather(zip_code):
	key = "ff14f8db605bb62b"
	fileName = "http://api.wunderground.com/api/" + key +    "/geolookup/conditions/q/PA/" + zip_code + ".json"
	f = request.urlopen(fileName)
	json_string = f.read().decode('utf-8')
	parsed_json = json.loads(json_string)
	location = parsed_json['location']['city']
	temp_f = parsed_json['current_observation']['temp_f']
	weather = parsed_json['current_observation']['weather']
	await client.say("Current temperature in {} is: {}F with {} conditions".format(location, temp_f, weather))

@client.command(description = "Retrieves the point value of major U.S. stock indices")
async def markets():
	quotesp, quotedj, quoten = "https://www.bloomberg.com/quote/SPX:IND", "https://www.bloomberg.com/quote/INDU:IND", "https://www.bloomberg.com/quote/CCMP:IND"


	pagesp, pagedj, pagen = urlopen(quotesp), urlopen(quotedj), urlopen(quoten)

	soupsp, soupdj, soupn = BeautifulSoup(pagesp, "html.parser"), BeautifulSoup(pagedj, "html.parser"), BeautifulSoup(pagen, "html.parser")

	pricesp = soupsp.find("div", attrs={"class": "price"})
	price1 = pricesp.text

	pricedj = soupdj.find("div", attrs={"class": "price"})
	price2 = pricedj.text

	pricen = soupn.find("div", attrs={"class": "price"})
	price3 = pricen.text
	

	await client.say("S&P500: {}".format(price1))	
	await client.say("Dow Jones: {}".format(price2))
	await client.say("Nasdaq: {}".format(price3))


@client.event
async def on_ready():
	print("Logged in as " + client.user.name)


client.run(TOKEN)
