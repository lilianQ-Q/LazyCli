import os
from session import Session

def test():
    saisie = ""
    while(saisie != "exit"):
        saisie = raw_input("t >>> ")
    print("Fin de test")

def main():
    session = Session()
    saisie = ""
    while(saisie != "exit"):
        saisie = raw_input(session.GetBanner())
        if os.path.isdir('/var/www/html/' + saisie):
            session.namespace = saisie
        else:
            print "notdir"

if __name__ == "__main__":
    main()