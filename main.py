import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

root = Tk()
root.title("Color Picker from Image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False, False)

filename = ""  # Initialize filename to prevent errors when calling Findcolor()

def showimage():
    global filename, img  # Keep a reference to prevent garbage collection
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(), title='Select Image File',
        filetypes=[('PNG file', '*.png'), ('JPG file', '*.jpg'), ('ALL file', '*.*')]
    )

    if filename:
        img = Image.open(filename)
        img = img.resize((310, 270))  # Resize to prevent large images from breaking layout
        img = ImageTk.PhotoImage(img)  # Store reference in a global variable
        lbl.configure(image=img, width=310, height=270)
        lbl.image = img  # Keep a reference


def Findcolor():
    global filename
    if not filename:
        print("No image selected!")
        return

    try:
        ct = ColorThief(filename)
        palette = ct.get_palette(color_count=10)  # Fixed method name from get_pallette to get_palette

        rbg1 = palette[0]
        rbg2 = palette[1]
        rbg3 = palette[2]
        rbg4 = palette[3]
        rbg5 = palette[4]
        rbg6 = palette[5]
        rbg7 = palette[6]
        rbg8 = palette[7]
        rbg9 = palette[8]
        rbg10 = palette[9]

        color1 = f"#{rbg1[0]:02x}{rbg1[1]:02x}{rbg1[2]:02x}"
        color2 = f"#{rbg2[0]:02x}{rbg2[1]:02x}{rbg2[2]:02x}"
        color3 = f"#{rbg3[0]:02x}{rbg3[1]:02x}{rbg3[2]:02x}"
        color4 = f"#{rbg4[0]:02x}{rbg4[1]:02x}{rbg4[2]:02x}"
        color5 = f"#{rbg5[0]:02x}{rbg5[1]:02x}{rbg5[2]:02x}"
        color6 = f"#{rbg6[0]:02x}{rbg6[1]:02x}{rbg6[2]:02x}"
        color7 = f"#{rbg7[0]:02x}{rbg7[1]:02x}{rbg7[2]:02x}"
        color8 = f"#{rbg8[0]:02x}{rbg8[1]:02x}{rbg8[2]:02x}"
        color9 = f"#{rbg9[0]:02x}{rbg9[1]:02x}{rbg9[2]:02x}"
        color10 = f"#{rbg10[0]:02x}{rbg10[1]:02x}{rbg10[2]:02x}"

        colors.itemconfig(id1, fill=color1)
        colors.itemconfig(id2, fill=color2)
        colors.itemconfig(id3, fill=color3)
        colors.itemconfig(id4, fill=color4)
        colors.itemconfig(id5, fill=color5)
        colors2.itemconfig(id6, fill=color6)
        colors2.itemconfig(id7, fill=color7)
        colors2.itemconfig(id8, fill=color8)
        colors2.itemconfig(id9, fill=color9)
        colors2.itemconfig(id10, fill=color10)

        hex1.config(text=color1)
        hex2.config(text=color2)
        hex3.config(text=color3)
        hex4.config(text=color4)
        hex5.config(text=color5)
        hex6.config(text=color6)
        hex7.config(text=color7)
        hex8.config(text=color8)
        hex9.config(text=color9)
        hex10.config(text=color10)

        print(color1, color2, color3, color4, color5, color6, color7, color8, color9, color10)

    except Exception as e:
        print(f"Error processing image: {e}")

Label(root, width=120, height=10, bg="#4272f9").pack()

frame = Frame(root, width=500, height=370, bg="#fff")
frame.place(x=50, y=50)

logo = PhotoImage(file="logo.png")
Label(frame, image=logo, bg="#fff").place(x=10, y=10)

Label(frame, text="Color Finder", font="Arial 16 bold", bg="white").place(x=180, y=20)

# ======= Color Set 1 =======
colors = Canvas(frame, bg="#fff", width=200, height=270, bd=0)
colors.place(x=20, y=90)

id1 = colors.create_rectangle(10, 10, 60, 60, fill="#b8255f")
id2 = colors.create_rectangle(10, 70, 60, 120, fill="#db4035")
id3 = colors.create_rectangle(10, 130, 60, 180, fill="#ff9933")
id4 = colors.create_rectangle(10, 190, 60, 240, fill="#fad000")
id5 = colors.create_rectangle(10, 250, 60, 300, fill="#afb83b")

hex1 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex1.place(x=80, y=105)

hex2 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex2.place(x=80, y=165)

hex3 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex3.place(x=80, y=225)

hex4 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex4.place(x=80, y=285)

hex5 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex5.place(x=80, y=345)

# ======= Color Set 2 =======
colors2 = Canvas(frame, bg="#fff", width=200, height=270, bd=0)
colors2.place(x=250, y=90)

id6 = colors2.create_rectangle(10, 10, 60, 60, fill="#7ecc49")
id7 = colors2.create_rectangle(10, 70, 60, 120, fill="#299438")
id8 = colors2.create_rectangle(10, 130, 60, 180, fill="#6accbc")
id9 = colors2.create_rectangle(10, 190, 60, 240, fill="#158fad")
id10 = colors2.create_rectangle(10, 250, 60, 300, fill="#14aaf5")

hex6 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex6.place(x=310, y=105)

hex7 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex7.place(x=310, y=165)

hex8 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex8.place(x=310, y=225)

hex9 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex9.place(x=310, y=285)

hex10 = Label(frame, text="", fg="#000", font="Arial 12 bold", bg="white")
hex10.place(x=310, y=345)

# Select Image
selectimage = Frame(frame, width=340, height=350, bg="#d6dee5")
selectimage.place(x=350, y=10)

f = Frame(selectimage, bd=3, bg="black", width=320, height=280, relief="groove")
f.place(x=10, y=10)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

Button(selectimage, text="Select Image", width=12, height=1, font="arial 14 bold", command=showimage).place(x=10, y=300)
Button(selectimage, text="Find Colors", width=12, height=1, font="arial 14 bold", command=Findcolor).place(x=176, y=300)

root.mainloop()
