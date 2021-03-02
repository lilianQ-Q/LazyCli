import random
class BannerDisplayer:

    @staticmethod
    def DisplayBanner():
        banners = [
        """ .____                          _________ .____    .___ 
|    |   _____  ___________.__.\_   ___ \|    |   |   |
|    |   \__  \ \___   <   |  |/    \  \/|    |   |   |
|    |___ / __ \_/    / \___  |\     \___|    |___|   |
|_______ (____  /_____ \/ ____| \______  /_______ \___|
        \/    \/      \/\/             \/        \/     """
    ]

        return(banners[0])

    @staticmethod
    def DisplayAuthor():
        author = """
Author      : Lilian DAMIENS
Creation    : January 2021
Description : Created because I'm a lazy person and I don't want to create the file by my own anymore on this project\n"""
        return(author)