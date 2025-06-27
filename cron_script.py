import os
import sys
import discord
import requests
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        user = client.get_user(299779317183938562) # discord user ID
        if phase == 1:
            message = "```" + random.choice(phase_1) + "```"
        elif phase == 2:
            message = "```" + random.choice(phase_2) +  "```"
        elif phase == 3:
            message = "```" + random.choice(phase_3) + "```"
        else:
            message = "```Error: Something went wrong with the phase selection. Phase was: " + phase + "```"
        await user.send(message)
        if phase == 1 and cat_img is not None:
            await user.send("```Here is your daily cat content!: ```")
            await user.send(cat_img)
        exit(0)  # Exit the script after sending the message

def get_reddit_cat_image():
    headers = {"User-Agent": "cat-bot/1.0"}
    url = "https://www.reddit.com/r/cats/top/.json?t=day&limit=10"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        posts = response.json()["data"]["children"]
        for post in posts:
            data = post["data"]

            # Case 1: Direct image or gif
            if data.get("post_hint") in ["image", "link"] and "url_overridden_by_dest" in data:
                url = data["url_overridden_by_dest"]
                if url.endswith((".jpg", ".png", ".gif", ".jpeg")):
                    return url

            # Case 2: Gallery post
            if data.get("is_gallery"):
                gallery_items = data.get("gallery_data", {}).get("items", [])
                media_metadata = data.get("media_metadata", {})

                for item in gallery_items:
                    media_id = item["media_id"]
                    media_info = media_metadata.get(media_id)
                    if media_info:
                        img_url = media_info.get("s", {}).get("u")
                        if img_url:
                            return img_url.replace("&amp;", "&")  # fix HTML escapes

        return None  # fallback if no images found

    except Exception as e:
        print("Reddit fetch failed:", e)
        return None

cat_img = get_reddit_cat_image()

phase_1 = open('list1.txt').read().splitlines()
phase_2 = open('list2.txt').read().splitlines()
phase_3 = open('list3.txt').read().splitlines()
phase = sys.argv[1]

client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))
