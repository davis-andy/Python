import tkinter as tk
import tkinter.font as font
from tkinter import PhotoImage

# Setting variables
backgroundColor = '#F0F0F0'
buttonBGColor = '#DCDCDC'
textboxBGColor = '#FDF5E6'

# Create Window
window = tk.Tk()
window.resizable(width=False, height=False)
window.title('Calculator')
window.config(bg=backgroundColor)

# variables for display
display = tk.StringVar()
equation = ''

# Create Frames
buttonFrame = tk.Frame(window, bg=backgroundColor)

# Create Displays
displayBox = tk.Entry(window, width=38, font=('Ariel', 10), bg=textboxBGColor, textvariable=display)


# Functions for button actions
def insert_btn(text):
    global equation

    if equation == '' and text == 0:
        pass
    else:
        equation += str(text)
    display.set(equation)


def btn_equal():
    global equation

    try:
        total = eval(equation)
        display.set(total)
        equation = ''
    except:
        display.set('** ERROR **')  # division by zero, not a number, other errors
        equation = ''


def clear():
    global equation

    equation = ''
    display.set(equation)


# Button font attributes
buttonFont = font.Font(size=10)
buttonW = 8

# Button 0
button0 = tk.Button(buttonFrame, text='0', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(0))
button0['font'] = buttonFont

# Button 1
button1 = tk.Button(buttonFrame, text='1', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(1))
button1['font'] = buttonFont

# Button 2
button2 = tk.Button(buttonFrame, text='2', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(2))
button2['font'] = buttonFont

# Button 3
button3 = tk.Button(buttonFrame, text='3', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(3))
button3['font'] = buttonFont

# Button 4
button4 = tk.Button(buttonFrame, text='4', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(4))
button4['font'] = buttonFont

# Button 5
button5 = tk.Button(buttonFrame, text='5', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(5))
button5['font'] = buttonFont

# Button 6
button6 = tk.Button(buttonFrame, text='6', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(6))
button6['font'] = buttonFont

# Button 7
button7 = tk.Button(buttonFrame, text='7', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(7))
button7['font'] = buttonFont

# Button 8
button8 = tk.Button(buttonFrame, text='8', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(8))
button8['font'] = buttonFont

# Button 9
button9 = tk.Button(buttonFrame, text='9', bg=buttonBGColor, width=buttonW,
                    command=lambda: insert_btn(9))
button9['font'] = buttonFont

# Button Period
buttonPeriod = tk.Button(buttonFrame, text='.', bg=buttonBGColor, width=buttonW,
                         command=lambda: insert_btn('.'))
buttonPeriod['font'] = buttonFont

# Button Add
buttonAdd = tk.Button(buttonFrame, text='+', bg=buttonBGColor, width=buttonW,
                      command=lambda: insert_btn(' + '))
buttonAdd['font'] = buttonFont

# Button Subtract
buttonSubtract = tk.Button(buttonFrame, text='-', bg=buttonBGColor, width=buttonW,
                           command=lambda: insert_btn(' - '))
buttonSubtract['font'] = buttonFont

# Button Multiply
buttonMultiply = tk.Button(buttonFrame, text='*', bg=buttonBGColor, width=buttonW,
                           command=lambda: insert_btn(' * '))
buttonMultiply['font'] = buttonFont

# Button Divide
buttonDivide = tk.Button(buttonFrame, text='/', bg=buttonBGColor, width=buttonW,
                         command=lambda: insert_btn(' / '))
buttonDivide['font'] = buttonFont

# Button Clear
buttonClear = tk.Button(buttonFrame, text='Clear', bg=buttonBGColor, width=buttonW,
                        command=lambda: clear())
buttonClear['font'] = buttonFont

# Button Equal
buttonEqual = tk.Button(buttonFrame, text='=', bg=buttonBGColor, width=buttonW,
                        command=lambda: btn_equal())
buttonEqual['font'] = font.Font(size=13)

# Pack Display to Frame
displayBox.pack(side=tk.TOP)

# Pack Top Row Buttons to Frame
button1.grid(row=0, column=0, sticky='nesw')
button2.grid(row=0, column=1, sticky='nesw')
button3.grid(row=0, column=2, sticky='nesw')
buttonAdd.grid(row=0, column=3, sticky='nesw')
# Pack Second Row Buttons to Frame
button4.grid(row=1, column=0, sticky='nesw')
button5.grid(row=1, column=1, sticky='nesw')
button6.grid(row=1, column=2, sticky='nesw')
buttonSubtract.grid(row=1, column=3, sticky='nesw')
# Pack Third Row Buttons to Frame
button7.grid(row=2, column=0, sticky='nesw')
button8.grid(row=2, column=1, sticky='nesw')
button9.grid(row=2, column=2, sticky='nesw')
buttonMultiply.grid(row=2, column=3, sticky='nesw')
# Pack Fourth Row Buttons to Frame
button0.grid(row=3, column=0, columnspan=2, sticky='nesw')
buttonPeriod.grid(row=3, column=2, sticky='nesw')
buttonDivide.grid(row=3, column=3, sticky='nesw')
# Pack Bottom Row Buttons to Frame
buttonEqual.grid(row=4, column=0, columnspan=3, sticky='nesw')
buttonClear.grid(row=4, column=3, sticky='nesw')

# Pack Frame to Window
buttonFrame.pack(fill=tk.X)

window.mainloop()
