import discord
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Your bot token (set in Vercel)
GUILD_ID = 1344699990777270362  # Replace with your server ID

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
    if message.guild is None and not message.author.bot:  # Only DMs
        admin_id = 987654321098765432  # Replace with your Discord ID
        admin = await bot.fetch_user(admin_id)
        await admin.send(f"{message.author} ({message.author.id}) is requesting to join.")

        await message.author.send("Your request has been sent. Please wait for approval.")

@bot.event
async def on_message(message):
    if message.content.startswith("!approve"):
        parts = message.content.split()
        if len(parts) == 2:
            user_id = int(parts[1])
            user = await bot.fetch_user(user_id)
            invite_link = "https://discord.gg/YOUR_INVITE_LINK"  # Replace with your invite
            await user.send(f"You have been approved! Here is your invite: {invite_link}")
            await message.channel.send(f"User {user.mention} has been approved.")

bot.run(TOKEN)
