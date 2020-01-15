class GenerateCodeword:
    def __init__(self):
        self.x = 0x000

    def parseBase(self,direction):
        self.x = 0x000
        if direction == 'F':
            self.x|=0x40
        elif direction == 'B':
            self.x|=0x50
        elif direction == 'L':
            self.x|=0x60
        elif direction == 'R':
            self.x|=0x70
        return self.x

    def parseCamera(self,cameraNum):
        self.x = 0x100
        if cameraNum == 1:
            self.x|=0x00
        if cameraNum == 2:
            self.x|=0x10
        return self.x

    def parseArm(self,direction):
        self.x = 0x200
        if direction=='L':
            self.x|=0x020
        if direction=='R':
            self.x|=0x030
        return self.x

    def parseActuator1(self,state):
        self.x = 0x300
        if state=='E':
            self.x|=0x20
        if state=='R':
            self.x|=0x30
        return self.x

    def parseActuator2(self,state):
        self.x = 0x400
        if state=='E':
            self.x|=0x20
        if state=='R':
            self.x|=0x30
        return self.x

    def parseActuator3(self,state):
        self.x = 0x500
        if state=='E':
            self.x|=0x20
        if state=='R':
            self.x|=0x30
        return self.x

    def parseGripperDir(self,direction):
        self.x = 0x600
        if direction=='L':
            self.x|=0x20
        if direction=='R':
            self.x|=0x30
        return self.x

    def parseGripperState(self,state):
        self.x = 0x700
        if state=='O':
            self.x|=0x20
        if state=='C':
            self.x|=0x30
        return self.x

    def parseSensors(self):
        self.x = 0x800
        return self.x

    def parseMagnetometerRequest(self):
        self.x = 0x900
        return self.x

    def parseGpsCompassRequest(self):
        self.x = 0xa00
        return self.x

    def parseSoilSetup(self,step):
        self.x = 0xb00
        if step=='augerUp':
            self.x|=0x10
        if step=='augerDown':
            self.x|=0x20
        if step=='soilCollect':
            self.x|=0x30
        return self.x 

    def parseAutonomousCommands(self,command):
        self.x = 0xc00
        if command=='startAutonomous':
            self.x|=0x00
        if command=='goLeft':
            self.x|=0x10
        if command=='goRight':
            self.x|=0x20
        if command=='stop':
            self.x|=0x30
        return self.x 

    def parseAddLatitude(self,lattitude):
        self.x= 0xd00
        # attach latitude to end of prefix
        return self.x


    def parseAddLongitude(self,longitude):
        self.x= 0xe00
        # attach longitude to end of prefix
        # print(type(self.x))
        return self.x


    def parsePWM(self,state):
        self.x = 0xf00
        if state=='U':
            self.x|=0x20
        if state=='D':
            self.x|=0x30
        return self.x

"""
Reference:
https://github.com/technocratsroboticsvitc/rover/blob/master/BaseRoverComm/sockets/test/generateCommand.py
The above link is a work of Shreyansh Saha and Dhrubanka Dutta
"""