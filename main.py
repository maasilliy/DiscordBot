import discord
from discord.ext import commands
import webbrowser
import time

TOKEN = 'ODkxMzM0NzQxNjY2NzA1NDQ4.YU82Kg.TDgu6DK8kD5omd_RgbLvwXSDbrU'
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True) # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент



@bot.command()
async def minecraft(ctx):
    embed = discord.Embed(
        title="https://ggsel.com/catalog/minecraft",
        description="Купить Майнкрафт от 29 рублей с гарантеей",
        url='https://rt.pornhub.com/gayporn',
    )
    await ctx.send(embed=embed)


bot.run(TOKEN)
