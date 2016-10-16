import printString
from tkinter import *

root= Tk() #Create the window
#windowS setup
root.title("Braille Printer")
root.geometry("400x300")




#Event Handlers
def printTextBoxContent():
    printString.main(textField.get())


#window elements
app = Frame(root)
app.grid()
label = Label(app, text = "What would you like to print?")
label.grid(row=0)
textField = Entry(app)
textField.grid(row = 1, column=0,columnspan=2, sticky=W)
prBoxBtn = Button(app, text = "Print Textbox content")
prBoxBtn.grid(row=1,column=2)
prBoxBtn["command"] = printTextBoxContent
openFileBtn = Button(app, text = "Open File")
openFileBtn.grid(row=2)





root.mainloop()
