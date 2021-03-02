import socket

target_host = "127.0.0.1"
target_port = 9998

conn = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((target_host,target_port))
    conn = 1
except Exception as error:
    print "[x] Fail to connect to %s:%s" % (target_host, target_port)

if conn == 1:
    saisie = ""
    while True and saisie != "close":
        saisie = raw_input(">>> ")
        try:
            client.send(saisie)
            response = client.recv(1024)
            print "Le serveur a repondu : %s" % response
        except Exception as error:
            print(error)