import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
otherparent = os.path.dirname(parentdir)
ootherparent = os.path.dirname(otherparent)
sys.path.append(parentdir)
sys.path.append(otherparent)
sys.path.append(ootherparent)
from utils.bcolors import bcolors

def main():
    print("creating new " + sys.argv[1] + " model..... " + bcolors.OKGREEN + "[OK]" + bcolors.ENDC)


if __name__ == "__main__":
    main()