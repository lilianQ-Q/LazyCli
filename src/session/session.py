from src.utils.bcolors import bcolors

class Session:
    def __init__(self):
        self.name = "lilianux"
        self.workspace = "noworkspace"
        self.savepath = "none"

    def GetHeader(self):
        return(bcolors.OKBLUE + self.name + bcolors.ENDC + "::" + bcolors.OKBLUE + self.workspace + bcolors.ENDC)