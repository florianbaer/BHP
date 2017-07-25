import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "Listening from %s:%d" % (bind_ip, bind_port)

def handle_client(data_socket):
    request = data_socket.recv(1024)

    print "[*] Received: %s" % request

    data_socket.send("ACK!")
    data_socket.close()

while True:
    client, address = server.accept()
    print "Accepted connection from %s:%d" % (address[0], address[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()