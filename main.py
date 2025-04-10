from  tkinter import *
import pandas as pd
from tkinter import  messagebox
from random import choice


timer = None
BACKGROUND_COLOR = "#B1DDC6"
current_word = ""
remember_words_english = []
remember_words_hindi = []

word_to_remember = { "English":[], "Hindi":[] }

#-------------------------------Save Data-------------------------------------------------------------#

def right_button_pressed():
    button_pressed = True
    show_new_card(button_pressed)


def left_button_pressed():
    button_pressed = False
    show_new_card(button_pressed)

def save_data():

    is_saving = messagebox.askyesno(title="Flashy", message="Do you want to save the progress?")
    window.destroy()
    if is_saving:
        word_to_remember["English"] = english_words.copy()
        word_to_remember["Hindi"] = hindi_words.copy()
        new_data = pd.DataFrame(word_to_remember)
        new_data.to_csv("data/word_to_remember.csv")
        # print(new_data)

#-------------------------------Search Words---------------------------------------------------------#

try:
    data = pd.read_csv("data/word_to_remember.csv")
    print("old data")
except FileNotFoundError:
    data = pd.read_csv("data/english_words.csv")
    print("new data")
finally:
    english_words = data.English.to_list()
    hindi_words = data.Hindi.to_list()


def show_new_card(button_state):
    global  timer, current_word

    try:
        if button_state:
            english_words.remove(current_word)
            remember_words_english.append(current_word)

            hindi_words.remove(data.Hindi[data.English == current_word].iloc[0])
            remember_words_hindi.append(data.Hindi[data.English == current_word].iloc[0])
        # print(f"{len(english_words)}\n{len(hindi_words)}")
    except ValueError:
        pass

    current_word = choice(data.English)
    canvas.itemconfig(language_text, text="English", fill= "Black")
    canvas.itemconfig(word_text, text=current_word, fill= "Black")


    # print(word_to_remember)
    canvas.itemconfig(image, image=card_front_image)

    if timer:
        window.after_cancel(timer)

    timer = window.after(3000, flip_card, data)


#--------------------------------Flip the cards------------------------------------------------------#

def flip_card(data):
    global  current_word

    canvas.itemconfig(image, image=card_back_image)
    hindi_word = data.Hindi[data.English == current_word].iloc[0]

    canvas.itemconfig(language_text, text="Hindi", fill= "White")
    canvas.itemconfig(word_text, text= hindi_word, fill= "White")


#------------------------UI Setup--------------------------------------------------------------------#

#Game window
window = Tk()
window.title("Flashy")
window.resizable(FALSE,FALSE)
window.config(padx= 50, pady= 50, bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400, 263, image=card_front_image)

word_text = canvas.create_text(400, 263, text="word",font=("Arial", 60, "bold"))
language_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.grid(column= 0, row= 0, columnspan=2)

#Buttons
## Right Button
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image= right_button_img, bg= BACKGROUND_COLOR, highlightthickness=0,command= right_button_pressed)
right_button.grid(column= 0, row= 1,)

## Wrong Button
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image= wrong_button_img, bg= BACKGROUND_COLOR, highlightthickness=0, command= left_button_pressed)
wrong_button.grid(column= 1, row= 1,)

window.protocol("WM_DELETE_WINDOW", save_data)

# To hold the window
window.mainloop()




