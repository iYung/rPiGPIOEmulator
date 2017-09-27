import GPIOPin
from threading import Thread
import time

#Consts
BCM = "BCM"
BOARD = "BOARD"
OUT = "OUT"
IN = "IN"
HIGH = True
LOW = False

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
        print("GPIO mode set to BOARD")
    else:
        print("ERROR: Invalid GPIO mode was selected")

def setup(channels, inOrOut, val=None):
    global pinArray
    if isinstance(channels, int):
        pinNums = [channels]
    else:
        pinNums = channels
    for pinNum in pinNums:
        if (inOrOut != "IN" and inOrOut !="OUT"):
            print("ERROR: Invalid mode was selected for pin setup")
        elif (val != None and val != True and val != False):
            print("ERROR: Invalid intial state was selected for pin setup")
        elif (isBoard):
            if ((pinNum > 40) or (pinNum < 1)):
                print("ERROR: Setup pin must be between 1 - 40")
            else:
                pinArray[pinNum - 1].setup(inOrOut)
                if (val != None):
                    output(pinNum, val)
        else:
            pin = next((x.pinNum for x in pinArray if x.bcmNum == pinNum), None)
            if (pin):
                pinArray[pin - 1].setup(inOrOut)
                if (val != None):
                    output(pinNum, val)
            else:
                print("ERROR: Invalid pin number was selected for pin setup")

def output(channels, values):
    global pinArray
    if isinstance(channels, int):
        pinNums = [channels]
    else:
        pinNums = channels
    if isinstance(values, (int,bool)):
        vals = [values]
    else:
        vals = values
    for i in xrange(len(pinNums)):
        val = vals[i % len(vals)]
        if (val != True and val != False):
            print("ERROR: Invalid output value was selected")
        elif (isBoard):
            if ((pinNums[i] > 40) or (pinNums[i] < 1)):
                print("ERROR: Output pin must be between 1 - 40")
            else:
                pinArray[pinNums[i] - 1].setVal(val)
        else:
            pin = next((x.pinNum for x in pinArray if x.bcmNum == pinNums[i]), None)
            if (pin):
                pinArray[pin - 1].setVal(val)
            else:
                print("ERROR: Invalid pin number was selected for pin output")

def input(channel):
    global pinArray
    if (isBoard):
        if ((channel > 40) or (channel < 1)):
            print("ERROR: Input pin must be between 1 - 40")
        else:
            return pinArray[channel - 1].getVal()
    else:
        pin = next((x.pinNum for x in pinArray if x.bcmNum == channel), None)
        if (pin):
            return pinArray[pin - 1].getVal()
        else:
            print("ERROR: Invalid pin number was selected for pin input")
            
def cleanup(channels=None):
    global pinArray
    global isBoard
    if isinstance(channels, int):
        pinNums = [channels]
    else:
        pinNums = channels
    if (channels == None):
        print("Cleaned all channels and the pin numbering system")
        pinArray = [GPIOPin.pin(i + 1, BCMdic.get(i + 1,None)) for i in xrange(40)]
        isBoard = None
    elif (isBoard != None):
        for pinNum in pinNums:
            if (isBoard):
                if ((pinNum > 40) or (pinNum < 1)):
                    print("ERROR: Cleanup pin must be between 1 - 40")
                else:
                    pinArray[pinNum - 1].clean()
            else:
                pin = next((x.pinNum for x in pinArray if x.bcmNum == pinNum), None)
                if (pin):
                    pinArray[pin - 1].clean()
                else:
                    print("ERROR: Invalid pin number was selected for pin cleanup")
                    
class PWM(object):
    pinIndex = None
    pwmPeriod = None
    dc = None
    on = False
        
    def __init__(self, channel, freq):
        global pinArray
        global isBoard
        if (isBoard):
            if ((channel > 40) or (channel < 1)):
                print("ERROR: PWM pin must be between 1 - 40")
            else:
                self.pinIndex = channel - 1
                self.pwmFreq = 1 / freq
        else:
            pin = next((x.pinNum for x in pinArray if x.bcmNum == channel), None)
            if (pin):
                self.pinIndex = pin
                self.pwmPeriod = 1 / freq
            else:
                print("ERROR: Invalid pin number was selected for PWM")
            
    def start(self, dc):
        try:
            self.dc = float(dc)
            t = Thread(target = self.__runPWM)
            t.daemon = True
            t.start()
        except ValueError:
            print("ERROR: DC must be a value from 0 - 100")
        
    def __runPWM(self):
        global pinArray
        self.on = True
        while (self.on):
            pinArray[self.pinIndex].setVal(HIGH)
            time.sleep(self.pwmFreq * self.dc)
            pinArray[self.pinIndex].setVal(LOW)
            time.sleep(self.pwmFreq * (1 - self.dc))
    
    def stop(self):
        self.on = False
        print("Stopping PWM")