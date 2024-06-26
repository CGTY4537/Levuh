from interactions import Client, Intents, Activity

from interactions.ext import prefixed_commands
token=input("Token")


    
intents = Intents.DEFAULT  | Intents.MESSAGE_CONTENT
activty = Activity.create("Coming back?", url= "Developed by (rembeber to fill in this gap)")
bot = Client(intents= intents, activity= activty, token= token)
prefixed_commands.setup(bot, default_prefix="l!")

bot.load_extension("test")
bot.start(token)
