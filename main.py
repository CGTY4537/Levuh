import interactions
bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

bot.start("MTI1NDQyNjI1MzE4MDY2NTg1Ng.Gy06aj.lwAHi97ACPVVzJ4h_wwEnYQ539M-KiMbVvvvlA")
from interactions import Client, Intents, Activity

from interactions.ext import prefixed_commands
token=input("Token")


    
intents = Intents.DEFAULT
activty = Activity.create("Coming back?", url= "Developed by (rembeber to fill in this gap)")
bot = Client(intents= intents, activity= activty, token= token)
prefixed_commands.setup(bot, default_prefix="l!")

bot.load_extension("test")
bot.start(token)
