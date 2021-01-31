import discord
import random
import praw
import asyncio
from discord.ext import commands
from discord.utils import *
from discord import DMChannel
import time
from functions import *
from keep_alive import keep_alive
from random import randint as r
from discord import Spotify

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="101",help_command=None, intents=intents)
game = Game()

reddit = praw.Reddit(
     client_id="12dfPT3Mwq22Dw",
     client_secret="arazo3VYRmDaM3yz0UQh7wqiaOoY9A",
     username="Fun101_Bot",
     password="fun12421231.",
     user_agent="fun101bot by u/Siflious&efechill")

@Bot.command("meme")
async def test(ctx):
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

@Bot.command("DM")
async def dm(ctx,  *, message=None):
    await ctx.message.delete()
    furkan= await Bot.fetch_user("360826099946487809")
    message = message or "Boş Mesaj Alındı!"
    embed = discord.Embed(title="Geri Bildiriminiz Gönderildi! :incoming_envelope:", color=6378918)
    embed.add_field(name="Gönderdiğiniz Mesaj:",value= message)
    await DMChannel.send(furkan,f"{ctx.author}' dan Yeni bir geri bildiriminiz var :mailbox_with_mail:")
    await DMChannel.send(furkan,message)
    await ctx.send(embed=embed)

@Bot.command("geribildirim")
async def geribildirim(ctx):
  embed=discord.Embed(title="101geribildirim :envelope:",color=6378918 )    
  embed.add_field(name="`101DM`  :incoming_envelope:",  value="Bu komutu kullanarak bize geri bildirim gönderebilirsiniz!", inline=False)
  embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
  await ctx.send(embed=embed)

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game('101yardım'))
    logchannel = Bot.get_channel(791778445112770570)
    print(f'Bot {Bot.user}' " Kullanıma Hazır!")
    embed = discord.Embed(title="**Fun101**", color=6378918, description="Fun101 Kullanımınıza Hazır!")
    embed.set_footer(text=" @fe#0001 | @Siflious#8620",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await logchannel.send(embed=embed)
    print(f'Şuanda {len(Bot.guilds)} sunucuda aktif!')
    print('Bağlanılan Sunucular:')
    print('')
    for server in Bot.guilds:
        print(server.name)
        
@Bot.command("şarkı")
async def spotify(ctx, user: discord.Member = None):
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

@Bot.command("kaç")
async def kacsunucuda(ctx):
    await ctx.message.delete()
    print(f'Şuanda {len(Bot.guilds)} sunucuda aktif!')
    print('Bağlanılan Sunucular:')
    for server in Bot.guilds:
        print(server.name)

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hos-geldin")
    await channel.send(f"{member.mention} aramıza katıldı. Hoş geldi!")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="ayrilanlar")
    await channel.send(f"{member.mention} Sunucudan ayrıldı.")

@Bot.command("bilgi")
async def kullanicibilgi(ctx, member: discord.Member = None):
   
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

        embed = discord.Embed(color=6378918)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Ad", value=member.mention, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Durum", value=str(status), inline=False)
        embed.add_field(name="Oluşturulma Tarihi", value=member.created_at.strftime("%d/%m/%Y  %H:%M  "), inline=False)
        embed.add_field(name="Katılma Tarihi", value=member.joined_at.strftime("%d/%m/%Y  %H:%M  "), inline=True)
        embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
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

        embed = discord.Embed(color=6378918)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Ad", value=member.mention, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Durum", value=str(status), inline=False)
        embed.add_field(name="Oluşturulma Tarihi", value=member.created_at.strftime("%d/%m/%Y  %H:%M  "), inline=False)
        embed.add_field(name="Katılma Tarihi", value=member.joined_at.strftime("%d/%m/%Y  %H:%M  "), inline=True)
        await ctx.send(embed=embed)

@Bot.command("bot")
async def botb(ctx):
    embed = discord.Embed(color=6378918)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    embed.add_field(name="Bot:", value=ctx.me.mention, inline=True)
    embed.add_field(name="ID", value=ctx.me.id, inline=True)
    embed.add_field(name="Oluşturulma Tarihi", value=ctx.me.created_at.strftime("%d/%m/%Y  %H:%M  "), inline=False)
    embed.add_field(name="Katılma Tarihi", value=ctx.me.joined_at.strftime("%d/%m/%Y  %H:%M  "), inline=True)
    embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
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
    embed = discord.Embed(color=6378918)
    embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
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
    embed = discord.Embed(title=("<3"),color=16734079)
    embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    embed.add_field(name="GIF ", value=(ctx.author.mention) + "," + (member.mention) + "'e sarıldı!")
    embed.set_image(url=random.choice(sarilgifleri))
    await ctx.send(embed=embed)

@Bot.command("zarvs")
async def zarvsvs(ctx, member: discord.Member, *args):
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
    await ctx.send(game.roll_dice())

@Bot.command("tekrarla")
async def speak(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

@Bot.command("yazıtura")
async def yazitura(ctx, *args):
    await ctx.send(game.yazi_tura())

@Bot.command("tkm")
async def taskagitmakas(ctx, text):
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
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)

        elif botsecim == "Makas":
            embed = discord.Embed(title="Benim seçimim...", colour=5563206 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :scissors:", value=secimkazandi, inline=True)
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)

        elif botsecim == "Kağıt":
            embed = discord.Embed(title="Benim seçimim...", colour=15484486 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :page_with_curl:", value=secimkaybetti, inline=True)
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)

    elif text == "Kağıt":
        if botsecim == "Taş":
            embed = discord.Embed(title="Benim seçimim...", colour=5563206 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :rock:", value=secimkazandi, inline=True)
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)

        elif botsecim == "Makas":
            embed = discord.Embed(title="Benim seçimim...", colour=15484486 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :scissors:", value=secimkaybetti, inline=True)
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)

        elif botsecim == "Kağıt":
            embed = discord.Embed(title="Benim seçimim...", colour=16383227 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :page_with_curl:", value="Berabere :handshake:", inline=True)
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)

    elif text == "Makas":
        if botsecim == "Taş":
            embed = discord.Embed(title="Benim seçimim...", colour=15484486)
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :rock:", value=secimkaybetti, inline=True)
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)
        elif botsecim == "Makas":
            embed = discord.Embed(title="Benim seçimim...", colour=16383227 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :scissors:", value="Berabere :handshake:", inline=True)
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)

        elif botsecim == "Kağıt":
            embed = discord.Embed(title="Benim seçimim...", colour=5563206 )
            embed.set_thumbnail(url=tkmicon)
            embed.add_field(name=botsecim + " :page_with_curl:", value=secimkazandi, inline=True)
            embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
            await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Hatalı Seçim!", colour=15484486)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/791041260524797985/792341701280268288/furkanpng.png")
        embed.add_field(name="Lütfen aşağıdaki seçimlerden birini yapınız.", value="Taş,Kağıt,Makas", inline=False)
        embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
        await ctx.send(embed=embed)

@Bot.command("tahmin")
async def guessing(ctx, text):
    tahminliste = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    tahminsonuc = random.choice(tahminliste)
    dogruliste = ("Doğru bildin! :partying_face:", "Nokta atışı! :dart:", "Sen bu işi biliyorsun! :sunglasses:")
    dogrucevap = random.choice(dogruliste)
    if text == "1":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "2":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "3":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "4":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "5":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "6":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "7":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "8":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "9":
        if text == tahminsonuc:
            embed = discord.Embed(color=5563206 )
            embed.add_field(name="Tebrikler!", value=ctx.author.mention + ",  " + dogrucevap,inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=15484486 )
            embed.add_field(name="Bilemedin!", value=ctx.author.mention + "," + " aklımdan " + tahminsonuc + " tutmuştum!  ",inline=False)
            await ctx.send(embed=embed)

    elif text == "10":
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
    embed=discord.Embed(color=6378918)
    embed.add_field(name="Moodun:", value= game.emoji(), inline=False)
    await ctx.send(embed=embed)

@Bot.command("kahin")
async def kahin(ctx, *args):
    embed=discord.Embed(color=6378918)
    embed.add_field(name="Düşünüyorum...", value= game.sekiz_top(), inline=False)
    await ctx.send(embed=embed)

@Bot.command("kick")
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: discord.User = None, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("Kendini atamazsın!")
        return
    if reason == None:
        reason = "Kuralları çiğnediği için yasaklandı."
    await ctx.guild.kick(member, reason=reason)
    embed=discord.Embed(color=6378918)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Atıldı!", value=f"{member.mention} sunucudan atıldı! ", inline=False)
    embed.add_field(name="Şu sebeple:",value=f"{reason}",inline=False)
    embed.set_footer(text="Fun101 Bot",icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("ban")
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: discord.User = None, reason=None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("Kendini yasaklayamazsın!")
        return
    if reason == None:
        reason = "Kuralları çiğnediği için yasaklandı."
    await ctx.guild.ban(member, reason=reason)
    embed=discord.Embed(color=6378918)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Yasaklandı!", value=f"{member.mention} sunucudan yasaklandı! ", inline=False)
    embed.add_field(name="Şu sebeple:",value=f"{reason}",inline=False)
    embed.set_footer(text="Fun101 Bot",icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("muteall")
@commands.has_permissions(manage_channels=True, administrator=True)
async def muteall(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)
    embed=discord.Embed(color=6378918)
    embed.add_field(name="101muteall", value=f"{ctx.author.mention},  **{ctx.channel}** kanalındaki herkesi susturdu! :mute:", inline=True)
    embed.set_footer(text="Fun101 Bot",icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("unmuteall")
@commands.has_permissions(manage_channels=True, administrator=True)
async def unmuteall(ctx,):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)
    embed=discord.Embed(color=6378918)
    embed.add_field(name="101unmuteall", value=f"{ctx.author.mention},  **{ctx.channel}** kanalındaki herkesin sesini açtı! :loud_sound:", inline=True)
    embed.set_footer(text="Fun101 Bot",icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("mute")
@commands.has_permissions(manage_channels=True, administrator=True)
async def mute(ctx, user: discord.Member):
    if str(user.status) != "online":
      await user.edit(mute=True)
      embed=discord.Embed(title="101mute",color=6378918)
      embed.set_thumbnail(url=user.avatar_url)
      embed.add_field(name= " Susturuldu! :mute:  ",value=user.mention,inline=True)
      embed.set_footer(text="Fun101 Bot",
      icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
      await ctx.send(embed=embed)
        
@Bot.command("unmute")
@commands.has_permissions(manage_channels=True, administrator=True)
async def unmute(ctx, user: discord.Member):
    if str(user.status) != "online":
        await user.edit(mute=False)
        embed=discord.Embed(title="101unmute",color=6378918)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name= "Artık konuşabilir! :loud_sound:  ",value=user.mention,inline=True)
        embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
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
    embed = discord.Embed(title="GIF",color=6378918)
    embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    embed.set_image(url=random.choice(gifler))
    await ctx.send(embed=embed)

@Bot.command("sunucu")
async def displayembed(ctx, ):
    guild = ctx.guild
    embed = discord.Embed(title="Sunucu Bilgileri",color=6378918)
    embed.set_footer(text="Fun101 Bot",icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Sunucu İsmi", value=guild.name, inline=False)
    embed.add_field(name="Üye Sayısı", value=len(guild.members), inline=True)
    embed.add_field(name="Sunucu Sahibi", value=guild.owner.mention, inline=False)
    embed.add_field(name="Oluşturulma Tarihi",value=guild.created_at.strftime("%d/%m/%Y  %H:%M  "))
    await ctx.send(embed=embed)

@Bot.command("sil")
@commands.has_permissions(manage_messages=True, administrator=True)
async def sil(ctx, amount=2):
  if amount > 50:
    await ctx.send("50'den fazla mesaj silemem!")
  else:
    await ctx.channel.purge(limit=amount)

@Bot.command("eğlence", pass_context=True, )
async def eglence(ctx):
    embed = discord.Embed(title="Eğlence  :tada:", color=6378918)
    embed.add_field(name="`101şarkı` :musical_note:", value="Etiketlenen kullanıcının dinlediği şarkıyı gösterir.", inline=False)
    embed.add_field(name="`101play` :cd:", value="Kullanıcının istediği şarkıları çalar.", inline=False)
    embed.add_field(name="`101meme` :laughing: :rofl:", value="Reddit'ten r/dankmemes subreddit'inden rastgele meme gönderir.", inline=False)
    embed.add_field(name="`101gif` :regional_indicator_g: :regional_indicator_i: :regional_indicator_f:", value="Rastgele bir gif gönderir.", inline=False)
    embed.add_field(name="`101kahin` :crystal_ball:", value="Kahin senin için bir tahmin yapar.", inline=False)
    embed.add_field(name="`101mood` :partying_face: :sob: :laughing:", value="Mooduna göre bir emoji yollar.", inline=False)
    embed.add_field(name="`101tekrarla` :speech_balloon: :repeat:", value="Yazılan mesajı tekrarlar.", inline=False)
    embed.add_field(name="`101tokatla` :clap:", value="Etiketlenen kullanıcıyı tokatlar.", inline=False)
    embed.add_field(name="`101sarıl` :hugging:", value="Etiketlenen kullanıcıya sarılır.", inline=False)
    embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("oyunlar", pass_context=True, )
async def oyunlar(ctx):
    embed = discord.Embed(title="Oyunlar  :joystick:", color=6378918)
    embed.add_field(name="`101yazıtura` :coin:", value="Yazı tura atar.", inline=False)
    embed.add_field(name="`101zar`  :game_die:", value="6'lık zar atar.", inline=False)
    embed.add_field(name="`101zarvs`  :game_die: :vs: :game_die:", value="Etiketlenen kullanıcıyla zar kapışması başlar.", inline=False)
    embed.add_field(name="`101tkm`  :fist: :v: :raised_hand:", value="Fun101 ile taş kağıt makas!", inline=False)
    embed.add_field(name="`101tahmin` :question:", value="1-10 arası Fun101'in tahmin ettiği sayıyı bulmaya çalış!", inline=False)
    embed.add_field(name="`101dövüş` :punch:", value="Arkadaşınla ölümüne dövüş!", inline=False)
    embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("moderasyon", pass_context=True, )
async def moderasyon(ctx):
    embed = discord.Embed(title="Moderasyon   :tools:", color=6378918)
    embed.add_field(name="`101bot`  :robot:", value="Bot hakkında bilgi gösterir.", inline=True)
    embed.add_field(name="`101sunucu`  :book: ", value="Sunucu hakkında bilgi gösterir.", inline=True)
    embed.add_field(name="`101bilgi`  :restroom:", value="Etiketlenen kullanıcı hakkında bilgi gösterir.", inline=True)
    embed.add_field(name="`101sil`  :wastebasket:", value="Belirtilen sayı kadar mesaj siler.", inline=True)
    embed.add_field(name="`101kick` :mans_shoe:", value="Etiketlenen kullanıcı sunucudan atılır.", inline=True)
    embed.add_field(name="`101ban` :no_entry_sign:", value="Etiketlenen kullanıcı sunucudan yasaklanır.", inline=True)
    embed.add_field(name="`101mute` :mute:", value="Etiketlenen kullanıcıyı susturur.", inline=True)
    embed.add_field(name="`101unmute` :loud_sound:", value="Etiketlenen kullanıcının susturması kaldırılır.", inline=True)
    embed.add_field(name="`101muteall`  :mute:", value="Kanaldaki herkesi susturur.", inline=True)
    embed.add_field(name="`101unmuteall`  :loud_sound:", value="Kanaldaki herkesin susturması kaldırılır.", inline=True)
    embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("yardım", pass_context=True, )
async def yardim(ctx):
    embed = discord.Embed(title="Yardım", color=6378918)
    embed.add_field(name=":tools:  Moderasyon", value="`101moderasyon` ", inline=True)
    embed.add_field(name=":tada:  Eğlence", value="`101eğlence` ", inline=False)
    embed.add_field(name=":joystick:  Oyunlar ", value=" `101oyunlar` ", inline=False)
    embed.add_field(name=":envelope:  Geri Bildirim ", value=" `101geribildirim`", inline=False)
    embed.set_footer(text="Fun101 Bot",
                     icon_url="https://cdn.discordapp.com/avatars/790929563559002122/f27720946f484ab1bf4203510f347c54.webp?size=1024")
    await ctx.send(embed=embed)

@Bot.command("dövüş")
async def battle(ctx, member: discord.Member):
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
"""
Line 1-12 -> Imports -> Needed Imports For The Code
Line 14-16 -> General Settings -> Game Activity, Prefix etc.
Line 18-23 -> Reddit Praw Settings -> Needed Settings For 101meme
Line 25-39 -> 101meme -> Takes A Random Post From r/dankmemes Subreddit
Line 41-50 -> 101DM -> Sends The Written Text To Siflious#8620
Line 51-58 -> 101geribildirim -> Shows How To Send Feedbacks
Line 60-74 -> Bot On Ready -> Casual Things Bot Does When It Stars
Line 76-93 -> 101şarkı -> Shows What The Tagged Person Is Listening
Line 95-101 -> 101kaç -> Shows The Servers Bot Has Joined On Terminal
Line 103-106 -> On Member Join -> Sends A Message When Someone Joins
Line 108-111 -> On Member Remove -> Sends A Message When Someone Lefts
Line 113-160 -> 101bilgi -> Shows Information About Tagged User
Line 162-173 -> 101bot -> Shows Information About Fun101 Bot
Line 175-194 -> 101tokatla Gifs -> Gif Links For 101tokatla
Line 196-203 -> 101tokatla -> Slaps The Tagged Person
Line 205-222 -> 101sarıl Gifs -> Gif Links For 101sarıl
Line 224-231 -> 101sarıl -> Hugs The Tagged Person
Line 233-254 -> 101zarvs -> Rolls 2 Dices And Sends A Winning Message
Line 256-258 -> 101zar -> Rolls A Dice
Line 260-264 -> 101tekrarla -> Repeats The Written Text
Line 266-268 -> 101yazıtura -> Flips A Coin
Line 270-358 -> 101tkm -> User Plays Rock, Paper, Scissors With Fun101  
Line 360-469 -> 101tahmin -> Bot Chooses A Number And User Tries To Guess It
Line 471-475 -> 101mood -> Decides Your Mood With Some Emojis
Line 477-481 -> 101kahin -> Bot Replies To User Question With Random Answers
Line 483-497 -> 101kick -> Kicks Tagged User If Author Has The Permission
Line 499-513 -> 101ban -> Bans Tagged User If Author Has The Permission
Line 515-524 -> 101muteall -> Mutes Every User In A Voice Channel
Line 526-535 -> 101unmuteall -> Unmutes Every User In A Voice Channel
Line 537-547 -> 101mute -> Mutes The Tagged User
Line 549-559 -> 101unmute -> Unmutes The Tagged User
Line 561-582 -> Gifs for 101gif -> Gif Links For 101gif
Line 584-590 -> 101gif -> Sends A Random Gif
Line 592-602 -> 101sunucu -> Gives Information About The Discord Server
Line 604-610 -> 101sil -> Deletes Up To 50 Messages (User tells The Amount)
Line 612-626 -> 101eğlence -> Shows All Fun Comments For Fun101
Line 628-639 -> 101oyunlar -> Shows All Game Comments For Fun101
Line 641-656 -> 101moderasyon -> Shows All Moderation Comments For Fun101
Line 658-667 -> 101yardım -> Shows Help Comments For Fun101
Line 669-792 -> 101dövüş -> Stars A Fight Between Tagged User And Message Author
Line 793-837 -> Code Comments -> Explanations For All Of Fun101's Code
Line 838-838 -> Keep Alive -> Keeps Fun101 Always Active
Line 839-839 -> Bot Run -> But Token And The Function Needed To Run Fun101
"""
keep_alive()
Bot.run("NzkwOTI5NTYzNTU5MDAyMTIy.X-Hwjg.cX_64XMhJfK8nO0RgeTwDRKo7qE")
    
