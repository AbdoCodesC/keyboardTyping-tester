import tkinter.messagebox
from tkinter import *
from WordsOnly import word_list
import random

TITLE_FONT = "Arial"
TITLE = "#00ADB5"
WORD_FONT = "Times New Roman"
WORD = "#EEEEEE"
BACKGROUND = "#222831"
RANDOM_WORD = random.choice(word_list)
WORDS_TYPED = 0
ERRORS = 0
SCORE = 0

def reset_game():
    """Reset all game variables"""
    global ERRORS, SCORE, WORDS_TYPED, RANDOM_WORD
    ERRORS = 0
    SCORE = 0
    WORDS_TYPED = 0
    RANDOM_WORD = random.choice(word_list)
    error_label.config(text=f"Errors: {ERRORS}/10")
    score_label.config(text=f"Score: {SCORE}")
    word_label.config(text=f"{RANDOM_WORD}", bg=BACKGROUND)
    text_entry.delete(0, END)

def game_over():
    """Handle game over state"""
    response = tkinter.messagebox.askquestion("Game Over", 
        f"Final Score: {SCORE}\nWould you like to play again?")
    if response == 'yes':
        reset_game()
    else:
        root.quit()

def change_word():
    """Go to the next word"""
    global RANDOM_WORD, SCORE
    RANDOM_WORD = random.choice(word_list)
    text_entry.delete(0, END)
    word_label.config(text=f"{RANDOM_WORD}")
    SCORE += 1
    score_label.config(text=f"Score: {SCORE}")

def callback(sv):
    """To verify if you've typed in the right word and to calculate your final result"""
    global RANDOM_WORD, WORDS_TYPED, ERRORS
    current_letter = (len(sv.get()) - 1)

    if sv.get() == RANDOM_WORD:
        WORDS_TYPED += len(RANDOM_WORD)
        change_word()
    elif sv.get():
        try:
            if sv.get()[current_letter] != RANDOM_WORD[current_letter]:
                word_label.config(text=f"{RANDOM_WORD}", bg="Red")
                ERRORS += 1
                error_label.config(text=f"Errors: {ERRORS}/10")
                if ERRORS >= 10:
                    game_over()
            else:
                word_label.config(text=f"{RANDOM_WORD}", bg=BACKGROUND)
        except IndexError:
            word_label.config(text=f"{RANDOM_WORD}", bg="Red")
            ERRORS += 1
            error_label.config(text=f"Errors: {ERRORS}/10")
            if ERRORS >= 10:
                game_over()

root = Tk()
root.title('Abdo: Typing Test')
root.config(padx=25, pady=25, bg=BACKGROUND)
root.geometry("750x500")

title_label = Label(text="Typing Test", font=(TITLE_FONT, 54, "bold"), fg=TITLE, bg=BACKGROUND)
title_label.place(relx=0.5, rely=0.1, anchor=CENTER)

# Add error counter
error_label = Label(text=f"Errors: {ERRORS}/10", font=(WORD_FONT, 20), fg=WORD, bg=BACKGROUND)
error_label.place(relx=0.1, rely=0.2, anchor=W)

# Add score counter
score_label = Label(text=f"Score: {SCORE}", font=(WORD_FONT, 20), fg=WORD, bg=BACKGROUND)
score_label.place(relx=0.9, rely=0.2, anchor=E)

word_label = Label(text=f"{RANDOM_WORD}", font=(WORD_FONT, 44), fg=WORD, bg=BACKGROUND)
word_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Callback to check if you're typing in the right characters
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
text_entry = Entry(root, width=15, font=(f"{WORD_FONT}", 24), textvariable=sv)
text_entry.place(relx=0.5, rely=0.7, anchor=CENTER)
text_entry.focus()

# Add reset button
reset_button = Button(text="Reset", font=(WORD_FONT, 16), command=reset_game)
reset_button.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()