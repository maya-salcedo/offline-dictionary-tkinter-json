from tkinter import *
import json
import difflib
""" This is an offline dictionary where the information is stored in a .json file. 
"""

data = json.load(open('data.json'))


def definition(word):
    if word in data:
        print(word)
        return(data[word])
    elif word.lower() in data:
        return (data[word.lower()])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    else:
        try:
            alternative_word = [difflib.get_close_matches(word, data, n=1)]
            word_alternate = str(alternative_word[0]).replace("['", "").replace("']", "")
            data[word_alternate].insert(0, "Do you mean " + word_alternate + "?")
            return(data[word_alternate])
        except KeyError:
            return(["Word not found available in this dictionary. Sorry"])


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
list1.grid(row=3, column=1, rowspan=6, columnspan=7)

sby = Scrollbar(window)
sby.grid(row=2, column=7, rowspan=5)

sbx = Scrollbar(window, orient=HORIZONTAL)
sbx.grid(row=9, column=2, columnspan=4)


list1.configure(yscrollcommand=sby.set, xscrollcommand=sbx.set)

sby.configure(command=list1.yview)
sbx.configure(command=list1.xview)

window.mainloop()

print(definition('sets'))