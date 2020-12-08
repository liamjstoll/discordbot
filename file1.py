import os
import random
import discord
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import praw
from praw.models import MoreComments
import openpyxl
from datetime import date
from yahoo_fin import stock_info as si

msft=si.get_live_price("msft")
aapl = si.get_live_price("aapl")
spy = si.get_live_price("spy")
tsla=si.get_live_price("tsla")
nkla=si.get_live_price("nkla")
amd=si.get_live_price("amd")
nvda=si.get_live_price("nvda")
pton=si.get_live_price("pton")
fb=si.get_live_price("fb")
bynd=si.get_live_price("bynd")

reddit = praw.Reddit(client_id = 'uIt4LCqPKaTdZw',client_secret = 'uFiS_dnsaLgCC1zSk09Xt6V3w4c',username = 'maniaclunatic',password='@Stoll1126',user_agent='liam')

wsb = reddit.subreddit('wallstreetbets')
robinhood = reddit.subreddit('robinhood')
options = reddit.subreddit('options')


robinhoodHot = robinhood.hot(limit=5)
robinhoodTop = robinhood.top(time_filter = "day", limit=2)
wsbHot = wsb.hot(limit=5)
wsbTop = wsb.top(time_filter = "day", limit=2)
optionsHot = options.hot(limit=10)
optionsTop = options.top(time_filter = "day", limit=4)

spy_count = 0
tesla_count = 0
nikola_count = 0
apple_count = 0
amd_count=0
nvidia_count=0
peloton_count=0
elon_count = 0
jpow_count = 0
tendies_count = 0
moon_count = 0
algo_count = 0
facebook_count = 0
microsoft_count=0
beyond_meat_count = 0
palantir_count = 0
boomer_count = 0




for submission in wsbHot:

	if not submission.stickied:
		print(submission.title)
		print(submission.ups)
		
		comments=submission.comments.list()
		for top_level_comment in submission.comments:
			if isinstance(top_level_comment, MoreComments):
				continue
			if 'Algo' not in top_level_comment.body and 'algo' not in top_level_comment.body:
                
                if 'BOOMER' in top_level_comment.body or 'boomer' in top_level_comment.body:
				    boomer_count +=1
                if 'PLTR' in top_level_comment.body or 'Palantir' in top_level_comment.body:
					palantir_count +=1
				if 'SPY' in top_level_comment.body or 'spy' in top_level_comment.body:
					spy_count +=1
				if 'Tesla' in top_level_comment.body or 'TSLA' in top_level_comment.body:
					tesla_count +=1
				if 'Nikola' in top_level_comment.body or 'NKLA' in top_level_comment.body:
					nikola_count +=1
				if 'Apple' in top_level_comment.body or 'AAPL' in top_level_comment.body:
					apple_count +=1
				if 'Elon' in top_level_comment.body or 'elon' in top_level_comment.body:
					elon_count +=1
				if 'j pow' in top_level_comment.body or 'J Pow' in top_level_comment.body:
					jpow_count +=1
				if 'tendies' in top_level_comment.body or 'Tendies' in top_level_comment.body:
					tendies_count +=1
				if 'AMD' in top_level_comment.body or 'amd' in top_level_comment.body:
					amd_count +=1
				if 'Nvidia' in top_level_comment.body or 'NVDA' in top_level_comment.body:
					nvidia_count +=1
				if 'peloton' in top_level_comment.body or 'PTON' in top_level_comment.body:
					peloton_count +=1
				if 'FB' in top_level_comment.body or 'Facebook' in top_level_comment.body:
					facebook_count +=1
				if 'MSFT' in top_level_comment.body or 'Microsoft' in top_level_comment.body:
					microsoft_count +=1
				if 'BYND' in top_level_comment.body or 'beyond meat' in top_level_comment.body:
					beyond_meat_count +=1

for submission in optionsHot:

	if not submission.stickied:
		print(submission.title)
		print(submission.ups)
		
		comments=submission.comments.list()
		for top_level_comment in submission.comments:
			if isinstance(top_level_comment, MoreComments):
				continue
			if 'Algo' not in top_level_comment.body and 'algo' not in top_level_comment.body:
				if 'citron' in top_level_comment.body or 'CITRON' in top_level_comment.body:
					palantir_count +=1
                if 'BOOMER' in top_level_comment.body or 'boomer' in top_level_comment.body:
					boomer_count +=1
                if 'PLTR' in top_level_comment.body or 'Palantir' in top_level_comment.body:
					palantir_count +=1
                if 'SPY' in top_level_comment.body or 'spy' in top_level_comment.body:
					spy_count +=1
				if 'Tesla' in top_level_comment.body or 'TSLA' in top_level_comment.body:
					tesla_count +=1
				if 'Nikola' in top_level_comment.body or 'NKLA' in top_level_comment.body:
					nikola_count +=1
				if 'Apple' in top_level_comment.body or 'AAPL' in top_level_comment.body:
					apple_count +=1
				if 'Elon' in top_level_comment.body or 'elon' in top_level_comment.body:
					elon_count +=1
				if 'j pow' in top_level_comment.body or 'J Pow' in top_level_comment.body:
					jpow_count +=1
				if 'tendies' in top_level_comment.body or 'Tendies' in top_level_comment.body:
					tendies_count +=1
				if 'AMD' in top_level_comment.body or 'amd' in top_level_comment.body:
					amd_count +=1
				if 'Nvidia' in top_level_comment.body or 'NVDA' in top_level_comment.body:
					nvidia_count +=1
				if 'peloton' in top_level_comment.body or 'PTON' in top_level_comment.body:
					peloton_count +=1
				if 'FB' in top_level_comment.body or 'Facebook' in top_level_comment.body:
					facebook_count +=1
				if 'MSFT' in top_level_comment.body or 'Microsoft' in top_level_comment.body:
					microsoft_count +=1
				if 'BYND' in top_level_comment.body or 'beyond meat' in top_level_comment.body:
					beyond_meat_count +=1

for submission in robinhoodHot:

	if not submission.stickied:
		print(submission.title)
		print(submission.ups)
		
		comments=submission.comments.list()
		for top_level_comment in submission.comments:
			if isinstance(top_level_comment, MoreComments):
				continue
			if 'Algo' not in top_level_comment.body and 'algo' not in top_level_comment.body:
				if 'citron' in top_level_comment.body or 'CITRON' in top_level_comment.body:
					palantir_count +=1
                if 'BOOMER' in top_level_comment.body or 'boomer' in top_level_comment.body:
					boomer_count +=1
                if 'PLTR' in top_level_comment.body or 'Palantir' in top_level_comment.body:
					palantir_count +=1
                if 'SPY' in top_level_comment.body or 'spy' in top_level_comment.body:
					spy_count +=1
				if 'Tesla' in top_level_comment.body or 'TSLA' in top_level_comment.body:
					tesla_count +=1
				if 'Nikola' in top_level_comment.body or 'NKLA' in top_level_comment.body:
					nikola_count +=1
				if 'Apple' in top_level_comment.body or 'AAPL' in top_level_comment.body:
					apple_count +=1
				if 'Elon' in top_level_comment.body or 'elon' in top_level_comment.body:
					elon_count +=1
				if 'j pow' in top_level_comment.body or 'J Pow' in top_level_comment.body:
					jpow_count +=1
				if 'tendies' in top_level_comment.body or 'Tendies' in top_level_comment.body:
					tendies_count +=1
				if 'AMD' in top_level_comment.body or 'amd' in top_level_comment.body:
					amd_count +=1
				if 'Nvidia' in top_level_comment.body or 'NVDA' in top_level_comment.body:
					nvidia_count +=1
				if 'peloton' in top_level_comment.body or 'PTON' in top_level_comment.body:
					peloton_count +=1
				if 'FB' in top_level_comment.body or 'Facebook' in top_level_comment.body:
					facebook_count +=1
				if 'MSFT' in top_level_comment.body or 'Microsoft' in top_level_comment.body:
					microsoft_count +=1
				if 'BYND' in top_level_comment.body or 'beyond meat' in top_level_comment.body:
					beyond_meat_count +=1



for submission in wsbTop:

	if not submission.stickied:
		print(submission.title)
		print(submission.ups)
		
		comments=submission.comments.list()
		for top_level_comment in submission.comments:
			if isinstance(top_level_comment, MoreComments):
				continue
			if 'Algo' not in top_level_comment.body and 'algo' not in top_level_comment.body:
				if 'citron' in top_level_comment.body or 'CITRON' in top_level_comment.body:
					palantir_count +=1
                if 'BOOMER' in top_level_comment.body or 'boomer' in top_level_comment.body:
					boomer_count +=1
                if 'PLTR' in top_level_comment.body or 'Palantir' in top_level_comment.body:
					palantir_count +=1
                if 'SPY' in top_level_comment.body or 'spy' in top_level_comment.body:
					spy_count +=1
				if 'Tesla' in top_level_comment.body or 'TSLA' in top_level_comment.body:
					tesla_count +=1
				if 'Nikola' in top_level_comment.body or 'NKLA' in top_level_comment.body:
					nikola_count +=1
				if 'Apple' in top_level_comment.body or 'AAPL' in top_level_comment.body:
					apple_count +=1
				if 'Elon' in top_level_comment.body or 'elon' in top_level_comment.body:
					elon_count +=1
				if 'j pow' in top_level_comment.body or 'J Pow' in top_level_comment.body:
					jpow_count +=1
				if 'tendies' in top_level_comment.body or 'Tendies' in top_level_comment.body:
					tendies_count +=1
				if 'AMD' in top_level_comment.body or 'amd' in top_level_comment.body:
					amd_count +=1
				if 'Nvidia' in top_level_comment.body or 'NVDA' in top_level_comment.body:
					nvidia_count +=1
				if 'peloton' in top_level_comment.body or 'PTON' in top_level_comment.body:
					peloton_count +=1
				if 'FB' in top_level_comment.body or 'Facebook' in top_level_comment.body:
					facebook_count +=1
				if 'MSFT' in top_level_comment.body or 'Microsoft' in top_level_comment.body:
					microsoft_count +=1
				if 'BYND' in top_level_comment.body or 'beyond meat' in top_level_comment.body:
					beyond_meat_count +=1

for submission in robinhoodTop:

	if not submission.stickied:
		print(submission.title)
		print(submission.ups)
		
		comments=submission.comments.list()
		for top_level_comment in submission.comments:
			if isinstance(top_level_comment, MoreComments):
				continue
			if 'Algo' not in top_level_comment.body and 'algo' not in top_level_comment.body:
				if 'citron' in top_level_comment.body or 'CITRON' in top_level_comment.body:
					palantir_count +=1
                if 'BOOMER' in top_level_comment.body or 'boomer' in top_level_comment.body:
					boomer_count +=1
                if 'PLTR' in top_level_comment.body or 'Palantir' in top_level_comment.body:
					palantir_count +=1
                if 'SPY' in top_level_comment.body or 'spy' in top_level_comment.body:
					spy_count +=1
				if 'Tesla' in top_level_comment.body or 'TSLA' in top_level_comment.body:
					tesla_count +=1
				if 'Nikola' in top_level_comment.body or 'NKLA' in top_level_comment.body:
					nikola_count +=1
				if 'Apple' in top_level_comment.body or 'AAPL' in top_level_comment.body:
					apple_count +=1
				if 'Elon' in top_level_comment.body or 'elon' in top_level_comment.body:
					elon_count +=1
				if 'j pow' in top_level_comment.body or 'J Pow' in top_level_comment.body:
					jpow_count +=1
				if 'tendies' in top_level_comment.body or 'Tendies' in top_level_comment.body:
					tendies_count +=1
				if 'AMD' in top_level_comment.body or 'amd' in top_level_comment.body:
					amd_count +=1
				if 'Nvidia' in top_level_comment.body or 'NVDA' in top_level_comment.body:
					nvidia_count +=1
				if 'peloton' in top_level_comment.body or 'PTON' in top_level_comment.body:
					peloton_count +=1
				if 'FB' in top_level_comment.body or 'Facebook' in top_level_comment.body:
					facebook_count +=1
				if 'MSFT' in top_level_comment.body or 'Microsoft' in top_level_comment.body:
					microsoft_count +=1
				if 'BYND' in top_level_comment.body or 'beyond meat' in top_level_comment.body:
					beyond_meat_count +=1

for submission in optionsTop:

	if not submission.stickied:
		print(submission.title)
		print(submission.ups)
		
		comments=submission.comments.list()
		for top_level_comment in submission.comments:
			if isinstance(top_level_comment, MoreComments):
				continue
			if 'Algo' not in top_level_comment.body and 'algo' not in top_level_comment.body:
				if 'citron' in top_level_comment.body or 'CITRON' in top_level_comment.body:
					palantir_count +=1
                if 'BOOMER' in top_level_comment.body or 'boomer' in top_level_comment.body:
					boomer_count +=1
                if 'PLTR' in top_level_comment.body or 'Palantir' in top_level_comment.body:
					palantir_count +=1
                if 'SPY' in top_level_comment.body or 'spy' in top_level_comment.body:
					spy_count +=1
				if 'Tesla' in top_level_comment.body or 'TSLA' in top_level_comment.body:
					tesla_count +=1
				if 'Nikola' in top_level_comment.body or 'NKLA' in top_level_comment.body:
					nikola_count +=1
				if 'Apple' in top_level_comment.body or 'AAPL' in top_level_comment.body:
					apple_count +=1
				if 'Elon' in top_level_comment.body or 'elon' in top_level_comment.body:
					elon_count +=1
				if 'j pow' in top_level_comment.body or 'J Pow' in top_level_comment.body:
					jpow_count +=1
				if 'tendies' in top_level_comment.body or 'Tendies' in top_level_comment.body:
					tendies_count +=1
				if 'AMD' in top_level_comment.body or 'amd' in top_level_comment.body:
					amd_count +=1
				if 'Nvidia' in top_level_comment.body or 'NVDA' in top_level_comment.body:
					nvidia_count +=1
				if 'peloton' in top_level_comment.body or 'PTON' in top_level_comment.body:
					peloton_count +=1
				if 'FB' in top_level_comment.body or 'Facebook' in top_level_comment.body:
					facebook_count +=1
				if 'MSFT' in top_level_comment.body or 'Microsoft' in top_level_comment.body:
					microsoft_count +=1
				if 'BYND' in top_level_comment.body or 'beyond meat' in top_level_comment.body:
					beyond_meat_count +=1
"""
print("SPY: ", spy_count)
print('Tesla: ',tesla_count)
print('Nikola:',nikola_count)
print('Apple:',apple_count)
print('Facebook:',facebook_count)
print('Elon:', elon_count)
print('jpow:', jpow_count)
print('tendies:', tendies_count)
print('moon:', moon_count)
print('nvidia:', nvidia_count)
print('amd:', amd_count)
print('peloton:', peloton_count)
"""
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'connected.')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, pick from supported commands...'
    )
    await member.dm_channel.send( f'Available Commands:\n-hype\n-stonks')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    list_of_quotes = [
        'Stonks only go up.',
        'Money printer go brrrrr.',
        'Boomer stonks are dead.',
        'Fundamentals dont matter. Invest in memes.'
    ]

    if message.content == 'hype':
        response = random.choice(list_of_quotes)
        await message.channel.send(response)
        await message.channel.send(f'--------------------------------')
        await message.channel.send(f'Boomer mentions: {boomer_count}')
        await message.channel.send(f'Boomer mentions within retail investing subs should correlate with higher retail investing activity.')
        

    if message.content == 'stonks':
        await message.channel.send(f'SPY: {spy_count}')
        await message.channel.send(f'Tesla: {tesla_count}')
        await message.channel.send(f'Nikola: {nikola_count}')
        await message.channel.send(f'Palantir: {palantir_count}')
client.run(TOKEN)

# bot is Stonks Bot
#server is Stonks Server
# guild is wsb_bot_server
# permissions integer 8 dont think i need this
#scopes url below
#https://discord.com/api/oauth2/authorize?client_id=785560444127543346&permissions=8&scope=bot