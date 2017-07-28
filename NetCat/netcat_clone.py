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
    print "-e --ececute=file_to_run - execute the given file upon a incoming connection"
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


usage()
