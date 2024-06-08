# Register Discord Commands Script
Python utility for invoking Discord DevelopersAPI with Bot Commands to add

## Prerequisites
- Python `3.12`
- Registered Discord Bot ([Bots can be registered here.]([Discord Developer Portal](https://discord.com/developers/)))

## Configuration
### Bot Configuration
In order to use this script, you must supply an Application ID and a Token in a `.env` file at the project root.
- Obtaining the Application ID can be done in the [Discord Developer Portal](https://discord.com/developers/)
  - Under the `General Information` tab, there will be an `Application ID`
- Obtaining the Token is a one-time read, and if you misplace the token you will have to rotate it. This means anything you have configured with that old token will no longer work until the token is updated, so be careful.
  - Under the `Bot` tab, there is a `Token` section to obtain one.
- When you have obtained these, add the following to your `.env` file:
  - ```
    discord_bot_token=<Enter your Token>
    discord_app_id=<Enter your Application ID>
    ```
### Command Customization
The commands in the `discord_commands.yaml` file are commands for the `Ball Chaser` Discord Bot for Rocket League. You will want to replace these commands with the commands for your bot.
Be sure to follow the [Discord Commands API Wiki](https://discord.com/developers/docs/interactions/application-commands) when authoring your commands

## Execution
To run the script, simply execute:
```commandline
py ./register-commands
```