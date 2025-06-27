import os
import datetime
from zoneinfo import ZoneInfo
from discord.ext import commands, tasks
import discord

count = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        user = client.get_user(299779317183938562) # discord user ID
        await user.send(f'```Hello, bozo, bot has been started!```')
        cog = MyCog(self)

    async def on_message(self, message):
        # only respond to ourselves
        if message.author != self.user:
            return

        if message.content == 'exit':
            await message.channel.send('```Exiting...```')
            await self.close()
        if message.content == 'test':
            await message.channel.send('```Working...```')


pdt = ZoneInfo("America/Los_Angeles")

# If no tzinfo is given then UTC is assumed.
times = [
    datetime.time(hour=4, tzinfo=pdt),
    datetime.time(hour=4, minute=40, tzinfo=pdt),
    datetime.time(hour=5, minute=30, second=0, tzinfo=pdt)
]

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()
        print("Cog initialized and task started.")

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=times)
    async def my_task(self):
        print("Task started.")
        user = client.get_user(853363486112874519)  # discord user ID
        await user.send(f'Hello, {user.name}!')
        global count
        if count % 3 == 0:
            await user.send(f'```Its 11:00 PM, better be getting ready to wrap it up smh```')
        elif count % 3 == 1:
            await user.send(f'```Its getting even later, you better be in bed soon```')
        else:
            await user.send(f'```I\'m almost awake nerd, you better sleep soon if you haven\'t already!!```')
        count += 1


client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))

