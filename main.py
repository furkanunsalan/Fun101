import discord
import random
import praw
import json
import asyncio
from discord.ext import commands
from discord.utils import *
from discord import DMChannel
import time
from functions import *
from keep_alive import keep_alive
from random import randint as r
from discord import Spotify
from datetime import datetime, timedelta
import requests
import youtube_dl
import os


example = ""
emo =":dollar: "
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="101",help_command=None, intents=intents)
game = Game()

d = datetime.now() + timedelta(hours=3, minutes=0)

duyuruyazi = f"""
      Fun101 Yenilikler:
      Bakiye Sistemi: Artık coin kazanabilir ve bununla yazıtura oynayabilirsiniz(ileride başka oyunlar
      ve market sistemi olacak)

      101bakiye: Bakiyenizi gösterir (başlangıçta 1000{emo} hediyedir)

      101günlük: 24 saatte bir alabileceğiniz 1000{emo}

      101bakiyever: Etiketlediğiniz kullanıcıya {emo} yollayabilirsiniz.

      101yazıtura: Artık {emo} ile oynanıyor. Örn: 101yazıtura 500

      101gereksizsite: Size rastgele gereksiz siteler gösterir.

      101dc: Doğruluk mu Cesaret mi oyunu.

      101hiç: Daha önce hiç ...... yapmadım.
      
      101xox: 2 kişilik xox oyunu.

      101aşı: Türkiye'deki toplam yapılan aşıları öğrenebilirsiniz!


      İyi günler dileriz, Efe & Furkan
      

        """

bot_pp = "https://cdn.discordapp.com/attachments/621719869368434699/813053963007164486/fun101.png"

bot_name = "Fun101 Bot"

embedcolor = 7440323

current_time = d.strftime("%d/%m/%Y  %H:%M  ")
print(current_time)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

reddit = praw.Reddit(
     client_id="12dfPT3Mwq22Dw",
     client_secret="arazo3VYRmDaM3yz0UQh7wqiaOoY9A",
     username="Fun101_Bot",
     password="fun12421231.",
     user_agent="fun101bot by u/Siflious&efechill")

@Bot.command("meme")
async def test(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101meme' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    subreddit = reddit.subreddit("dankmemes")
    allsubs = []
    top = subreddit.top(limit = 50)
    for submission in top:
      allsubs.append(submission)
    randomsub = random.choice(allsubs)
    name = randomsub.title
    suburl = randomsub.url
    em = discord.Embed(title = name,url = suburl, color=15484486)
    em.set_image(url = suburl)
    em.set_footer(text="Reddit",
                     icon_url="https://logodownload.org/wp-content/uploads/2018/02/reddit-logo-16.png")
    await ctx.send(embed = em)

@Bot.command("dm")
async def dm(ctx,  *, message=None):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101dm' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    await ctx.message.delete()
    furkan= await Bot.fetch_user("360826099946487809")
    message = message or "Boş Mesaj Alındı!"
    embed = discord.Embed(title="Geri Bildiriminiz Gönderildi! :incoming_envelope:", color=5563206)
    embed.add_field(name="Gönderdiğiniz Mesaj:",value= message)
    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    await DMChannel.send(furkan,f"{ctx.author}' dan Yeni bir geri bildiriminiz var :mailbox_with_mail:")
    await DMChannel.send(furkan,message)
    await ctx.send(embed=embed)

@Bot.command("geribildirim")
async def geribildirim(ctx):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101geribildirim' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
  embed=discord.Embed(title="101geribildirim :envelope:",color=embedcolor )    
  embed.add_field(name="`101dm`  :incoming_envelope:",  value="Bu komutu kullanarak bize geri bildirim gönderebilirsiniz!", inline=False)
  embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
  await ctx.send(embed=embed)

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game('101yardım'))
    print(bcolors.OKGREEN + f'Bot {Bot.user}' " Kullanıma Hazır!" + bcolors.ENDC)
    print(bcolors.OKGREEN + f"{current_time}tarihinde bot çalıştırıldı." + bcolors.ENDC)
    print(f'Şuanda {len(Bot.guilds)} sunucuda aktif!')
    print('Bağlanılan Sunucular:')
    print('')
    for server in Bot.guilds:
      print(bcolors.OKBLUE+ server.name + bcolors.ENDC)
        
@Bot.command("şarkı")
async def spotify(ctx, user: discord.Member = None):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101şarkı' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    if user == None:
        user = ctx.author
        pass
    if user.activities:
        for activity in user.activities:
            if isinstance(activity, Spotify):
                embed = discord.Embed(
                    title=f"{user.name}",
                    color=5563206)
                embed.set_thumbnail(url=activity.album_cover_url)
                embed.add_field(name="Dinlediği Şarkı", value=format(activity.title), inline= False)
                embed.add_field(name="Sanatçı", value=activity.artist)
                embed.add_field(name="Albüm", value=activity.album)
                embed.set_footer(text="Spotify",
                     icon_url="https://www.freepnglogos.com/uploads/spotify-logo-png/spotify-logo-vector-download-11.png")
                await ctx.send(embed=embed)
            else:
              await ctx.send("Dinlenilen şarkı bulunamadı.")
    else:
              await ctx.send("Dinlenilen şarkı bulunamadı.")
    
async def is_owner(ctx):
    return ctx.author.id ==  327822893331513356 or ctx.author.id ==  360826099946487809


@Bot.command("kaç")
@commands.check(is_owner)
async def kacsunucuda(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101kaç' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    await ctx.message.delete()
    print(f'Şuanda {len(Bot.guilds)} sunucuda aktif!')
    print('Bağlanılan Sunucular:')
    for server in Bot.guilds:
        print(bcolors.OKBLUE+ server.name + bcolors.ENDC)


@Bot.command("bilgi")
async def kullanicibilgi(ctx, member: discord.Member = None):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101bilgi' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
   
    if member == None:
        member = ctx.author
        if "online" in [status for status in member.status]:
              status = "Çevrimiçi"

        elif "offline" in [status for status in member.status]:
            status = "Çevrimdışı"

        elif "dnd" in [status for status in member.status]:
            status = "Rahatsız Etmeyin"

        elif "idle" in [status for status in member.status]:
          status = "Uykuda"

        embed = discord.Embed(color=embedcolor)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Ad", value=member.mention, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Durum", value=str(status), inline=False)
        embed.add_field(name="Oluşturulma Tarihi", value=member.created_at.strftime("%d/%m/%Y  %H:%M  "), inline=False)
        embed.add_field(name="Katılma Tarihi", value=member.joined_at.strftime("%d/%m/%Y  %H:%M  "), inline=True)
        embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
        await ctx.send(embed=embed)
    else: 
        if "online" in [status for status in member.status]:
              status = "Çevrimiçi"

        elif "offline" in [status for status in member.status]:
            status = "Çevrimdışı"

        elif "dnd" in [status for status in member.status]:
            status = "Rahatsız Etmeyin"
            
        elif "idle" in [status for status in member.status]:
          status = "Uykuda"

        embed = discord.Embed(color=embedcolor)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Ad", value=member.mention, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Durum", value=str(status), inline=False)
        embed.add_field(name="Oluşturulma Tarihi", value=member.created_at.strftime("%d/%m/%Y  %H:%M  "), inline=False)
        embed.add_field(name="Katılma Tarihi", value=member.joined_at.strftime("%d/%m/%Y  %H:%M  "), inline=True)
        await ctx.send(embed=embed)

@Bot.command("bot")
async def botb(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101bot' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed = discord.Embed(color=embedcolor)
    embed.set_thumbnail(
        url=bot_pp)
    embed.add_field(name="Bot:", value=ctx.me.mention, inline=True)
    embed.add_field(name="ID", value=ctx.me.id, inline=True)
    embed.add_field(name="Oluşturulma Tarihi", value=ctx.me.created_at.strftime("%d/%m/%Y  %H:%M  "), inline=False)
    embed.add_field(name="Katılma Tarihi", value=ctx.me.joined_at.strftime("%d/%m/%Y  %H:%M  "), inline=True)
    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    await ctx.send(embed=embed)

tokatgifleri = ["https://media1.tenor.com/images/9b408bd50a738f795bc7f3ceebd2b2cb/tenor.gif?itemid=17672480",
"https://media1.tenor.com/images/31f29b3fcc20a486f44454209914266a/tenor.gif?itemid=17942299",
"https://media1.tenor.com/images/49de17c6f21172b3abfaf5972fddf6d6/tenor.gif?itemid=10206784",
"https://media1.tenor.com/images/74db8b0b64e8d539aebebfbb2094ae84/tenor.gif?itemid=15144612",
"https://media1.tenor.com/images/e29671457384a94a7e19fea26029b937/tenor.gif?itemid=10048943",
"https://media1.tenor.com/images/6722d10331eacb1a514aa41d0aa263e2/tenor.gif?itemid=9342231",
"https://media1.tenor.com/images/2f95e402b0837bbb858c570d9cd4022f/tenor.gif?itemid=4051071",
"https://media1.tenor.com/images/d40977fe97c6c94215a9b84f990357f7/tenor.gif?itemid=7339789",
"https://media1.tenor.com/images/f89e82f50a8b552eba781f912e6b259d/tenor.gif?itemid=4590339",
"https://media1.tenor.com/images/49796f431821592cafbdd97092347a00/tenor.gif?itemid=3468779",
"https://media1.tenor.com/images/3c161bd7d6c6fba17bb3e5c5ecc8493e/tenor.gif?itemid=5196956",
"https://media1.tenor.com/images/d2257d7a3803a4aabcdddf3878149d01/tenor.gif?itemid=14279719",
"https://media1.tenor.com/images/29c7edfb6df189e313354fb3423ce333/tenor.gif?itemid=15308590",
"https://media1.tenor.com/images/42621cf33b44ca6a717d448b1223bccc/tenor.gif?itemid=15696850",
"https://media1.tenor.com/images/df8af24e5756ecf4a4e8af0c9ea6499b/tenor.gif?itemid=4902917",
"https://media1.tenor.com/images/bc858e69d5022807b84554b2d4583c10/tenor.gif?itemid=5013065",
"https://media1.tenor.com/images/3380661a98f11e2bdc0a0082f551fe91/tenor.gif?itemid=15151334",
"https://media1.tenor.com/images/cdbedebfa1ce2e1a6268c5213916a007/tenor.gif?itemid=13621308",
"https://media1.tenor.com/images/9c650b319d1296337ed5566f88654877/tenor.gif?itemid=14567647",
"https://media1.tenor.com/images/6aa432caad8e3272d21a68ead3629853/tenor.gif?itemid=4474446"]

@Bot.command("tokatla")
async def tokatt(ctx, member: discord.Member):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101tokatla' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed = discord.Embed(color=embedcolor)
    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    embed.add_field(name="Tokat! ",value=(member.mention) + ",  " + (ctx.author.mention) + "     tarafından tokatlandı!")
    embed.set_image(url=random.choice(tokatgifleri))
    await ctx.send(embed=embed)

sarilgifleri = (
    "https://media1.tenor.com/images/dd1b8fe694d7bfba2ae87e1ede030244/tenor.gif?itemid=15999080",
    "https://media1.tenor.com/images/24ac13447f9409d41c1aecb923aedf81/tenor.gif?itemid=5026057",
    "https://media1.tenor.com/images/8ac5ada8524d767b77d3d54239773e48/tenor.gif?itemid=16334628",
    "https://media1.tenor.com/images/216e23dbe3daddc40e5e17778fe29293/tenor.gif?itemid=15782411",
    "https://media1.tenor.com/images/68f16d787c2dfbf23a4783d4d048c78f/tenor.gif?itemid=9512793",
    "https://media1.tenor.com/images/2d13ede25b31d946284eaa3b8a4e6b31/tenor.gif?itemid=11990658",
    "https://media1.tenor.com/images/a682682dd298ef14b535587f51a83ed3/tenor.gif?itemid=15959340",
    "https://media1.tenor.com/images/03e00c1581797c08ac7595772c08f593/tenor.gif?itemid=4201428",
    "https://media1.tenor.com/images/9d5e58e884c20e33204f54aa62928fe6/tenor.gif?itemid=15320132",
    "https://media.tenor.com/images/e844a7b7783d2fd62331a559c634dc9a/tenor.gif",
    "https://media1.tenor.com/images/c9853a84d5cbba42aba426a1256db493/tenor.gif?itemid=19608350",
    "https://media1.tenor.com/images/f3ffd3669c13ee8d091a6b583976efe9/tenor.gif?itemid=9322908",
    "https://media1.tenor.com/images/4f9e31e2a854c2435d128defd1a1988d/tenor.gif?itemid=9836912",
    "https://media1.tenor.com/images/607b01352712d545f5abbc7d6ca02fdd/tenor.gif?itemid=14184904",
    "https://media1.tenor.com/images/0be55a868e05bd369606f3684d95bf1e/tenor.gif?itemid=7939558",
    "https://media1.tenor.com/images/e9064ca73302be0156b1e552e11bdace/tenor.gif?itemid=15030924",
    "https://media1.tenor.com/images/7c19731601c43d201d2bf2d235053e5c/tenor.gif?itemid=17387841")

@Bot.command("sarıl")
async def sarilll(ctx, member: discord.Member):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101sarıl' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed = discord.Embed(title=("<3"),color=16734079)
    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    embed.add_field(name="GIF ", value=(ctx.author.mention) + "," + (member.mention) + "'e sarıldı!")
    embed.set_image(url=random.choice(sarilgifleri))
    await ctx.send(embed=embed)

@Bot.command("zarvs")
async def zarvsvs(ctx, member: discord.Member, *args):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101zarvs' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    await ctx.send(member.mention + ",    " + ctx.author.mention + " sana meydan okuyor! Zarlar atılıyor...")
    await ctx.send(ctx.author.mention + " :game_die: zar atıyor...")
    time.sleep(1)
    zarauthor = r(1, 6)
    await ctx.send(zarauthor)
    time.sleep(0.5)
    await ctx.send(member.mention + " :game_die: zar atıyor...")
    zarmember = r(1, 6)
    await ctx.send(zarmember)
    time.sleep(0.5)
    if zarauthor > zarmember:
        await ctx.send(
            ctx.author.mention + " kazandı! :tada:    " + member.mention + "  belki bir dahaki sefere! :sob:")

    elif zarmember > zarauthor:
        await ctx.send(
            member.mention + " kazandı! :tada:    " + ctx.author.mention + "  belki bir dahaki sefere! :sob:")

    else:
        await ctx.send(ctx.author.mention + " ve " + member.mention + "  berabere kaldı! :handshake:")

@Bot.command("zar")
async def zar(ctx, *args):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101zar' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    await ctx.send(game.roll_dice())

@Bot.command("tekrarla")
async def speak(ctx, *, text):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101tekrarla' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")



@Bot.command("tkm")
async def taskagitmakas(ctx, text):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101tkm' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    tkmliste = ("Taş", "Kağıt", "Makas")
    tkmicon = "https://cdn.discordapp.com/attachments/621719869368434699/792995188582645780/furkanpng.png"
    botsecim = random.choice(tkmliste)
    secimkazandi = ((ctx.author.mention) + "   Kazandı :trophy:")
    secimkaybetti = ((ctx.author.mention) + "   Kaybetti :sob:")
    if text == "Taş":
        if botsecim == "Taş":
            embed = discord.Embed(title="Benim seçimim...", colour=16383227 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :rock:", value="Berabere :handshake:", inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)

        elif botsecim == "Makas":
            embed = discord.Embed(title="Benim seçimim...", colour=5563206 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :scissors:", value=secimkazandi, inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)

        elif botsecim == "Kağıt":
            embed = discord.Embed(title="Benim seçimim...", colour=15484486 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :page_with_curl:", value=secimkaybetti, inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)

    elif text == "Kağıt":
        if botsecim == "Taş":
            embed = discord.Embed(title="Benim seçimim...", colour=5563206 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :rock:", value=secimkazandi, inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)

        elif botsecim == "Makas":
            embed = discord.Embed(title="Benim seçimim...", colour=15484486 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :scissors:", value=secimkaybetti, inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)

        elif botsecim == "Kağıt":
            embed = discord.Embed(title="Benim seçimim...", colour=16383227 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :page_with_curl:", value="Berabere :handshake:", inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)

    elif text == "Makas":
        if botsecim == "Taş":
            embed = discord.Embed(title="Benim seçimim...", colour=15484486)
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :rock:", value=secimkaybetti, inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)
        elif botsecim == "Makas":
            embed = discord.Embed(title="Benim seçimim...", colour=16383227 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :scissors:", value="Berabere :handshake:", inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)

        elif botsecim == "Kağıt":
            embed = discord.Embed(title="Benim seçimim...", colour=5563206 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :page_with_curl:", value=secimkazandi, inline=True)
            embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
            await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Hatalı Seçim!", colour=15484486)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/791041260524797985/792341701280268288/furkanpng.png")
        embed.add_field(name="Lütfen aşağıdaki seçimlerden birini yapınız.", value="Taş,Kağıt,Makas", inline=False)
        embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
        await ctx.send(embed=embed)

@Bot.command("tahmin")
async def guessing(ctx, text):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101tahmin' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    tahminliste = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    tahminsonuc = random.choice(tahminliste)
    dogruliste = ("Doğru bildin! :partying_face:", "Nokta atışı! :dart:", "Sen bu işi biliyorsun! :sunglasses:")
    dogrucevap = random.choice(dogruliste)
    
    if text in tahminliste:
      if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
      else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    else:
        embed = discord.Embed(color=15484486)
        embed.add_field(name="Hatalı Seçim!", value=ctx.author.mention + "," + " lütfen 1 ile 10 arasında bir sayı gir.",inline=False)
        await ctx.send(embed=embed)
        
@Bot.command("mood")
async def mood(ctx, *args):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101mood' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed=discord.Embed(color=embedcolor)
    embed.add_field(name="Moodun:", value= game.emoji(), inline=False)
    await ctx.send(embed=embed)

@Bot.command("kahin")
async def kahin(ctx, *args):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101kahin' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed=discord.Embed(color=embedcolor)
    embed.add_field(name="Düşünüyorum...", value= game.sekiz_top(), inline=False)
    await ctx.send(embed=embed)
@Bot.command("muteall")
@commands.has_permissions(manage_channels=True, administrator=True)
async def muteall(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101muteall' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)
    embed=discord.Embed(color=embedcolor)
    embed.add_field(name="101muteall", value=f"{ctx.author.mention},  **{ctx.channel}** kanalındaki herkesi susturdu! :mute:", inline=True)
    embed.set_footer(text=bot_name,icon_url=bot_pp)
    await ctx.send(embed=embed)

@Bot.command("unmuteall")
@commands.has_permissions(manage_channels=True, administrator=True)
async def unmuteall(ctx,):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101muteall' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)
    embed=discord.Embed(color=embedcolor)
    embed.add_field(name="101unmuteall", value=f"{ctx.author.mention},  **{ctx.channel}** kanalındaki herkesin sesini açtı! :loud_sound:", inline=True)
    embed.set_footer(text=bot_name,icon_url=bot_pp)
    await ctx.send(embed=embed)

@Bot.command("mute")
@commands.has_permissions(manage_channels=True, administrator=True)
async def mute(ctx, user: discord.Member):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101mute' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    if str(user.status) != "online":
      await user.edit(mute=True)
      embed=discord.Embed(title="101mute",color=embedcolor)
      embed.set_thumbnail(url=user.avatar_url)
      embed.add_field(name= " Susturuldu! :mute:  ",value=user.mention,inline=True)
      embed.set_footer(text=bot_name,
      icon_url=bot_pp)
      await ctx.send(embed=embed)
        
@Bot.command("unmute")
@commands.has_permissions(manage_channels=True, administrator=True)
async def unmute(ctx, user: discord.Member):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101unmute' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    if str(user.status) != "online":
        await user.edit(mute=False)
        embed=discord.Embed(title="101unmute",color=embedcolor)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name= "Artık konuşabilir! :loud_sound:  ",value=user.mention,inline=True)
        embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
        await ctx.send(embed=embed)

gifler = (
    "https://media.tenor.com/images/71c36964aa6bd434a315f334984bca8b/tenor.gif",
    "https://media.tenor.com/images/a05b34291e3b9b27f2bc807a40768401/tenor.gif",
    "https://media1.tenor.com/images/adf072c48a6c33876980aa0830bf94ca/tenor.gif",
    "https://media1.tenor.com/images/b56605bb6cc592d82e13e64d41c70aaf/tenor.gif",
    "https://media1.tenor.com/images/494c983c2c205ac1bb16bab31162db5f/tenor.gif",
    "https://media1.tenor.com/images/439de8dbf1e208eaa2562e7c615fc668/tenor.gif",
    "https://media.tenor.com/images/534f6b5e63200482489c3ef3a3233719/tenor.gif",
    "https://media.tenor.com/images/88c61cbe18da54e445e4493b066ddf96/tenor.gif",
    "https://media.tenor.com/images/fb49a3cf50d3d4fd65ea491e05ceff0b/tenor.gif",
    "https://media.tenor.com/images/c7abe0981045a2241ae24bb9dcb7ab8f/tenor.gif",
    "https://media.tenor.com/images/e4ba95529c283f662daba2fbc386577c/tenor.gif",
    "https://media.tenor.com/images/1b3f69bdf45b36604ff1c67c0796693c/tenor.gif",
    "https://media.tenor.com/images/d9d5bc10ee006a3012bb8d793117bace/tenor.gif",
    "https://media1.tenor.com/images/f1dd7db7600ff62d97481d538efad3cf/tenor.gif",
    "https://media.tenor.com/images/b5a6fd34d65c7071210e0e5100e62c20/tenor.gif",
    "https://media.tenor.com/images/8cd3a0ab3ae34253d32081c82136ce4a/tenor.gif",
    "https://media.tenor.com/images/1d4288cb91b219fae60b25a04a29fcfe/tenor.gif",
    "https://media.tenor.com/images/62fdb502e07de1b2de8d28af6f7ad236/tenor.gif",
    "https://media.tenor.com/images/ad498799f733b2efef7f6cbf5899547c/tenor.gif",
    "https://media1.tenor.com/images/a64be27204aeb61ce9e156c9e47231c1/tenor.gif",
    "https://media1.tenor.com/images/7b58ec2b3dfc3d8c53d13397622ed23a/tenor.gif")

@Bot.command("gif")
async def komikgif(ctx, ):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101gif' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed = discord.Embed(title="GIF",color=embedcolor)
    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    embed.set_image(url=random.choice(gifler))
    await ctx.send(embed=embed)

@Bot.command("sunucu")
async def displayembed(ctx, ):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101sunucu' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    guild = ctx.guild
    embed = discord.Embed(title="Sunucu Bilgileri",color=embedcolor) 
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Sunucu İsmi", value=guild.name, inline=False)
    embed.add_field(name="Üye Sayısı", value=len(guild.members), inline=True)
    embed.add_field(name="Sunucu Sahibi", value=guild.owner.mention, inline=False)
    embed.add_field(name="Oluşturulma Tarihi",value=guild.created_at.strftime("%d/%m/%Y  %H:%M  "))
    embed.set_footer(text=bot_name,icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("sil")
@commands.has_permissions(manage_messages=True, administrator=True)
async def sil(ctx, amount=2):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101sil' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
  if amount > 50:
    await ctx.send("50'den fazla mesaj silemem!")
  else:
    await ctx.channel.purge(limit=amount)

@Bot.command("eğlence", pass_context=True, )
async def eglence(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101eğlence' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed = discord.Embed(title="Eğlence  :tada:", color=embedcolor)
    embed.add_field(name="`101şarkı` :musical_note:", value="Etiketlenen kullanıcının dinlediği şarkıyı gösterir.", inline=False)
    embed.add_field(name="`101meme` :laughing: :rofl:", value="Reddit'ten r/dankmemes subreddit'inden rastgele meme gönderir.", inline=False)
    embed.add_field(name="`101gereksizsite` :person_shrugging:", value="Gereksiz websiteler gösterir.", inline=False)
    embed.add_field(name="`101gif` :regional_indicator_g: :regional_indicator_i: :regional_indicator_f:", value="Rastgele bir gif gönderir.", inline=False)
    embed.add_field(name="`101kahin` :crystal_ball:", value="Kahin senin için bir tahmin yapar.", inline=False)
    embed.add_field(name="`101mood` :partying_face: :sob: :laughing:", value="Mooduna göre bir emoji yollar.", inline=False)
    embed.add_field(name="`101tekrarla` :speech_balloon: :repeat:", value="Yazılan mesajı tekrarlar.", inline=False)
    embed.add_field(name="`101tokatla` :clap:", value="Etiketlenen kullanıcıyı tokatlar.", inline=False)
    embed.add_field(name="`101sarıl` :hugging:", value="Etiketlenen kullanıcıya sarılır.", inline=False)

    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    await ctx.send(embed=embed)

@Bot.command("oyunlar", pass_context=True, )
async def oyunlar(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101oyunlar' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed = discord.Embed(title="Oyunlar  :joystick:", color=embedcolor)
    embed.add_field(name="`101bakiye` :moneybag:", value="Bakiyenizi Gösterir.", inline=False)
    embed.add_field(name="`101yazıtura` :coin:", value="Yazı tura atar.", inline=False)
    embed.add_field(name="`101dc`  :champagne:", value="Doğruluk/Cesaret seçimine göre soru sorar.", inline=False)
    embed.add_field(name="`101hiç`  :wine_glass:", value="Daha önce hiç.....", inline=False)
    embed.add_field(name="`101xox`  :regional_indicator_x: :o2: :regional_indicator_x:", value="2 kişilik xox oyunu", inline=False)
    embed.add_field(name="`101zar`  :game_die:", value="6'lık zar atar.", inline=False)
    embed.add_field(name="`101zarvs`  :game_die: :vs: :game_die:", value="Etiketlenen kullanıcıyla zar kapışması başlar.", inline=False)
    embed.add_field(name="`101tkm`  :fist: :v: :raised_hand:", value="Fun101 ile taş kağıt makas!", inline=False)
    embed.add_field(name="`101tahmin` :question:", value="1-10 arası Fun101'in tahmin ettiği sayıyı bulmaya çalış!", inline=False)
    embed.add_field(name="`101dövüş` :punch:", value="Arkadaşınla ölümüne dövüş!", inline=False)
    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    await ctx.send(embed=embed)

@Bot.command("moderasyon", pass_context=True, )
async def moderasyon(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101moderasyon' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed = discord.Embed(title="Moderasyon   :tools:", color=embedcolor)
    embed.add_field(name="`101bot`  :robot:", value="Bot hakkında bilgi gösterir.", inline=True)
    embed.add_field(name="`101sunucu`  :book: ", value="Sunucu hakkında bilgi gösterir.", inline=True)
    embed.add_field(name="`101bilgi`  :restroom:", value="Etiketlenen kullanıcı hakkında bilgi gösterir.", inline=True)
    embed.add_field(name="`101sil`  :wastebasket:", value="Belirtilen sayı kadar mesaj siler.", inline=True)
    embed.add_field(name="`101mute` :mute:", value="Etiketlenen kullanıcıyı susturur.", inline=True)
    embed.add_field(name="`101unmute` :loud_sound:", value="Etiketlenen kullanıcının susturması kaldırılır.", inline=True)
    embed.add_field(name="`101muteall`  :mute:", value="Kanaldaki herkesi susturur.", inline=True)
    embed.add_field(name="`101unmuteall`  :loud_sound:", value="Kanaldaki herkesin susturması kaldırılır.", inline=True)
    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    await ctx.send(embed=embed)

@Bot.command("yardım", pass_context=True, )
async def yardim(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101yardım' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    embed = discord.Embed(title="Yardım", color=embedcolor)
    embed.add_field(name=":tools:  Moderasyon", value="`101moderasyon` ", inline=True)
    embed.add_field(name=":tada:  Eğlence", value="`101eğlence` ", inline=False)
    embed.add_field(name=":joystick:  Oyunlar ", value=" `101oyunlar` ", inline=False)
    embed.add_field(name=":envelope:  Geri Bildirim ", value=" `101geribildirim`", inline=False)
    embed.set_footer(text=bot_name,
                     icon_url=bot_pp)
    await ctx.send(embed=embed)

@Bot.command("dövüş")
async def battle(ctx, member: discord.Member):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101dövüş' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    gonderencan = 100
    etiketlenencan = 100
    etiketlenen = member.mention
    gonderen = ctx.message.author.mention
    bot = ctx.me.mention
    tur = r(0,1)
    
    if etiketlenen == gonderen:
        await ctx.send(f"Kendinle dövüşemezsin :sob: {gonderen} ")

    elif etiketlenen == bot:
      await ctx.send(f"Benimle dövüşemezsin :sob: {gonderen}")

    else:
        await ctx.send(f'{gonderen} vs {etiketlenen}, acaba kim kazanacak?')
        while gonderencan > 0 and etiketlenencan > 0:
          if tur == 0:
            dmg1 = r(0,35)
            dmg2 = r(0,35)
            dmg4 = r(10,45)
            dmg5 = r(15,50)
            dmg6 = r(15,50)
            dmg7 = r(35,60)
            dmg8 = r(35,60)
            dmg9 = r(45,60)
            dmg10 = r(60,100)
            dmglist = (dmg1,dmg2,dmg4,dmg5,dmg6,dmg7,dmg8,dmg9,dmg10)
            await ctx.send(f'{gonderen}: `yumruk`, `şifa`, `teslim ol`')

            def check(m):
                return m.content == 'yumruk' and m.author == ctx.message.author or m.content == 'şifa' and m.author == ctx.message.author or m.content == 'teslim ol' and m.author == ctx.message.author

            response = await Bot.wait_for('message', check = check)
            if "yumruk" in response.content.lower():              
                if etiketlenencan > 0:
                    dmg = random.choice(dmglist)
                    if dmg == 0:
                        await ctx.send(f"**{gonderen}, yumruğunu kaçırdı!** :sob:")
                        tur = 1
                    else:
                      etiketlenencan = etiketlenencan - dmg
                      if etiketlenencan <= 0:
                        etiketlenencan = 0
                      
                      await ctx.send(f"{etiketlenen}   **{etiketlenencan}** cana düştü. {gonderen}  **{dmg}** vurdu.")
                      tur = 1
                      if etiketlenencan<= 0:
                          await ctx.send(f"**{gonderen} dövüşü kazandı**")
                          tur = 1
                          break
                elif etiketlenencan <= 0:
                    await ctx.send(f"**{gonderen} dövüşü kazandı**")
                    tur = 1
                    break
            if "şifa" in response.content.lower():
                  sifamiktar=r(5,30)
                  makscan = 150
                  gonderencan = gonderencan + sifamiktar
                  if gonderencan <= makscan:
                    await ctx.send(f"{gonderen}  {sifamiktar} can şifalandı! {gonderen} **{gonderencan}** can oldu!")
                    tur = 1
                  elif gonderencan > makscan:
                    gonderencan = 150
                    await ctx.send(f"{sifamiktar} can kazanmaya çalıştın fakat en fazla {makscan} canın olabilir. Daha fazla can alamazsın! ")
                    tur = 1
            if "teslim ol" in response.content.lower():
                await ctx.send(f"{gonderen} **{gonderencan}** canla teslim oldu. {etiketlenen} **{etiketlenencan}** canı varken kazandı.")
                etiketlenencan = etiketlenencan - 200
                gonderencan = gonderencan - 200
                break
          elif tur == 1:
            dmg1 = r(0,35)
            dmg2 = r(0,35)
            dmg4 = r(10,45)
            dmg5 = r(15,50)
            dmg6 = r(15,50)
            dmg7 = r(35,60)
            dmg8 = r(35,60)
            dmg9 = r(45,60)
            dmg10 = r(60,100)
            dmglist = (dmg1,dmg2,dmg4,dmg5,dmg6,dmg7,dmg8,dmg9,dmg10)
            await ctx.send(f'{etiketlenen}: `yumruk`, `şifa`, `teslim ol`')
            def check(m):
                return m.content == 'yumruk' and m.author == member or m.content == 'şifa'  and m.author == member or m.content == 'teslim ol' and m.author == member
            response = await Bot.wait_for('message', check = check)
            if "yumruk" in response.content.lower():
                if etiketlenencan > 0:
                      dmg = random.choice(dmglist)
                      if dmg == 0:
                        await ctx.send(f"**{etiketlenen}, yumruğunu kaçırdı!** :sob:")
                        tur = 0
                      else:
                        gonderencan = gonderencan - dmg
                        if gonderencan <= 0:
                          gonderencan = 0
                        await ctx.send(f"{gonderen}   **{gonderencan}** cana düştü. {etiketlenen}  **{dmg}** vurdu.")
                        tur = 0
                        if gonderencan<= 0:
                            await ctx.send(f"**{etiketlenen} dövüşü kazandı**")
                            break
                elif gonderencan <= 0:
                    await ctx.send(f"**{etiketlenen} dövüşü kazandı**")
                    break
            if "şifa" in response.content.lower():
                  sifamiktar=r(5,30)
                  makscan = 150
                  etiketlenencan = etiketlenencan + sifamiktar
                  if etiketlenencan <= makscan:
                    await ctx.send(f"{etiketlenen}  {sifamiktar} can şifalandı! {etiketlenen} **{etiketlenencan}** can oldu!")
                    tur = 0
      
                  elif etiketlenencan > makscan:
                    etiketlenencan = 150
                    await ctx.send(f"{sifamiktar} can kazanmaya çalıştın fakat en fazla {makscan} canın olabilir. Daha fazla can alamazsın! ")
                    tur = 0
                  
            if "teslim ol" in response.content.lower():
                  await ctx.send(f"{etiketlenen} **{etiketlenencan}** canla teslim oldu. {gonderen} **{gonderencan}** canı varken kazandı.")
                  break


@Bot.command("dc")
async def dogruluk(ctx, member: discord.Member = None ):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101dc' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
  
  if member == None:
    
    await ctx.send("Doğruluk mu? Cesaret mi?")
    def check(m):
        return m.content == 'doğruluk' and m.author == ctx.author or m.content == 'cesaret'  and m.author == ctx.author
    response = await Bot.wait_for('message', check = check)
    if "doğruluk" in response.content.lower():
        embed = discord.Embed(title="Doğruluk", color=embedcolor)
        embed.add_field(name="İşte Sorun!", value=game.dogruluksorular(), inline=True)
        embed.set_footer(text=bot_name,
                        icon_url=bot_pp)
        await ctx.send(embed=embed)
                
    elif "cesaret" in response.content.lower():
        embed = discord.Embed(title="Cesaret", color=embedcolor)
        embed.add_field(name="İşte Görevin!", value=game.cesaretsorular(), inline=True)
        embed.set_footer(text=bot_name,
                        icon_url=bot_pp)
        await ctx.send(embed=embed)
  else:
    await ctx.send("Doğruluk/Cesaret")
    def check(m):
        return m.content == 'doğruluk' and m.author == member or m.content == 'cesaret'  and m.author == member
    response = await Bot.wait_for('message', check = check)
    if "doğruluk" in response.content.lower():
        embed = discord.Embed(title="Doğruluk", color=embedcolor)
        embed.add_field(name="İşte Sorun!", value=game.dogruluksorular(), inline=True)
        embed.set_footer(text=bot_name,
                        icon_url=bot_pp)
        await ctx.send(embed=embed)
                
    elif "cesaret" in response.content.lower():
        embed = discord.Embed(title="Cesaret", color=embedcolor)
        embed.add_field(name="İşte Görevin!", value=game.cesaretsorular(), inline=True)
        embed.set_footer(text=bot_name,
                        icon_url=bot_pp)
        await ctx.send(embed=embed)


@Bot.command("bakiye")
async def balance(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101bakiye' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.") 
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()   

    wallet_amt =  users[str(user.id)]["wallet"] 
      
    em = discord.Embed(title = f"{ctx.author.name}, bakiyen:", color=embedcolor)
    em.add_field(name = "Wallet",value = users[str(user.id)]["wallet"] )
    
    await ctx.send(embed = em)
@Bot.command("bakiyever")
async def balancetransfer(ctx,member:discord.Member,text):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101bakiyever' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
  await open_account(ctx.author)
  await open_account(member)
  users = await get_bank_data() 
  user = ctx.author
  if user == member:
    await ctx.send("Kendine para yollayamazsın!")
  else:
    if int(text) > 0:
      if int((text)) <= users[str(user.id)]["wallet"]:
        users[str(member.id)]["wallet"] += int(text) 
        users[str(user.id)]["wallet"] -= int(text)
        
        await ctx.send(f"{user.mention}, {member.mention} kişisine {text} bakiye yolladı. ")
    else:
      await ctx.send("Lütfen geçerli bir miktar giriniz.")
@Bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    BotMessage = await ctx.send("Lütfen geçerli bir argüman giriniz.")
    
    time.sleep(2)
    await BotMessage.delete()
@Bot.command("yazıtura")
async def yazitura(ctx, *, text):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101yazıtura' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
  yazitura = ("Yazı","Tura")
  sonuc = random.choice(yazitura)
  await open_account(ctx.author)
  users = await get_bank_data() 
  user = ctx.author
  userlist = ("Yazı","Tura")
  usersecim = random.choice(userlist)
  
  if int((text)) <= users[str(user.id)]["wallet"]:
      await ctx.send(f"{user.mention},  {usersecim} seçti")
      seciyor = await ctx.send("Para havaya atılıyor...")
      time.sleep(2)
      await seciyor.edit(content =sonuc + " geldi!")
      if sonuc == usersecim:
        users[str(user.id)]["wallet"] += int(text)   
        await ctx.send(user.mention + f" {text} kazandı!")
      else:
        users[str(user.id)]["wallet"] -= int(text)   
        await ctx.send(user.mention + f" {text} kaybetti :sob:")
      with open("mainbank.json","w") as f: 
           json.dump(users,f)
  else:
    await ctx.send("Lütfen geçerli bir miktar giriniz.")
async def open_account(user):
   
    users = await get_bank_data() 

    if str(user.id) in users: 
        return False 
    else: 
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 1000    
 

    with open("mainbank.json","w") as f: 
        json.dump(users,f)
    return True


async def get_bank_data():
    with open("mainbank.json","r") as f: 
        users = json.load(f) 

    return users   

@Bot.command("aşı")
async def asi_sayisi(ctx):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101aşı' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")

  bosluk = ''
  response = requests.get("https://covid19asi.saglik.gov.tr")
  data = response.text
  start = data.index("<script>var yapilanasisayisi = ") + 31
  end = data.index(";</script>", start)
  embed=discord.Embed(title="Türkiye Toplam Aşı Sayısı", color=embedcolor)
  embed.add_field(name=f"  Aşılanan Kişi Sayısı:", value= f":syringe: {response.text[start:end]}" , inline=False)

  embed.set_footer(text=f"{bot_name}  {current_time} ",
                     icon_url=bot_pp)
  await ctx.send(embed=embed)


@Bot.command("gereksizsite")
async def siteyolla(ctx):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101gereksizsite' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
  await ctx.send(game.gereksizsiteler())

async def exportla(deger):
  channel = Bot.get_channel(813688774089113680)
  await channel.send(deger)
async def setup(yazi):
  consolelog = yazi
  print(bcolors.WARNING +yazi+ bcolors.ENDC)
  await exportla(yazi)

@Bot.command("hiç")
async def dahaoncehic(ctx):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101hiç' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
  await ctx.send(game.neverhaveiever())

@Bot.command("duyuru")
@commands.check(is_owner)
async def duyuru(ctx):
  d = datetime.now() + timedelta(hours=3, minutes=0)
  current_time = d.strftime("%d/%m/%Y  %H:%M  ")
  guild = ctx.guild
  await setup(guild.name+ f" sunucusunda '101duyuru' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
  guilds = ctx.message.guild
  embed=discord.Embed(color=embedcolor)
  embed.add_field(name="Duyuru!", value=duyuruyazi, inline=False)
  embed.set_footer(text=f"{bot_name}  {current_time}",icon_url = bot_pp)
  for guild in ctx.bot.guilds:
    await guilds.text_channels[0].send(embed=embed)
    
@Bot.command("günlük")
@commands.cooldown(1, 60*60*24, commands.BucketType.user)
async def gunluk(ctx):
  user = ctx.author
  await open_account(user)
  users = await get_bank_data() 
  users[str(user.id)]["wallet"] += 1000     
  await ctx.send(f"günlük bakiyen olan 1000 i aldın!")
  with open("mainbank.json","w") as f: 
              json.dump(users,f)





@Bot.command("xox")
async def tictactoe(ctx,  p2: discord.Member):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101xox' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    global count
    global player1
    global player2
    global turn
    global gameOver
    p1 = ctx.author
    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = ctx.author
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send(f"{player1.mention}, sıra sende.")
        elif num == 2:
            turn = player2
            await ctx.send(f"{player2.mention}, sıra sende.")
    else:
        await ctx.send("Şuanda zaten bir oyun oynanıyor! Yenisine başlamadan önce o oyunu bitir.")





player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@Bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                
                if gameOver == True:
                    await ctx.send(mark + " kazandı!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Berabere!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("1 ile 9 arasından bir sayı seçtiğinizden emin olun.")
        else:
            await ctx.send("Sıra şuanda sende değil.")
    else:
        await ctx.send("101xox komutunu kullanarak yeni bir oyun başlatabilirsiniz.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Lütfen işaretlemek istediğiniz noktayı 1 ile 9 arsından bir sayı girerek seçiniz.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Bir sayı girdiğinizden emin olun.")


@Bot.command("soru")
@commands.check(is_owner)
async def triviacommand(ctx):
    d = datetime.now() + timedelta(hours=3, minutes=0)
    current_time = d.strftime("%d/%m/%Y  %H:%M  ")
    guild = ctx.guild
    await setup(guild.name+ f" sunucusunda '101soru' komutu {current_time} tarihinde  {ctx.author},{ctx.author.id} tarafından çalıştırıldı.")
    soru1 = sorular("Fatih Sultan Mehmet’in babası kimdir?","a","Genel Kültür","A) II.Murat B) Yıldırım Beyazıt C) I.Mehmet")
    soru2 = sorular("İstiklal Marşı hangi yıl yazılmıştır?","b","Bilim","a) 1919 b)1921 c) 1920")
    soru3 = sorular("Kuyucaklı Yusuf adlı eser kime aittir?","a","Genel Kültür","a) Sabahattin Ali b) Yaşar Kemal c) Yusuf Atılgan")
    soru4 = sorular("18. Osmanlı’da Lale devri hangi padişah döneminde yaşamıştır?","b","Genel Kültür","a) IV. Murat b) III. Ahmet c) III. Selim")
    triviasorular = (soru1.soruicerigi,soru2.soruicerigi,soru3.soruicerigi,soru4.soruicerigi)
    triviasoru = random.choice(triviasorular)
  
    if triviasoru == soru1.soruicerigi:
      triviacevap = soru1.dogrucevap
      triviasik = soru1.siklar
      konu = soru1.konu
    elif triviasoru == soru2.soruicerigi:
      triviacevap = soru2.dogrucevap
      triviasik = soru2.siklar
      konu = soru2.konu
    elif triviasoru == soru3.soruicerigi:
      triviacevap = soru3.dogrucevap
      triviasik = soru3.siklar
      konu = soru3.konu
    
    embed=discord.Embed(color = embedcolor)
    embed.add_field(name="Soru", value=triviasoru, inline=False)
    embed.add_field(name="Şıkkı seçiniz:", value=triviasik, inline=False)
    embed.set_footer(text=konu,icon_url = bot_pp)
    await ctx.send(embed=embed)
    def check(m):
        return m.content == 'A' and m.author == ctx.author or m.content == 'B'  and m.author == ctx.author or m.content == 'C' and m.author == ctx.author 
    response = await Bot.wait_for('message', check = check) 
    if "a" in response.content.lower():
      if  triviacevap == "a":
        await ctx.send("Doğru Cevap!")
      else:
        await ctx.send(f"Yanlış, doğru cevap: {triviacevap}")
    elif "b" in response.content.lower():
      if  triviacevap == "b":
        await ctx.send("Doğru Cevap!")
      else:
        await ctx.send(f"Yanlış, doğru cevap: {triviacevap.upper()}")
    elif "c" in response.content.lower():
      if  triviacevap == "c":
        await ctx.send("Doğru Cevap!")
      else:
        await ctx.send(f"Yanlış, doğru cevap: {triviacevap}")


keep_alive()
Bot.run("NzkwOTI5NTYzNTU5MDAyMTIy.X-Hwjg.r3ADau3pajyjrqEL3MUwQ9M0Jy0")
