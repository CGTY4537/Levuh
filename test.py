from interactions import Extension, slash_command, SlashContext
from interactions.ext.prefixed_commands import prefixed_command, PrefixedContext


class MyExtension(Extension):
    @prefixed_command(name="test")
    async def my_command_function(self, ctx: PrefixedContext):
        await ctx.reply("Hello world!")