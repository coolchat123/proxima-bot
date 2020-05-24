import discord
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import Bot

class Admin(commands.Cog, name="Admin"):
    """Administrative commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.has_role("Proxima Team")
    @commands.command()
    async def debug(self, ctx):
        """Enables or disables debugging mode"""
        embed = discord.Embed(title="Debugging disabled", description="This must be activated through console!", color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.has_role("Proxima Team")
    @commands.command()
    async def reload(self, ctx, module : str):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            print(e)
            print()
            embed = discord.Embed(title="Module error", description="Oops! That module doesn't exist.", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Module reloaded", description="The module was reloaded successfully", color=discord.Color.blue())
            await ctx.send(embed=embed)

    @commands.has_role("Proxima Team")
    @commands.command(pass_context = True)
    async def clear(self, ctx, number):
        mgs = []
        number = int(number)
        async for x in commands.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await commands.delete_messages(mgs)

def setup(bot):
    bot.add_cog(Admin(bot))
