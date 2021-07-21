from .karastreams import KaraStreams


def setup(bot):
    cog = KaraStreams(bot)
    bot.add_cog(cog)
