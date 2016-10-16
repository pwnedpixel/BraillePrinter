import RPi.GPIO as GPIO
import time


#Pin setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

#Globals
topPin=23
middlePin=24
bottomPin=25
servoPin=22
servoInnerCharTime = 0.05
servoInterCharTime = 0.075
prevNum = False

def main(inputString):
    newString=""
    
    for i in range (0,(len(inputString) - 1)):
        print(inputString[i])

        if i == 0:
            if 48 <= ord(inputString[i]) <=57:
                newString += "+"
            else:
                newString += "-"
                
        newString += inputString[i]

        print(ord(inputString[i]))
            
        if 48 <= ord(inputString[i]) <=57:
            if ord(inputString[i+1]) > 57:
                newString += "-"
        else:
            if 48 <= ord(inputString[i+1]) <= 57:
                newString += "+"

    newString += inputString[len(inputString)-1]
            
    strToPrintReverse = newString[::-1]
    setZero()
    print("pins set to zero")
    for character in strToPrintReverse:
        print("printing: "+character)
        printChar(character, prevNum)
    print("DONE")
#endmain

#functions-------------------
def printChar(char, prevNumber):#prints one character
    valid=True
    charOrig=char
    char = char.lower()
    if char == '0':
        printPattern(True,True,False)
        nextColumn()
        printPattern(False, True, False)
        
    elif char == '1':
        printPattern(False,False,False)
        nextColumn()
        printPattern(True, False, False)
        
    elif char == '2':
        printPattern(False,False,False)
        nextColumn()
        printPattern(True, True, False)
        
    elif char == '3':
        printPattern(True, False, False)
        nextColumn()
        printPattern(True, False, False)
        
    elif char == '4':
        printPattern(True,True,False)
        nextColumn()
        printPattern(True, False, False)
        
    elif char == '5':
        printPattern(False,True,False)
        nextColumn()
        printPattern(True, False, False)
        
    elif char == '6':
        printPattern(True,False,False)
        nextColumn()
        printPattern(True, True, False)
        
    elif char == '7':
        printPattern(True,True,False)
        nextColumn()
        printPattern(True, True, False)
        
    elif char == '8':
        printPattern(False,True,False)
        nextColumn()
        printPattern(True, True, False)
        
    elif char == '9':
        printPattern(True,False,False)
        nextColumn()
        printPattern(False, True, False)
        
    elif char == 'a':
        printPattern(False,False,False)
        nextColumn()
        printPattern(True, False, False)
        
    elif char == 'b':
        printPattern(False,False,False)
        nextColumn()
        printPattern(True, True, False)
        
    elif char == 'c':
        printPattern(True,False,False)
        nextColumn()
        printPattern(True, False, False)
        
    elif char == 'd':
        printPattern(True,True,False)
        nextColumn()
        printPattern(True, False, False)
        
    elif char == 'e':
        printPattern(False,True,False)
        nextColumn()
        printPattern(True, False, False)
        
    elif char == 'f':
        printPattern(True,False,False)
        nextColumn()
        printPattern(True, True, False)
        
    elif char == 'g':
        printPattern(True,True,False)
        nextColumn()
        printPattern(True, True, False)
        
    elif char == 'h':
        printPattern(False,True,False)
        nextColumn()
        printPattern(True, True, False)
        
    elif char == 'i':
        printPattern(True,False,False)
        nextColumn()
        printPattern(False, True, False)
        
    elif char == 'j':
        printPattern(True,True,False)
        nextColumn()
        printPattern(False, True, False)
        
    elif char == 'k':
        printPattern(False,False,False)
        nextColumn()
        printPattern(True, False,True)
        
    elif char == 'l':
        printPattern(False,False,False)
        nextColumn()
        printPattern(True, True, True)
        
    elif char == 'm':
        printPattern(True,False,False)
        nextColumn()
        printPattern(True, False, True)
        
    elif char == 'n':
        printPattern(True,True,False)
        nextColumn()
        printPattern(True, False, True)
        
    elif char == 'o':
        printPattern(False,True,False)
        nextColumn()
        printPattern(True, False, True)
        
    elif char == 'p':
        printPattern(True,False,False)
        nextColumn()
        printPattern(True, True, True)
        
    elif char == 'q':
        printPattern(True,True,False)
        nextColumn()
        printPattern(True, True, True)
        
    elif char == 'r':
        printPattern(False,True,False)
        nextColumn()
        printPattern(True, True, True)
        
    elif char == 's':
        printPattern(True,False,False)
        nextColumn()
        printPattern(False, True, True)
        
    elif char == 't':
        printPattern(True,True,False)
        nextColumn()
        printPattern(False, True, True)
        
    elif char == 'u':
        printPattern(False,False,True)
        nextColumn()
        printPattern(True, False, True)
        
    elif char == 'v':
        printPattern(False,False,True)
        nextColumn()
        printPattern(True, True, True)
        
    elif char == 'w':
        printPattern(True,True,True)
        nextColumn()
        printPattern(False, True, False)
        
    elif char == 'x':
        printPattern(True,False,True)
        nextColumn()
        printPattern(True, False, True)
        
    elif char == 'y':
        printPattern(True,True,True)
        nextColumn()
        printPattern(True, False, True)
        
    elif char == 'z':
        printPattern(False,True,True)
        nextColumn()
        printPattern(True, False, True)
        
    elif char == '+':
        printPattern(True,True,True)
        nextColumn()
        printPattern(False,False,True)
        
    elif char == '-':
        printPattern(False,True,True)
        nextColumn()
        printPattern(False,False,False)


    else:
        valid=False
        print("Not valid Character"+char)

    if (charOrig.isupper()):
        nextCharacter()
        printPattern(False,False,True)
        nextColumn()
        printPattern(False, False, False)
        nextCharacter()
    if(valid):
         nextCharacter()


def printPattern(top,middle,bottom): #prints one column
    if(top==True):
        GPIO.output(topPin,1)
        time.sleep(0.2)
        GPIO.output(topPin,0)
        time.sleep(0.3)
        GPIO.output(topPin,1)
        time.sleep(0.2)
        GPIO.output(topPin,0)
    if(middle==True):
        GPIO.output(middlePin,1)
        time.sleep(0.2)
        GPIO.output(middlePin,0)
        time.sleep(0.3)
        GPIO.output(middlePin,1)
        time.sleep(0.2)
        GPIO.output(middlePin,0)
    if (bottom==True):
        GPIO.output(bottomPin,1)
        time.sleep(0.2)
        GPIO.output(bottomPin,0)
        time.sleep(0.3)
        GPIO.output(bottomPin,1)
        time.sleep(0.2)
        GPIO.output(bottomPin,0)

def nextColumn():#same character column spacing
    time.sleep(0.4)
    GPIO.output(servoPin,1)
    time.sleep(servoInnerCharTime) #change spacing between character columns
    GPIO.output(servoPin,0)
    time.sleep(0.25)
def nextCharacter():#inter character spacing
    time.sleep(0.25)
    GPIO.output(servoPin,1)
    time.sleep(servoInterCharTime) #change spacing between characters
    GPIO.output(servoPin,0)
    time.sleep(0.25)
def setZero():
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)

#ENd of Functions-----------------
