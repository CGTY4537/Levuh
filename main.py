import interactions
bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

bot.start("MTI1NDQyNjI1MzE4MDY2NTg1Ng.Gy06aj.lwAHi97ACPVVzJ4h_wwEnYQ539M-KiMbVvvvlA")