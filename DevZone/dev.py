import discord
import random
import os
import json
from discord.ext import commands
from hentai import Utils, Format, Sort, Option, Path, Hentai


hentaipath = './Database/hentai_claim.json'

class nHentai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Hentai is working.')

    @commands.command()
    async def check210(self, ctx, code):
        with open(hentaipath,"r") as f:
            hentaiclaim = json.load(f)
        hentai = Hentai(code)
        # Hentai.exists(hentai.id)
        # print(hentai.title(Format.Pretty))
        embed = discord.Embed(title='Công cụ recommend 210 cho anh em:>',
                              description=' ',
                              colour=discord.Colour.blue())
        embed.add_field(name='Tên', value=hentai.title(Format.Pretty), inline=False)
        embed.add_field(name='Link', value=hentai.url, inline=False)
        embed.set_image(url=hentai.image_urls[0])
        if str(hentai.id) in hentaiclaim["history"]:
            embed.add_field(name='_____', value=f'<@{hentaiclaim["history"][str(hentai.id)]}> đã liếm bộ này', inline=False)
        await ctx.send(embed=embed)  
        with open(hentaipath,"w") as f:
            json.dump(hentaiclaim, f)   


def setup(client):
    client.add_cog(nHentai(client))