import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

def handle_client(client_socket, addr):
    try:
        conn = ""
        while conn != "closed":
            request = client_socket.recv(1024)
            print "[*] Received %s" % request
            if request == "close":
                client_socket.send("bye!")
                print "closing connection with " + addr
                client_socket.close()
                conn = "closed"
            else:
                client_socket.send("<Ok>")
    except Exception as e:
        print(e)

while True:
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client,args=(client,addr[0]))
    client_handler.start()