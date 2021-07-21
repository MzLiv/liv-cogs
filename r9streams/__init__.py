from .r9streams import R9Streams


def setup(bot):
    cog = R9Streams(bot)
    bot.add_cog(cog)
