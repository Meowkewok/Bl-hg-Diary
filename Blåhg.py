import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
import os
root = tk.Tk()
root.title("Blåhg- Your Journal Blåhaj")
root.geometry("500x400")
root.state("zoomed")
datefont = "Arial", 24
textboxfont = "Arial", 12
homeframe = tk.Frame(root, bg="#0096FF")
homeframe.pack(fill="both", expand=True)
fileframe = tk.Frame(root, bg="#0096FF")
homeframe.pack(fill="both", expand=True)
date_label = tk.Label(root, text="", font=datefont, bg="#0096FF", fg="black")
date_label.pack(side= "top", pady=50, fill=tk.X)
text_box = tk.Text(homeframe, height=11, width=40, font=textboxfont, wrap=tk.WORD, bd=1, relief="solid", padx=10, pady=10)
text_box.pack(pady=10, padx=100, fill=tk.BOTH, expand=True)
text_box_display = tk.Text(fileframe, height=10, width=50, font=textboxfont, wrap=tk.WORD, bd=1, relief="solid", padx=10, pady=10)
text_box_display.pack(pady=20, padx=100, fill=tk.BOTH, expand=True)
image_path = "blahaj.png"
image = Image.open(image_path)
image = image.resize((400, 200))
blahaj_image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=blahaj_image, bg="#0096FF")
image_label.pack(side="top", pady=10)
def upDATE():
    date = datetime.now().strftime("%m/%d/%Y")
    date_label.config(text=date)
    root.after(60000, upDATE)
def savetext():
    date = datetime.now().strftime("%m/%d/%Y")
    enteredtext = text_box.get("1.0", "end-1c")
    if enteredtext.strip():
        with open("diaryGUI.txt", "a") as file:
            file.write(f"{date}: {enteredtext}\n\n")
        text_box.delete("1.0", "end")
        messagebox.showinfo("Entry Saved", "Your Blåhg entry has been saved successfully.")
        loadtext()
def buttonstate():
    enteredtext = text_box.get("1.0", "end-1c")
    if enteredtext.strip():
        save_button.config(state="normal")
    else:
        save_button.config(state="disabled")
    root.after(500, buttonstate)
def loadtext():
    filepath= "diaryGUI.txt"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            content = file.read()
        text_box_display.delete("1.0", "end")
        text_box_display.insert("1.0", content)
    else:
            text_box_display.insert("1.0", "No entries yet. Start writing your Blåhg!")
def frameshown(framename):
    homeframe.pack_forget()
    fileframe.pack_forget()
    if framename == "home":
        homeframe.pack(fill="both", expand=True)
    elif framename == "file":
        fileframe.pack(fill="both", expand=True)
save_button = tk.Button(homeframe, text="Save Entry", font=("Arial", 12), bg="#6495ED", fg="black", command=savetext, state="disabled")
save_button.pack(side="bottom", pady=30)
file_button = tk.Button(homeframe, text="Open Blåhg", font=("Arial", 12), bg="#6495ED", fg="black", command=lambda: frameshown("file"))
file_button.pack(side="left", padx=10, pady=30)
back_button_view = tk.Button(fileframe, text="Back to Home", font=("Arial", 12), bg="#6495ED", fg="black", command=lambda: frameshown("home"))
back_button_view.pack(side="left", padx=10, pady=10) 
frameshown("home")
loadtext()
upDATE()
buttonstate()
root.mainloop()
# Thanks for trying out my Blåhaj themed diary app!