import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Blåhg- Your Journal Blåhaj")
root.geometry("500x400")
root.state("zoomed")
root.config(bg="#0096FF")
textboxfont = "Arial", 12
homeframe = tk.Frame(root, bg="#0096FF")
homeframe.pack(fill="both", expand=True)
fileframe = tk.Frame(root, bg="#0096FF")
searchframe = tk.Frame(root, bg="#0096FF")

date_label = tk.Label(root, text="", font=("Arial", 24), bg="#0096FF", fg="black")
date_label.pack(side= "top", pady=50, fill=tk.X)
text_box = tk.Text(homeframe, height=11, width=40, font=textboxfont, wrap=tk.WORD, bd=1, relief="solid", padx=10, pady=10)
text_box.pack(pady=10, padx=100, fill=tk.BOTH, expand=True)

text_box_display = tk.Text(fileframe, height=10, width=50, font=textboxfont, wrap=tk.WORD, bd=1, relief="solid", padx=10, pady=10)
text_box_display.pack(pady=20, padx=100, fill=tk.BOTH, expand=True)

text_box_search = tk.Text(searchframe, height=10, width=50, font=textboxfont, wrap=tk.WORD, bd=1, relief="solid", padx=10, pady=10)
text_box_search.pack(pady=20, padx=100, fill=tk.BOTH, expand=True)

image_path = "blahaj.png"
image = Image.open(image_path)
image = image.resize((400, 200))
blahaj_image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=blahaj_image, bg="#0096FF")
image_label.pack(side="top", pady=10)

def searchDATE():
    searchyear = yearentry.get()
    searchday = dayentry.get()
    searchmonth = monthentry.get()
    datesearched = (str(searchmonth) + "/" + str(searchday) + "/" + str(searchyear))
    print(datesearched)
    with open("diaryGUI.txt", "r") as file:
        lines = file.readlines()
        if any(datesearched in line for line in lines):
            text_box_search.delete("1.0", "end")
            for index, line in enumerate(lines):
                if datesearched in line:
                    text_box_search.insert("1.0", line)
        else:
            text_box_search.delete("1.0", "end")
            text_box_search.insert("1.0", "No entries found for that date")

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
    searchframe.pack_forget()
    if framename == "home":
        homeframe.pack(fill="both", expand=True)
    elif framename == "file":
        fileframe.pack(fill="both", expand=True)
    elif framename == "search":
        searchframe.pack(fill="both", expand=True)

save_button = tk.Button(homeframe, text="Save Entry", font=("Arial", 12), bg="#6495ED", fg="black", command=savetext, state="disabled")
save_button.pack(side="bottom", pady=30)

file_button = tk.Button(homeframe, text="Open Blåhg", font=("Arial", 12), bg="#6495ED", fg="black", command=lambda: frameshown("file"))
file_button.pack(side="left", padx=10, pady=30)

search_button = tk.Button(searchframe, text="Search Date", font=("Arial", 12), bg="#6495ED", fg="black", command=lambda: searchDATE())
search_button.pack(side="left", padx=10, pady=30)

back_button_view = tk.Button(fileframe, text="Back to Home", font=("Arial", 12), bg="#6495ED", fg="black", command=lambda: frameshown("home"))
back_button_view.pack(side="left", padx=10, pady=10) 

searchframe_button_home = tk.Button(homeframe, text="Search Entries", font=("Arial", 12), bg="#6495ED", fg="black", command=lambda: frameshown("search"))
searchframe_button_home.pack(side="left", padx=10, pady=10)

searchframe_button_view = tk.Button(fileframe, text="Search Entries", font=("Arial", 12), bg="#6495ED", fg="black", command=lambda: frameshown("search"))
searchframe_button_view.pack(side="left", padx=10, pady=10)

searchframe_button_return = tk.Button(searchframe, text="Back to Home", font=("Arial", 12), bg="#6495ED", fg="black", command=lambda: frameshown("home"))
searchframe_button_return.pack(side="left", padx=10, pady=10)

days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
years = [str(year) for year in range(2000, datetime.now().year + 1)]

monthentry = ttk.Combobox(searchframe, values=months)
monthentry.set("Select Month")
monthentry.pack(side="left", padx=10, pady=10)

dayentry = ttk.Combobox(searchframe, values=days)
dayentry.set("Select Day")
dayentry.pack(side="left", padx=10, pady=10)

yearentry = ttk.Combobox(searchframe, values=years)
yearentry.set("Select Year")
yearentry.pack(side="left", padx=10, pady=10)

frameshown("home")
loadtext()
upDATE()
buttonstate()
root.mainloop()
