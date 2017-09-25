class pin(object):
    pinNum = None
    bcmNum = None
    mode = None # 1 is input, 2 is output
    val = None

    def __init__(self, pinNum, bcmNum):
        self.pinNum = pinNum
        self.bcmNum = bcmNum

    def setup(self, mode):
        if (self.bcmNum == None):
            print("WARNING: Pin " + str(self.pinNum) + " is not a GPIO Pin")
        elif (mode == "IN"):
            if (self.mode == 1):
                print("WARNING: Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") was already set as an input")
            elif (self.mode == 2):
                self.mode = 1
                print("WARNING: Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") was previously set as an output")
            else:
                self.mode = 1
                print("Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") set as an input")
        elif (mode == "OUT"):
            if (self.mode == 1):
                self.mode == 2
                print("WARNING: Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") was previously set as an input")
            elif (self.mode == 2):
                print("WARNING: Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") was already set as an output")
            else:
                self.mode = 2
                print("Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") set as an output")
                
    def setVal(self, val):
        if (self.mode != 2):
            print("WARNING: Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") must be set as an output first before assigning an output")
        else:
            self.val = val
            print("Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") set to " + str(val))
            
    def getVal(self):
        if (self.mode != 1):
            print("WARNING: Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") must be set as an input first before retrieving its value. Returning False by default")
            return False
        else:
            return self.val
            
    def clean(self):
        self.val = None
        self.mode = 0
        print("Pin " + str(self.pinNum) + " (BCM " + str(self.bcmNum) + ") cleaned up")
        