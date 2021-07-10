# CONFIG
# -----------------------------------------------------
token = "Your token here" # INSERT BOT TOKEN HERE
counting_channel = "Your channel id here" # INSERT CHANNEL ID HERE
delay = [0.5, 5] # DELAY BETWEEN COUNTING
selfbot = True # Change this if using BOT ACCOUNT
last_number = "" # Optional, it starts counting from this number

mode = "INCREMENTAL" # CHOOSE MODE OF COUNTING
# You can choose from: INCREMENTAL or BINARY
# -----------------------------------------------------

try:
    import discord, time, random, sys
except ImportError as e:
    print(e)
    exit()
    
from discord.ext import commands

if sys.version_info[0] < 3:
    print("Python 3 or a more recent version is required.")
    exit()

if token == "Your token here" or counting_channel == "Your channel id here":
    print("Please fill out the config!")
    exit()

bot = commands.Bot(command_prefix='!', self_bot=selfbot)
bot.remove_command("help")

print("Logging in...")
@bot.event
async def on_ready():
    print('Logged in as {0.user}, time to start counting!'.format(bot))
    
@bot.event
if message == "based" {
// ''Your next line is ''based''''
}
            

try:
    bot.run(token, bot=(not selfbot))
    print("\nExiting, have a nice day!")
except discord.errors.LoginFailure as e:
    print("Error: " + str(e))
