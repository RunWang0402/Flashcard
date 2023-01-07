BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG=("Ariel",40,"italic")
FONT=("Ariel",60,"bold")
from tkinter import *
import pandas
import random

data_frame=pandas.read_csv("data/french_words.csv")
data=data_frame.to_dict("records")

random_pick=random.choice(data)
front=1

def display_word():
    global random_pick
    random_pick=random.choice(data)
    canvas.itemconfig(french, text=random_pick["French"])

#Window
window=Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.title("Flashy ;)")


#Canvas
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
flash_card_front=PhotoImage(file="images/card_front.png")
flash_card_back=PhotoImage(file="images/card_back.png")
background=canvas.create_image(400,263,image=flash_card_front)
language=canvas.create_text(400,150,text="French",fill="black",font=FONT_LANG)
french=canvas.create_text(400,263,text="trouve",fill="black",font=FONT)
canvas.grid(column=0,row=0,columnspan=2)

#Yes Button
yes_button_img=PhotoImage(file="images/right.png")
yes_button=Button(image=yes_button_img,highlightthickness=0,bg=BACKGROUND_COLOR,command=display_word)
yes_button.grid(column=0,row=1)


#NO Button
no_img=PhotoImage(file="images/wrong.png")
no_button=Button(image=no_img,highlightthickness=0,bg=BACKGROUND_COLOR,command=display_word)
no_button.grid(column=1,row=1)

#data

#change
def English():
    global random_pick
    canvas.itemconfig(language,text="English",fill="white")
    canvas.itemconfig(background,image=flash_card_back)
    canvas.itemconfig(french,text=random_pick["English"],fill="white")
    window.after(3000,French)


def French():
    global random_pick
    random_pick=random.choice(data)
    canvas.itemconfig(language,text="French",fill="black")
    canvas.itemconfig(background,image=flash_card_front)
    canvas.itemconfig(french,text=random_pick["French"],fill="black")
    window.after(3000,English)


window.after(3000,English)



window.mainloop()