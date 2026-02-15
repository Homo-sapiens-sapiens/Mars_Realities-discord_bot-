import discord
import json
import os # default module
from dotenv import load_dotenv
load_dotenv() # load all the variables from the env file
bot = discord.Bot()

class User:
    #nessesary factors, will cause death if uncontrolled. Water, energy and happyness
    nes={"wt":0, "en":0, "hp":0}
    #secondary factors, will make game really hard is uncontrolled. Pesourses, poison and food
    sec={"rs":0, "ps":0, "fd":0}
    #adress of a thread where game is going and ID of user
    thread=0
    id = 0
    def __init__(self):
        print("Ааа")
        
    

events={}

@bot.event
async def on_ready():
    global events
    with open("events.json", "r", encoding="utf-8") as f:
        events = json.load(f)
    print(f"{bot.user} is ready and online!")
    
@bot.slash_command(name="newgame", description="start the game (ATTENTION: the old one will be deleted)")
async def new_game(ctx: discord.ApplicationContext):
    global events
    mes = (await ctx.send(f"Creating game thread for {ctx.author}"))
    thread = (await mes.create_thread(name=f"{ctx.author}'s game", auto_archive_duration=60))
    await thread.send(f"The new game thread for {ctx.author} was created")
    await thread.send("Человечество наконец то начало распространяться за пределы Земли. \nНадежда-1 является одной из первых колоний на Марсе")
    await thread.send(events["ru"]["0"]["text"])

@bot.slash_command(name="save", description="save your game progress.")
async def save(ctx: discord.ApplicationContext):
    await ctx.send("Сохраняем")

bot.run(os.getenv('TOKEN')) # run the bot with the token