from tkinter import *
from tkinter import messagebox

morse = {' ': '/ ',
         '!': '-.-.-- ',
         '(': '-.--. ',
         ')': '-.--.- ',
         ',': '--..-- ',
         '-': '-....- ',
         '.': '.-.-.- ',
         '/': '-..-. ',
         '0': '----- ',
         '1': '.---- ',
         '2': '..--- ',
         '3': '...-- ',
         '4': '....- ',
         '5': '..... ',
         '6': '-.... ',
         '7': '--... ',
         '8': '---.. ',
         '9': '----. ',
         '?': '..--.. ',
         '@': '.--.-. ',
         'a': '.- ',
         'b': '-... ',
         'c': '-.-. ',
         'd': '-.. ',
         'e': '. ',
         'f': '..-. ',
         'g': '--. ',
         'h': '.... ',
         'i': '.. ',
         'j': '.--- ',
         'k': '-.- ',
         'l': '.-.. ',
         'm': '-- ',
         'n': '-. ',
         'o': '--- ',
         'p': '.--. ',
         'q': '--.- ',
         'r': '.-. ',
         's': '... ',
         't': '- ',
         'u': '..- ',
         'v': '...- ',
         'w': '.-- ',
         'x': '-..- ',
         'y': '-.-- ',
         'z': '--.. '
         }


def convert():
    output_text.delete('1.0', END)
    text = input_text.get("1.0", 'end-1c').lower()
    if radio_used() == 1:
        table = text.maketrans(morse)
        translated_text = text.translate(table)
        output_text.insert('1.0', translated_text)
    else:
        reversed_morse = {v.strip(): k for k, v in morse.items()}
        letters = text.split()
        try:
            sentence = "".join(reversed_morse.get(letter.strip()) for letter in letters).upper()
        except TypeError:
            messagebox.showwarning(title="Invalid data",
                                   message="With the Morse Code option, you can only enter valid Morse Сode.")
        else:
            output_text.insert('1.0', sentence)


def radio_used():
    return int(radio_state.get())


def clear():
    input_text.delete('1.0', END)
    output_text.delete('1.0', END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Morse Code")
window.minsize(width=800, height=550)
window.maxsize(width=800, height=550)
window.config(padx=15, pady=30)

window_height = 550
window_width = 800
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate-80}")


canvas = Canvas(width=300, height=150)
image = PhotoImage(file='logo.png')
canvas.create_image(150, 75, image=image)
canvas.grid(columnspan=3, row=0)

input_label = Label(text="Input:", font=("arial", 12))
input_label.grid(column=1, row=1, pady=3, sticky=W)
input_text = Text(width=71, height=5, font=("arial", 12))
input_text.focus()
input_text.grid(column=1, row=2, sticky=W)

output_label = Label(text="Output:", font=("arial", 12))
output_label.grid(column=1, row=5, pady=3, sticky=W)
output_text = Text(width=53, height=5, font=("arial", 16))
output_text.grid(column=1, row=6, sticky=W)

add_button = Button(text="Convert", width=68, command=convert)
add_button.grid(column=1, row=4, pady=10, sticky=W)

clear_button = Button(text="Clear", width=20, command=clear)
clear_button.grid(column=1, row=4, pady=10, sticky=E)

radio_state = IntVar()
radio_state.set(1)
radio_button1 = Radiobutton(window, text="Text", variable=radio_state, value=1, command=radio_used)
radio_button1.grid(column=2, row=1, rowspan=2, sticky=W, padx=5)
radio_button2 = Radiobutton(window, text="Morse Code", variable=radio_state, value=2, command=radio_used)
radio_button2.grid(column=2, row=2, rowspan=3, sticky=W, padx=5)

window.mainloop()
