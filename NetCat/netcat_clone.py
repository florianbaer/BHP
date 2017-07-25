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

