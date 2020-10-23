from tkinter import *
import json
import difflib
""" This is an offline dictionary where the information is stored in a .json file. 
"""

data = json.load(open('data.json'))

def definition(word):
    if word in data:
        return(data[word])
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        try:
            alternative_word = difflib.get_close_matches(word, data, n=1)
            word = alternative_word[0]
            return("Do you mean " + word + "?\n" + data[word])
        except IndexError:
            return('that is not in my dictionary. sorry')

def view_definition():
    list1.delete(0, END)
    for row in definition(word_to_find.get()):
        list1.insert(END, row)

def delete():
    t1.delete(0, END)
    list1.delete(0, END)

window = Tk()
window.wm_title("Offline Dictionary")

word_to_find = StringVar()
t1 = Entry(window, textvariable=word_to_find, width=30)
t1.grid(row=1, column=1, columnspan=4)

b1 = Button(window, text="Search", width=12, command=view_definition)
b1.grid(row=1, column=5)
b2 = Button(window, text="Clear", width=12, command=delete)
b2.grid(row=1, column=6)
list1 = Listbox(window, height=6, width=55)
list1.grid(row=2, column=1, rowspan=6, columnspan=7)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=7, rowspan=5)

#sb2 = Scrollbar(window)
#sb2.grid(row=7, column= 1, columnspan=5)

list1.configure(yscrollcommand=sb1.set)
#list1.configure(xscrollcommand=sb2.set)
sb1.configure(command=list1.yview)
#sb2.configure(command=list1.xview)

window.mainloop()

