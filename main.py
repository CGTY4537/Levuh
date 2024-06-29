from interactions import Client, Intents, Activity, listen

from interactions.ext import prefixed_commands
import sqlite3 

db = sqlite3.connect("kayit_olanlar.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS kayit(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    key Text NOT NULL
    );""")
db.commit()

token="MTI1NDQyNjI1MzE4MDY2NTg1Ng.GHPQDp.G716egXo9KgiM0175FXCbjFWF1GaDj2Y3D5ESo"
    
intents = Intents.DEFAULT  | Intents.MESSAGE_CONTENT
activty = Activity.create("Coming back?", url= "Developed by (rembeber to fill in this gap)")
bot = Client(intents= intents, activity= activty, token= token)
prefixed_commands.setup(bot, default_prefix="l!")

@listen()
async def on_startup():
    print("Bot is ready!")

bot.load_extension("test")
bot.start(token)