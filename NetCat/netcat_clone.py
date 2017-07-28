import socket
import threading
import subprocess
import sys
import getopt

listen              =   False
command             =   False
upload              =   False
execute             =   ""
target              =   ""
upload_destination  =   ""
port                =   3344

def usage():
    print "BHP Net Tool"
    print
    print "Usage bhpnet.py -t target_host -p port"
    print "-l --listen              - listen at [host]:[port] for incoming connections"
    print "-e --execute=file_to_run - execute the given file upon a incoming connection"
    print "-c --command             - initialize a command shell"
    print "-u --upload=destination  - upon receiving a connection upload a file to [destination]"
    print 
    print
    print "Example usages:"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c\\target.exe"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e\"cat /etc/passwd\""
    print "'echo ABCDEFGHI' | ./bhpnet.py -t 192.168.1.12 -p 333"
    sys.exit(0)

def main():
    global listen 
    global port
    global execute
    global command
    global target
    global upload_destination

    if not len(sys.argv[1:]):
        usage()

    #read the commandline options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    print opts
    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--command"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"

    # are we going to listen orjust send data from stdin?
    if not listen and len(target) and port < 0:
        
        '''
        read in the buffer from the commandline
        this will block, so send CTRL-D if not sending input
        to stdin
        '''
        buffer = sys.stdin.read()

        # send data off
        client_sender(buffer)
    
    if listen:
        server_loop()

def client_sender():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connect to the target
        client.connect((target, port))

        if len(buffer):
            client.send(buffer)
        
        while True:
            #now wait for data to come back
            recv_len = 1
            response = ""

            while recv_len:
                data        = client.recv(4096)
                recv_len    = len(data)
                response   += data

                if recv_len < 4096:
                    break
            
            print response

            # wait for more input
            buffer = raw_input("")
            buffer += "\n"

            # send it off
            client.send(buffer)

    except:
        print "[*] Exception! Exiting"

        #tear down
        client.close()

def server_loop():
    None

main()
