import os
import sys
import readline
from os import path
from src.utils.configreader import ConfigReader
from src.utils.bcolors import bcolors
from src.utils.bannerdisplayer import BannerDisplayer
from src.session.session import Session

def main():
    os.system("clear")

    #todo : Check les arguments du main
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--configure":
            print("configure the cli for the user")

    session = Session()
    confreader = ConfigReader("conf/app.conf")
    print(bcolors.OKBLUE + BannerDisplayer.DisplayBanner() + bcolors.ENDC)
    print(BannerDisplayer.DisplayAuthor())

    input = ""
    while(input != "exit"):
        input = raw_input(session.GetHeader() + " >>> ")
        #parse First word is the file / the module, other words are arguments

        splitted = [""]
        args = [""]
        if not input:
            splitted = [""]
        else :
            splitted = input.split()
        file = splitted[0]
        if(len(splitted) > 1):
            args = splitted[1:]
        else:
            args[0] = "--help"

        if(path.exists("src/modules/" + file + "/" + file + ".py")):
            callstring = "python src/modules/" + file + "/" + file + ".py "
            callstring += " ".join(args)
            os.system(callstring)

        elif(path.exists("src/core/" + file + "/" + file + ".py")):
            callstring = "python src/core/" + file + "/" + file + ".py "
            callstring += " ".join(args)
            os.system(callstring)

        else:
            if not input:
                print ""
            if input == "clear":
                os.system("clear")
                print(bcolors.OKBLUE + BannerDisplayer.DisplayBanner() + bcolors.ENDC + "\n")
            elif input != "exit":
                print bcolors.FAIL + "[!] unknown command \"" + file + "\". Is a module in src/modules/ missing ?" + bcolors.ENDC

if __name__ == "__main__":
    main()