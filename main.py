from interactions import Client, Intents, Activity

from interactions.ext import prefixed_commands
import pandas as pd 
import sqlite3 

db = sqlite3.connect("kayit_olanlar.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS kayit(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    key Text NOT NULL
    );""")
db.commit()

token="Token'ı buraya yazın lütfen."
    
intents = Intents.DEFAULT  | Intents.MESSAGE_CONTENT
activty = Activity.create("Coming back?", url= "Developed by (rembeber to fill in this gap)")
bot = Client(intents= intents, activity= activty, token= token)
prefixed_commands.setup(bot, default_prefix="l!")

bot.load_extension("test")
bot.start(token)