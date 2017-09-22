class pin(object):
    pinNum = None
    bcmNum = None
    mode = None # 1 is input, 2 is output

    def __init__(self, pinNum, bcmNum):
        self.pinNum = pinNum
        self.bcmNum = bcmNum

    def setup(self, mode):
        if (self.bcmNum == None):
            print("WARNING: Pin " + self.pinNum + " is not a GPIO Pin")
        elif (mode == "IN"):
            if (self.mode == 1):
                print("WARNING: Pin " + self.pinNum + " (BCM " + self.bcmNum + ") was already set as an input")
            elif (self.mode == 2):
                self.mode = 1
                print("WARNING: Pin " + self.pinNum + "(BCM " + self.bcmNum + ") was previously set as an output")
            else:
                self.mode = 1
                print("Pin " + self.pinNum + "(BCM " + self.bcmNum + ") set as an input")
        elif (mode == "OUT"):
            if (self.mode == 1):
                self.mode == 2
                print("WARNING: Pin " + self.pinNum + "(BCM " + self.bcmNum + ") was previously set as an input")
            elif (self.mode == 2):
                print("WARNING: Pin " + self.pinNum + "(BCM " + self.bcmNum + ") was already set as an output")
            else:
                self.mode = 2
                print("Pin " + self.pinNum + "(BCM " + self.bcmNum + ") set as an output")