class Session:
    def __init__(self):
        self.name = "Lilianux"
        self.root = "/var/www/html/"
        self.namespace = "none"
    
    def GetCurrentPath(self):
        return(self.root + self.namespace + "/")

    def GetBanner(self):
        return(self.name + "@[" + self.namespace + "] > ")