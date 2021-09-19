# ==== installation ===
# sudo apt install python3-tk

# === get the current time ===
from time import strftime
from tkinter import Label, Tk

# === configuring window ===
window = Tk()
window.title("")
window.geometry("200x80")
window.configure(bg="green")
window.resizable(False, False)

# === logic lives here ===

clock_label = Label(window, bg="green", fg="white", font=("Times", 30), relief='flat')
clock_label.place(x=20, y=20)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label) # update value every 80 milliseconds.

update_label()
window.mainloop()
