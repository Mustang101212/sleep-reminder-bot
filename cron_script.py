import sys
import discord
import random
import praw
import os


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        user = client.get_user(
            853363486112874519)  # discord user ID, 853363486112874519 for testing, 299779317183938562 for usuage
        if phase == 1:
            message = "```" + random.choice(phase_1) + "```"
        elif phase == 2:
            message = "```" + random.choice(phase_2) + "```"
        elif phase == 3:
            message = "```" + random.choice(phase_3) + "```"
        else:
            message = "```Error: Something went wrong with the phase selection. Phase was: " + phase + "```"
        await user.send(message)
        print(type(phase))
        if phase == 1 and cat_img is not None:
            await user.send("```Here is your daily cat content! (taken from the top page of reddit): ```")
            await user.send(cat_img)
        elif phase == 2:
            channel = self.get_channel(1388559078372151348)  # discord channel ID
            try:
                msg = await channel.fetch_message(channel.last_message_id)
            except discord.NotFound:
                print("No last message found in the channel.")
                exit(0)  # Exit if no last message found
            attachment = [await a.to_file() for a in msg.attachments]
            if attachment:
                await user.send(
                    "```Bonus content```")
                await user.send(files=attachment)
                await msg.delete()
        exit(0)  # Exit the script after sending the message


def get_reddit_cat_image():
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="sleep-reminder-bot (by u/Mustang101212)",
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

    posts = list(reddit.subreddit("cats").top(time_filter="day", limit=10))

    for post in posts:
        if post.url.endswith((".jpg", ".png", ".gif", ".jpeg")):
            return post.url
    return None


cat_img = get_reddit_cat_image()

phase_1 = open('list1.txt').read().splitlines()
phase_2 = open('list2.txt').read().splitlines()
phase_3 = open('list3.txt').read().splitlines()
phase = int(sys.argv[1])

client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))
