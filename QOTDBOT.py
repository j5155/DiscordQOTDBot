# QOTD discord bot V0.1
# Writes used qotds to file, reads all qotds
# from channel
ReadChannel = 0000000000 # replace the 0s with
# the channel ID you want the bot to get
# it's qotds from
WriteChannel = 000000000
#replace those 0s with the channel ID you want
#the bot to send it's qotds to
import random
import time
while True:
    oldTime = time.localtime()
    now = time.localtime()
    while oldTime[2] == now[2]:
        print(str(oldTime[4]) + str(now[4]))
        time.sleep(1800)
        now = time.localtime()
    print("done")