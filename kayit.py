from interactions import BaseContext, Embed, Extension, check, has_role, slash_command, SlashContext
from interactions.ext.prefixed_commands import prefixed_command, PrefixedContext
import pandas as pd
import json
import sqlite3

db = sqlite3.connect("kayit_olanlar.db")
cur = db.cursor()


class MyExtension(Extension):


    @prefixed_command(name="kayıt")
    async def my_command_function(self, ctx: PrefixedContext, arg):
        if ctx.member.has_role(1255534039041835141):
            cur.execute(f"SELECT 1 FROM kayit WHERE key = ? LIMIT 1;", (arg,))
            if cur.fetchone() is None:
                try:
                    self.df = pd.read_csv("database.csv")
                except FileNotFoundError:
                    await ctx.send(embed=Embed(color="RED", description="Bir aksilik çıktı lütfen moderatörlere hata kodunu iletin! _Database Error 1_"))
                
                datas = self.df.loc[self.df['encrypted_password'] == arg]["raw_user_meta_data"]
                if not datas.empty:
                    data_dict = json.loads(datas.iloc[0])
                    await ctx.author.edit_nickname(data_dict["name"])
                    await ctx.send(embed=Embed(color="GREEN", description="Kaydınız başarılı! Roleriniz veriliyor."))
                    await ctx.author.remove_role(1255534039041835141)
                    await ctx.author.add_role(1255533752310960198)
                    cur.execute("INSERT INTO kayit (user_id, key) VALUES(?, ?)", (ctx.author_id, arg))
                    db.commit()
                else:
                    await ctx.send(embed=Embed(color="RED", description="Girdiğiniz kayıt kodu sistemde gözükmüyor."))
            else:
                await ctx.send(embed=Embed(color="RED", description="Bu kayıt kodu daha önceden kullanılmış. Eğer bir hata olduğunu düşünüyorsan moderatörlerimizden yardım isteyebilirsin."))
        else:
            await ctx.send(embed=Embed(color="RED", description="Şu anda kayıtlı gözüküyorsun."))
