BCM = "BCM"
BOARD = "BOARD"

#keeps track of mode, Board if True and VCM if False
isBoard = True

BCMdic = {2:3,3:5,4:7,5:29,6:31,7:26,8:24,9:21,10:19,11:23,12:32,13:33,14:8,15:10,16:36,17:11,18:12,19:35,20:38,21:40,22:15,23:16,24:18,25:22,26:37,27:13}

#set mode 
def setmode(mode):
    if (mode == BCM):
        print("GPIO mode set to BCM")
    elif (mode == BOARD):
        print("BOARD")
    else:
        print("WARNING: Invalid GPIO mode was selected")