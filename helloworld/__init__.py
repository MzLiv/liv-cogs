from .helloworld import Helloworld


def setup(bot):
    bot.add_cog(Helloworld(bot))