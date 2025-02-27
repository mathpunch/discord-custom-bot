import discord
import os

# Securely getting the bot token from an environment variable (set in Vercel)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Set your token in the environment variable in Vercel
GUILD_ID = 1344699990777270362  # Replace with your server ID

# Set up intents for receiving DMs and messages
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.dm_messages = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    # Ensure we ignore bot's own messages
    if message.author.bot:
        return

    # Handle direct messages (DMs)
    if message.guild is None:
        admin_id = 1342734754868363268  # Replace with your Discord ID
        admin = await bot.fetch_user(admin_id)
        await admin.send(f"{message.author} ({message.author.id}) is requesting to join.")

        # Send a response back to the user
        await message.author.send("Your request has been sent. Please wait for approval.")
    
    # Handle the !approve command in the server
    if message.guild is not None and message.content.startswith("!approve"):
        # Only allow admin to approve
        if message.author.id != 1342734754868363268:  # Check if the message sender is admin
            await message.channel.send("You do not have permission to approve users.")
            return

        parts = message.content.split()
        if len(parts) == 2:
            user_id = int(parts[1])
            user = await bot.fetch_user(user_id)
            invite_link = "https://discord.gg/yQ3rNvyVQK"  # Replace with your invite
            await user.send(f"You have been approved! Here is your invite: {invite_link}")
            await message.channel.send(f"User {user.mention} has been approved.")
        else:
            await message.channel.send("Please provide a valid user ID to approve.")

bot.run(TOKEN)
