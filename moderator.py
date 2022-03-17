import discord
from discord.ext import commands

#Command Check für Supporter Commands
def is_supporter():
	async def predicate(ctx):
		return False #ToDo Supporter Check Funktion benutzen ==> Datenbank
	
	return commands.check(predicate)

#Command Check für Moderator Commands	
def is_moderator():
	async def predicate(ctx):
		return False #ToDo Moderator Check Funktion benutzen ==> Datenbank
		
	return commands.check(predicate)

#Command Check für Team Commands
def is_team():
	async def predicate(ctx):
		return False #ToDo Team Check Funktion benutzen ==> Datenbank
	

#Der im Bot registrierte Part 
class Moderator(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
	
	def cog_load(self):
		pass
	
	async def cog_check(ctx):
		return True
	
	@commands.command(name="warn")
	@commands.guild_only()
	@is_supporter()
	async def warn_member_cmd(self, ctx, member: discord.Member, reason):
		pass
	
	@warn_member_cmd.error()
	async def warn_member_cmd_error(self, ctx, error):
		if isinstance(error, commands.NoPrivateMessage):
			embed = discord.Embed(description="Dies ist ein Moderations Command. Bitte benutze ihn in einem)
