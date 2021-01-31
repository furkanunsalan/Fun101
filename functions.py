import random
import discord
from discord.ext import commands
from random import randint as r

class Game:
    @staticmethod
    def roll_dice():
        zarsayilari = (":game_die:1", ":game_die:2", ":game_die:3", ":game_die:4", ":game_die:5", ":game_die:6")
        return random.choice(zarsayilari)

    @staticmethod
    def yazi_tura():
        liste = (":coin: Yazı", ":coin: Tura")
        return random.choice(liste)

    @staticmethod
    def sekiz_top():
        sekizcevap = (
            ":crystal_ball: Evet", ":crystal_ball:Hayır", ":crystal_ball:Kesinlikle Evet",
            ":crystal_ball:Kesinlikle Hayır", ":crystal_ball:Olabilir", ":crystal_ball:Olmayabilir",
            ":crystal_ball:Bilmem",
            ":crystal_ball:ASLA", ":crystal_ball:TAMAMIYLA DOĞRU",
            ":crystal_ball: Tekrar düşün", ":crystal_ball:Sana şimdi söylemesem iyi olur.", ":crystal_ball:Şüphesiz.", ":crystal_ball:Gördüğüm kadarıyla evet.",":crystal_ball:Gördüğüm kadarıyla hayır.", ":crystal_ball:Bu konuda bana güvenmemelisin.", ":crystal_ball:Kaynaklarım bunu doğruluyor.",":crystal_ball:Kaynaklarım bunu yalanlıyor.", ":crystal_ball:Buna güvenebilirsin", ":crystal_ball:Ben de bundan şüpheleniyorum")
        return random.choice(sekizcevap)

    @staticmethod
    def sekiztopdogrulama():
        return "Ne sormak istiyorsunuz?"

    @staticmethod
    def emoji():
        emojiler = ("( ͡° ͜ʖ ͡°)", "へ‿(ツ)‿ㄏ", "̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿",
                    "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)", "(ง ͠° ͟ل͜ ͡°)ง", "༼ つ ◕_◕ ༽つ", "ಠ_ಠ",
                    "(づ｡◕‿‿◕｡)づ", "[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]", "(ง'̀-'́)ง", "(ಥ﹏ಥ)", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]",
                    "(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)", "ლ(ಠ益ಠლ)", "♥‿♥", "༼ つ ಥ_ಥ ༽つ", "( ͡ᵔ ͜ʖ ͡ᵔ )", "◉_◉", "༼ʘ̚ل͜ʘ̚༽", "ᕦ(ò_óˇ)ᕤ",
                    "⚆ _ ⚆",
                    "ಥ_ಥ", ":')", "(°ロ°)☝", "(¬_¬)", "¯\(°_o)/¯", "ಠ~ಠ", "ಠ_ಥ", "( ﾟヮﾟ)", ">_>", "(･.◤)", "ღƪ(ˆ◡ˆ)ʃ♡ƪ(ˆ◡ˆ)ʃ♪", "─=≡Σᕕ( ͡° ͜ʖ ͡°)ᕗ", "(个_个)", "( ͡~ ͜ʖ ͡°)", "щ（ﾟДﾟщ)", "ɿ(｡･ɜ･)ɾ", "(´･_･`)", "凸( •̀_•́ )凸", "( ‾ ʖ̫ ‾)", "(╬ಠ益ಠ)", "¯\(©¿©) /¯")
        return random.choice(emojiler)
    
    @staticmethod
    def zarvss():
      zarsayilarivs = (":game_die:1", ":game_die:2", ":game_die:3", ":game_die:4", ":game_die:5", ":game_die:6")
      return random.choice(zarsayilarivs)
