from  tkinter import *
import pandas as pd
from random import choice


timer = None
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
words_to_learn = {}

#-------------------------------Search Words---------------------------------------------------------#

try:
    data = pd.read_csv("data/word_to_remember.csv")
    print("old data")
except FileNotFoundError:
    original_data = pd.read_csv("data/english_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
    print("new data")
else:
    words_to_learn = data.to_dict(orient="records")

def show_new_card():

    global  timer, current_word
    if timer:
        window.after_cancel(timer)
    current_word = choice(words_to_learn)
    canvas.itemconfig(language_text, text="English", fill= "Black")
    canvas.itemconfig(word_text, text=current_word["English"], fill= "Black")
    canvas.itemconfig(image, image=card_front_image)
    timer = window.after(3000, flip_card)


#--------------------------------Flip the cards------------------------------------------------------#

def flip_card():

    canvas.itemconfig(image, image=card_back_image)
    hindi_word = current_word["Hindi"]
    canvas.itemconfig(language_text, text="Hindi", fill= "White")
    canvas.itemconfig(word_text, text= hindi_word, fill= "White")

#-------------------------------Save Data-------------------------------------------------------------#

def is_remember():
    words_to_learn.remove(current_word)
    show_new_card()
    new_data = pd.DataFrame(words_to_learn)
    new_data.to_csv("data/word_to_remember.csv", index=False)


#------------------------UI Setup--------------------------------------------------------------------#
 
#Game window
window = Tk()
window.title("Flashy")
window.resizable(FALSE,FALSE)
window.config(padx= 50, pady= 50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

#Canvas
canvas = Canvas(width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=card_front_image)

word_text = canvas.create_text(400, 263, text="",font=("Arial", 60, "bold"))
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas.grid(column= 0, row= 0, columnspan=2)

#Buttons
## Right Button
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image= right_button_img, highlightthickness=0,command= is_remember)
right_button.grid(column= 0, row= 1,)

## Wrong Button
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image= wrong_button_img, highlightthickness=0, command= show_new_card)
wrong_button.grid(column= 1, row= 1,)

show_new_card()

# To hold the window
window.mainloop()




