# QOTD discord bot V0.1
# Writes used qotds to file, reads all qotds
# from channel
ReadChannel = 777343154646679585 # replace the 0s with
# the channel ID you want the bot to get
# it's qotds from
WriteChannel = 777343154646679585
#replace those 0s with the channel ID you want
#the bot to send it's qotds to
import random
import time
import discord
import asyncio
running = False
class MyClient(discord.Client):
    async def on_ready(self):
        running = False
        if not running:
            running = True
            oldTime = time.localtime()
            now = time.localtime()
            #while oldTime[2] == now[2]:
                #print(str(oldTime[4]) + str(now[4]))
                #await asyncio.sleep(1800)
                #now = time.localtime()
            ReadChannel = 777343154646679585 
            WriteChannel = 777343154646679585
            ReadChannel = discord.Client.get_channel(self, id=ReadChannel)
            WriteChannel = discord.Client.get_channel(self, id=WriteChannel)
            raw_qotds = await ReadChannel.history(limit=500).flatten()
            print(str(raw_qotds))
client = MyClient()
client.run('token')
    
while True:
    oldTime = time.localtime()
    now = time.localtime()
    while oldTime[2] == now[2]:
        print(str(oldTime[4]) + str(now[4]))
        time.sleep(1800)
        now = time.localtime()
    postQotd(ReadChannel, WriteChannel)