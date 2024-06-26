import discord
from discord.ext import commands
token=input("Token")
class Bot(commands.Bot):
  def __init__(self):
    super().__init__(command_prefix="l!")
