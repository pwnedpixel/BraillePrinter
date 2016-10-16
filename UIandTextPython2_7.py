import printString
from Tkinter import *
from tkFileDialog import askopenfilename
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

root= Tk() #Create the window
#windowS setup
root.title("Braille Printer")
root.geometry("400x100")

#Event Handlers
def printTextBoxContent():
    print("printing textbox content...")
    printString.main(textField.get())

def openFile():
    print("Chose File...")
    filepath = askopenfilename()
    print(filepath)
    if (".txt" in filepath):
        print("text found")
        with open(filepath,'r') as myfile:
            data = myfile.read().replace('\n',' ')
        print(data)
        parsedText=data
        gottenText["text"]="text to print: "+data
        printString.main(data)
    elif (".jpg" in filepath) or (".png" in filepath):
        print("image text: ")
        print(pytesseract.image_to_string(Image.open(filepath)))
        printString.main(pytesseract.image_to_string(Image.open(filepath)))
        print("end of image processing")
    else:
        print("accepted files are: *.txt, *.png and *.jpeg")


#window elements----------------------------
app = Frame(root)
app.grid()
#label
label = Label(app, text = "What would you like to print?")
label.grid(row=0)
#textfield
textField = Entry(app)
textField.grid(row = 1, column=0,columnspan=2, sticky=W)
#printTextButton
prBoxBtn = Button(app, text = "Print Textbox content")
prBoxBtn.grid(row=1,column=2)
prBoxBtn["command"] = printTextBoxContent
#openFileButton
openFileBtn = Button(app, text = "Open Text or image file")
openFileBtn.grid(row=2,column=0)
openFileBtn["command"] = openFile
#retreived text label
gottenText = Label(app, text = "")
gottenText.grid(row=2,column=2)
#printDiscoveredString
#printgottenBtn = Button(app,text="print image/file text")
#printgottenBtn.grid(column=0,row=3);
#printgottenBtn["command"] = printGottenText





root.mainloop()
