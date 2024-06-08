import requests
import yaml
from dotenv import load_dotenv
import os


load_dotenv()

TOKEN = os.getenv('discord_bot_token')
APPLICATION_ID = os.getenv('discord_app_id')
URL = f"https://discordapp.com/api/v9/applications/{APPLICATION_ID}/commands"


with open("discord_commands.yaml", "r") as file:
    yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

for command in commands:
    response = requests.post(URL, json=command, headers=headers)
    command_name = command["name"]
    if response.status_code == 200:
        print(f"{command_name} has been updated!")
    elif response.status_code == 201:
        print(f"{command_name} was created!")
    else:
        print(f"Result of submitting command: name={command_name} status={response.status_code} {response.text}")
