import discord
import os # default module
from dotenv import load_dotenv
load_dotenv() # load all the variables from the env file
bot = discord.Bot()

#nessesary factors, will cause death if uncontrolled. Water, energy and happyness
nes={"wt":100, "en":100, "hp":100}
#secondary factors, will make game really hard is uncontrolled. Pesourses, poison and food
sec={"rs":100, "ps":25, "fd":100}

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="newgame", description="start the game (ATTENTION: the old one will be deleted)")
async def new_game(ctx: discord.ApplicationContext):
    message = await ctx.send(f"The new game thread for {ctx.author} was created")
    thread = (await message.create_thread(name=f"{ctx.author}'s game", auto_archive_duration=60))
    await thread.send("Человечество наконец то начало распространяться за пределы Земли. \nНадежда-1 является одной из первых колоний на Марсе")
    await thread.send("<:energy:1471857321511747737>")

bot.run(os.getenv('TOKEN')) # run the bot with the token