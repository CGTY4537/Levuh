from interactions import Extension
from interactions.ext.prefixed_commands import prefixed_command, PrefixedContext
class MyExtension2(Extension):
    @prefixed_command(name="help")
    async def my_command_function(self, ctx: PrefixedContext):
        await ctx.send("Eğer kayıtsız rolünüz varsa kayıt olmak için l!kayıt yazıp boşluk bırakarak leva şifrenizi ekleyin.")
