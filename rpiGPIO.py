import GPIOPin

#Consts
BCM = "BCM"
BOARD = "BOARD"
OUT = "OUT"
IN = "IN"

#status variables
isBoard = True
outputPins = []
inputPins = []

#board:BCM
BCMdic = {3:2,5:3,7:4,29:5,31:6,26:7,24:8,21:9,19:10,23:11,32:12,33:13,8:14,10:15,36:16,11:17,12:18,35:19,38:20,40:21,15:22,16:23,18:24,22:25,37:26,13:27}

pinArray = [GPIOPin.pin(i + 1, BCMdic.get(i + 1,None)) for i in xrange(40)]

#set mode 
def setmode(mode):
    global isBoard
    if (mode == BCM):
        isBoard = False
        print("GPIO mode set to BCM")
    elif (mode == BOARD):
        isBoard = True
        print("BOARD")
    else:
        print("WARNING: Invalid GPIO mode was selected")

def setup(channel, inOrOut):
    global pinArray
    if (inOrOut != "IN" and inOrOut !="OUT"):
        print("WARNING: Invalid mode was selected for pin setup")
    elif (isBoard):
        if ((channel > 40) or (channel < 1)):
            print("WARNING: Pin must be between 1 - 40")
        else:
            pinArray[channel - 1].setup(inOrOut)
    else:
        pin = next((x.pinNum for x in pinArray if x.bcmNum == channel), None)
        if (pin):
            pinArray[pin - 1].setup(inOrOut)
        else:
            print("WARNING: Invalid pin number was selected for pin setup")
    
    
        

        
