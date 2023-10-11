import os 
from discord_webhook import DiscordWebhook
import requests
from colorama import Fore 

async def change_the_webhook(wbh):
    os.system('cls' or 'clear')
    with open(r"config\webhook.txt", "w", encoding='utf-8') as file:
       file.write(wbh)

    r = requests.post(wbh)
    if r.status_code != 404:
           webhook = DiscordWebhook(url=wbh, content="Launch the webhook")
           response = webhook.execute()
    else:
       print(f'{Fore.RED}[?]=> Webhook isn\'t working: {r.text}{Fore.RESET}')