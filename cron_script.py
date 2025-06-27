import os
import sys
import discord
import random

phase_1 = open('list1.txt').read().splitlines()
phase_2 = open('list2.txt').read().splitlines()
phase_3 = open('list3.txt').read().splitlines()

phase = sys.argv[1]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        user = client.get_user(853363486112874519) # discord user ID
        if phase == 1:
            message = "```" + random.choice(phase_1) + "```"
        elif phase == 2:
            message = "```" + random.choice(phase_2) +  "```"
        elif phase == 3:
            message = "```" + random.choice(phase_3) + "```"
        else:
            message = "```Error: Something went wrong with the phase selection.```"
        await user.send(message)
        exit(0)  # Exit the script after sending the message

client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))
