# CONFIG
# -----------------------------------------------------
token = "Your token here" # INSERT BOT TOKEN HERE
counting_channel = "Your channel id" # INSERT CHANNEL ID HERE
delay = [0.5, 5] # DELAY BETWEEN COUNTING
selfbot = False # Change this if using BOT ACCOUNT
last_number = "" # Optional, it starts counting from this number

mode = "BINARY" # CHOOSE MODE OF COUNTING
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
async def on_message(message):
    global last_number
    if bot.user.id != message.author.id and message.channel.id == int(counting_channel):
        channel = bot.get_channel(int(counting_channel))
        try:
            if last_number == "" and mode == "INCREMENTAL":
                last_number = int(message.content)
            elif last_number == "" and mode == "BINARY":
                last_number = int(message.content, 2)
        except:
            pass
        else:            
            if mode == "INCREMENTAL" and int(message.content) < last_number:
                print("Lower number posted, doing nothing!")
            elif mode == "INCREMENTAL" and int(message.content) > (last_number + 1):
                print("too high number, doing nothing!")
            elif mode == "BINARY" and int(message.content, 2) < last_number:
                print("Lower number posted, doing nothing!")
            elif mode == "BINARY" and int(message.content, 2) > (last_number + 1):
                print("too high number, doing nothing!")
            else:
                time.sleep(random.uniform(delay[0], delay[1]))
                last_number += 2
                if mode == "INCREMENTAL":
                    num = int(message.content)
                    bigger_num = num + 1
                    
                    await channel.send(bigger_num)
                    print("SENDING: " + str(bigger_num))
                    print("NEXT NUMBER: " + str(last_number))
                    
                elif mode == "BINARY":
                    num = int(message.content, 2)
                    bigger_num = "{0:b}".format(num + 1)
                    
                    await channel.send(bigger_num)
                    print("SENDING: " + str(bigger_num))
                    print("NEXT NUMBER: " + str("{0:b}".format(last_number)))
            

bot.run(token, bot=(not selfbot))
print("\nExiting, have a nice day!")
