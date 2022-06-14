
import discord
import random
import requests
import json
import time
token='OTgzNTkyMjAwNzU3NzEwODU4.G3IwXH.w-1BZikN29aBF-ypvWDVTwYYMjhfduqGXkpZXY'
list_of_memes=[]
def memes():
    url = "https://reddit3.p.rapidapi.com/subreddit"

    querystring = {"url":"https://www.reddit.com/r/memes","filter":"new"}

    headers = {
        "X-RapidAPI-Key": "3f722add89msh3718a9d2814ba6dp19173ejsn643b1ceedfc0",
        "X-RapidAPI-Host": "reddit3.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    api_return=json.loads(response.text)

    posts=api_return['posts']

    for post in posts:
        if post['is_video']==True:
            list_of_memes.append(post['media']['reddit_video']['scrubber_media_url'])
        else:
            list_of_memes.append(post['url'])


bot=discord.Client()

greetings=["hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning", "good morning", "morning",
"good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", 
"how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", 
"how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", 
"how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", 
"what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", 
"gday", "howdy"]
def choose_randomly(liste):
    return random.choice(liste)

@bot.event
async def on_message(message):
    if message.content.upper()=='HEY NEVARA':
        user=message.author
        await message.channel.send(choose_randomly(greetings)+user.mention)
    if 'now say my name' in message.content.lower():
        await message.channel.send("You're "+str(message.author))
    if 'aywa wle ' in message.content.lower():
        await message.channel.send('hehehehehehe suiiii')
    if 'memes' in message.content.lower():
        old_list=list_of_memes.copy()
        print(old_list)
        memes()
        print(list_of_memes)
        for meme in list_of_memes:
            print(meme not in old_list)
            if meme not in old_list:
                await message.channel.send(meme)


        


bot.run(token)