import discord, time, random
from discord.ext import commands

token = "Your token here" # INSERT BOT TOKEN HERE
prefix = "!" # INSERT PREFIX HERE
counting_channel = "CHANNEL ID HERE" # INSERT CHANNEL ID HERE
mode = "INCREMENTAL" # CHOOSE MODE OF COUNTING
# Currently you can choose from:
# INCREMENTAL, BINARY

last_number = ""
# The number it starts counting from
# I dont think there is need for it usually but you can set it yourself if you really want

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")
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
            print("LAST NUMBER: " + str(last_number))
            
            if mode == "INCREMENTAL" and int(message.content) < last_number:
                print("Lower number posted, doing nothing!")
            elif mode == "INCREMENTAL" and int(message.content) > (last_number + 1):
                print("too high number, doing nothing!")
            elif mode == "BINARY" and int(message.content, 2) < last_number:
                print("Lower number posted, doing nothing!")
            elif mode == "BINARY" and int(message.content, 2) > (last_number + 1):
                print("too high number, doing nothing!")
            else:
                time.sleep(random.uniform(0.5, 5))
                if mode == "INCREMENTAL":
                    num = int(message.content)
                    bigger_num = num + 1
                    last_number += 2
                    await channel.send(bigger_num)
                    print(bigger_num)
                elif mode == "BINARY":
                    num = int(message.content, 2)
                    bigger_num = "{0:b}".format(num + 1)
                    last_number += 2
                    await channel.send(bigger_num)
                    print(bigger_num)

bot.run(token, bot=False)
