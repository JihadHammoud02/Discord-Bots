from requests import request
from urlextract import URLExtract
import discord
import requests
import json

extractor=URLExtract()

def url_finder(msg):
    ext=extractor.find_urls(msg)
    if ext!=[]:
        return ext[0]
    return 0



def check_link(url1):
    querystring = {"url":url1}
    url = "https://exerra-phishing-check.p.rapidapi.com/"
    headers = {
        "X-RapidAPI-Host": "exerra-phishing-check.p.rapidapi.com",
        "X-RapidAPI-Key": "478e7ce64amsh569d1191267d886p1b7f84jsn3db136fa981c"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    api_return=json.loads(response.text)
    if api_return['isScam']==False:
        return 'This link is safe'
    return 'sus link '

bot=discord.Client()
token='OTgzNzI0MTQzOTI3MjYzMjkz.GO4U-w.BBI2MoI3TwInFgMkzGXtvogOxVgPUQ5_ecLyfM'





@bot.event
async def on_message(message):
    user=message.author
    if message.content=='!hey':
        await message.channel.send('Hello '+str(user.mention))
    try:
        if url_finder(message.content)!=0:
            await message.channel.send(check_link(url_finder(message.content)),reference=message)
    except:
        pass





bot.run(token)