
import discord


client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ez-help'):
        await message.channel.send('Hello fellow humans (or at least i hope you are . . .) \n I am made by Kelton the Conqueror. \n Commands coming soon!')
 
        
#___________________________________________________________________________________________________________________________________



#_________________________________________________________________________________________________________________________________
 








client.run('NzI2NTMwOTcwNDU0NTg5NDcx.Xvex2A.JtXdTNKylGCZpkNeKZcqq320pBM')