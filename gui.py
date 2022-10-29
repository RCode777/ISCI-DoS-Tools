from concurrent.futures import thread
from struct import pack
from tkinter import *
from email.mime import image
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import socket
import random
import sys
import os
from tkinter.ttk import *
from PIL import Image, ImageTk
import threading

window = tk.Tk()

window.configure(bg="#0c1220")
window.title("ISCI DoS Tools")
window.geometry("400x600")
window.resizable(False, False)


input_frame = tk.Frame(window, bg="#0c1220")
input_frame.pack(padx=10, pady=10, fill="x", expand=True)


images = Image.open("isci07.png")
resized_image = images.resize((100, 100))
img = ImageTk.PhotoImage(resized_image)
label1 = tk.Label(image=img)
label1.image = img
label1.pack()
label1.place(x=150, y=5)

# Label
target_label = tk.Label(input_frame, font="bold",
                        fg="aqua", bg="#0c1220", text="Input Target : ")
target_label.pack(padx=10, fill="x", expand=True)


TARGET = tk.StringVar()
target_input = tk.Entry(input_frame, textvariable=TARGET,
                        bg="#262a35", border="0", fg="aqua")
target_input.pack(padx=20, pady=5, fill="x", expand=True)


def lock():
    lock_target = TARGET.get()
    hostName = socket.gethostbyname(lock_target)
    lock_label = tk.Label(input_frame, text=hostName +
                          " / Target Locked!", anchor="center", bg="#0c1220", fg="aqua")
    lock_label.pack(pady=10, padx=10, fill="x",
                    expand=True)


button = tk.Button(input_frame, text="Lock Target!",
                   command=lock, border="0", fg="#0c1220", bg="aqua")
button.pack(pady=10, padx=20, fill="x",  expand=True)


packet_label = tk.Label(input_frame, text="Packets : ",
                        bg="#0c1220", font="bold", fg="aqua")
packet_label.pack(padx=10, fill="x", expand=True)

PACKETS = tk.StringVar()
packet_input = tk.Entry(input_frame, textvariable=PACKETS,
                        bg="#262a35", fg="aqua", border="0")
packet_input.pack(padx=20, pady=5, fill="x", expand=True)


times_label = tk.Label(input_frame, text="Times : ",
                       bg="#0c1220", font="bold", fg="aqua")
times_label.pack(padx=10, fill="x", expand=True)

TIMES = tk.StringVar()
times_input = tk.Entry(input_frame, textvariable=TIMES,
                       bg="#262a35", fg="aqua", border="0")
times_input.pack(padx=20, pady=5, fill="x", expand=True)

thread_label = tk.Label(input_frame, text="Thread : ",
                        bg="#0c1220", font="bold", fg="aqua")
thread_label.pack(padx=10, fill="x", expand=True)

THREAD = tk.StringVar()
times_input = tk.Entry(input_frame, textvariable=THREAD,
                       bg="#262a35", fg="aqua", border="0")
times_input.pack(padx=20, pady=5, fill="x", expand=True)


target = TARGET.get()
packet = PACKETS.get()
times = TIMES.get()
threads = int(THREAD.get() or 0)


def attack():
    os.system("python attack.py -s " + target + " -p " +
              packet + " -t " + times + " -n " + threads)


def stop():
    sys.exit(os.system("msg * good bye"))


button = tk.Button(input_frame, text="Start Attack!",
                   bg="aqua", fg="#0c1220", border="0", width="5", command=attack)
button.pack(pady=10, padx=20, fill="x",  expand=True)

button = tk.Button(input_frame, text="Stop Attack!",
                   border="0", bg="aqua", fg="#0c1220", command=stop)
button.pack(pady=10, padx=20, fill="x",  expand=True)

for y in range(threads):
    th = threading.Thread(target=attack)
    th.start()

window.mainloop()
