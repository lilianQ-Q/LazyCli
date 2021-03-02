import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
otherparent = os.path.dirname(parentdir)
sys.path.append(parentdir)
sys.path.append(otherparent)
from utils.bcolors import bcolors
def DisplayHelp():

    print("")
    print(bcolors.WARNING + "Usage:" + bcolors.ENDC)
    print("model [option] <argument>\n")
    print(bcolors.WARNING + "Options:")
    print(bcolors.OKGREEN + "--help                  -h   " + bcolors.ENDC +  " Display this help message")
    print(bcolors.OKGREEN + "--quiet                 -q   " + bcolors.ENDC +  " Disallow output messages")
    print(bcolors.OKGREEN + "--create [model_name]   -c   " + bcolors.ENDC +  " Start subprocess to create a new model")
    print(bcolors.OKGREEN + "--delete [model_name]   -d   " + bcolors.ENDC +  " Delete a model")
    print("")
    print(bcolors.PURPLE + "Author " + bcolors.ENDC + " Lilianux")
    print(bcolors.PURPLE + "Date " + bcolors.ENDC + "   January 2021\n")

def main():
    splitted_path = sys.argv[0].split("/")
    currentfolder = ""
    for folder in splitted_path[:-1]:
        currentfolder += folder + "/"

    if sys.argv[1] == "--create":
        if len(sys.argv) < 3:
            print("Missing argument bud")
        elif len(sys.argv) == 3:
            os.system("python " + currentfolder + "actions/create.py " + sys.argv[2])
        elif len(sys.argv) > 3:
            print("Too many arguments")
    else:
        DisplayHelp()

if __name__ == "__main__":
    main()