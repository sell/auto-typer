import pyautogui as p
import time as t
import random
from tkinter import *

words = []

printing = False
count_word = 0
seconds = 10


def timer_label_function():
    global seconds
    if printing:
        if seconds == 0:
            timer_label['text'] = f"00:00:00"
        else:
            seconds -= 1
            print(seconds)
            timer_label['text'] = f"00:00:0{seconds}"

    if not printing:
        seconds = 10
        timer_label['text'] = f"00:00:10"

    root.after(int(0.1 * 60 * 100), timer_label_function)


test_array = []


def print_random():
    # rand_word = random.choice(words)
    rand_word = e.get()
    global test_array
    settings_label['text'] = f"Time Delay: {custom_time.get()} Minute(s), Word(s): {rand_word}"
    if printing:
        test_array.append(e.get())
        rand_word = random.choice(test_array)
        print(test_array)
        global count_word
        p.typewrite(rand_word + "\n", 0.1)
        count_word += 1

        word_label['text'] = "Word Sent: " + str(rand_word)
        wcount['text'] = "Total Words Sent: " + str(count_word)

    root.after(int(float(custom_time.get()) * 60 * 1000), print_random)


# Function for when typer is stopped

def stopTyper():
    global printing
    printing = False
    print(printing)
    start_label['text'] = "Auto Typer Ended!"


# End of function for when typer is stopped

# Start of typer function

def startTyper():
    global printing
    printing = True
    print(printing)
    # p.typewrite("Auto Typer Started", 0.1)
    start_label['text'] = "Auto Typer Started!"


# End of start typer function


# for copy paste for text

def focusText(event):
    btc_label.config(state='normal')
    btc_label.focus()
    btc_label.config(state='disabled')


# End of btc copy and paste

root = Tk()
root.title('Terrible Auto Typer!')
root.geometry("500x500")
root.configure(background='#333')

# Title Name, main top label

name_label = Label(root, text="Terrible Auto Typer")
name_label.place(relx=0.5, rely=0.05, anchor='n')

# End of Title Label

# Start Label, shows when label is started and ended

start_label = Label(root, text="Start Auto Typer")
start_label.place(relx=0.5, anchor='n', rely=0.1)

# End of start and end label

# Count Down Timer Label

timer_label = Label(root, text="00:00:00")
timer_label.place(relx=0.5, anchor='n', rely=0.15)

# End of count down timer label

# Words Users wants to be sent label

entry_text = Label(root, text="Enter a word you want to send:")
entry_text.place(relx=0.5, anchor='n', rely=0.2)

# End of users word collection label

# Input for the user word

e = Entry(root, width=25)
e.place(relx=0.5, anchor='n', rely=0.25)

# End of input for users word

# Getting custom time of users input

custom_time_text = Label(root, text="Enter a delay time in mins (1):")
custom_time_text.place(relx=0.5, anchor='n', rely=0.35)
custom_time = StringVar()
time_custom = Entry(root, width=25, text=custom_time)
time_custom.place(relx=0.5, anchor='n', rely=0.4)

custom_time.set(0.1)
ctime = custom_time.get()

# End Of Custom Time

# Current Words Being typed label

word_label = Label(root, text="Current Word Being Typed")
word_label.place(relx=0.5, anchor='n', rely=0.5)

# End of current words

# Word Counter

wcount = Label(root, text="Word Counter")
wcount.place(relx=0.5, anchor='n', rely=0.55)

# End of Word Counter

# Settings Label (shows delay and words)

settings_label = Label(root, text=f"Time Delay: 1 Minute, Word(s): ")
settings_label.place(relx=0.5, anchor='n', rely=0.60)

# End of Settings Label

# Start and Stop Button

startButton = Button(root, text="Start", command=startTyper)
startButton.place(relx=0.35, anchor='n', rely=0.70, relwidth=0.2)

stopButton = Button(root, text="Stop", command=stopTyper)
stopButton.place(relx=0.65, anchor='n', rely=0.70, relwidth=0.2)

# End of start and stop button

# Donate Label

donate_label = Label(root, text="Want to support?")
donate_label.place(relx=0.5, anchor='n', rely=0.8)

# End of Donate Label

# BTC LABEL, TO DISPLAY BITCOIN

btc_label = Text(root, height=1, borderwidth=0, width=48)
btc_label.insert(1.0, "BTC ADDRESS: 12fMcxiRugD9pNambV1ZvNhT9uQVSUE7Hf")
btc_label.place(relx=0.5, anchor='n', rely=0.9)

btc_label.configure(state="disabled")

btc_label.bind('<Button-1>', focusText)

# End Of Bitcoin

# Runs these function
root.after(int(0.1 * 60 * 100), timer_label_function)
root.after(int(float(custom_time.get()) * 60 * 1000), print_random)
root.mainloop()
