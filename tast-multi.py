import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = entry.get()
    if text.strip():
        tts = gTTS(text=text, lang="en")
        tts.save("output.mp3")
        os.system("start output.mp3")
    else:
        messagebox.showwarning("Warning", "Please enter some text!")

def set_text():
    entry.delete(0, tk.END)
    entry.insert(0, " ")

def exit_app():
    window.destroy()


window = tk.Tk()
window.title("Text to Speech")
window.geometry("400x300")

label = tk.Label(window, text="Text to Speech", font=("Arial", 18),width=40)
label.pack(pady=10)


entry = tk.Entry(window, width=30, font=("Arial", 12))
entry.pack(pady=10)


frame = tk.Frame(window)
frame.pack(pady=10)

play_button = tk.Button(frame, text="Play", bg="#ec45b2", fg="white",width=8,height=2,font=("Arial",12), command=play_text)
play_button.grid(row=0, column=0, padx=5)

exit_button = tk.Button(frame, text="Exit", bg="#f08dde", fg="black",width=8,height=2,font=("Arial",12), command=exit_app)
exit_button.grid(row=0, column=1, padx=5)

set_button = tk.Button(frame, text="Set", bg="#ec45b2", fg="white",width=8,height=2,font=("Arial",12), command=set_text)
set_button.grid(row=0, column=2, padx=5)

window.mainloop()