from machine import Pin, UART

#CLASSES:
#CLASS TO CONTROL PISTONS THROUGH RELAYS
class RelayControl:
    def __init__(self,relay=2):
        self.relay=Pin(relay,Pin.OUT)
    def on(self):
        self.relay.value(1)
    def off(self):
        self.relay.value(0)


#CLASS TO SETUP AND RECIEVE BLUETOOTH SIGNAL FROM HC-05 MODULE
class Bluetooth:
    def __init__(self,uart_num=0,baudrate=9600):
        self.signal=UART(uart_num,baudrate)
    def getsignal(self):
        if self.signal.any():
            return self.signal.read(1).decode('utf-8')
        return None


#METHODS TO CONTROL:
#TO CONTROL UP AND DOWN MOTION OF SYSTEM
def armcontrol(blue,relay):
    if blue.lower()=='u':
        relay.off()
    elif blue.lower()=='d':
        relay.on()

#TO CONTROL OPENING AND CLOSING OF CLAW
def clawcontrol(blue,relay):
    if blue.lower()=='p':
        relay.on()
    elif blue.lower()=='q':
        relay.off()

#OVERALL CONTROL OF THE ENTIRE SYSTEM INCLUDING CLAW AND ARM USING BLUETOOTH SIGNAL
def control(blue,clawrelay,armrelay):
    armcontrol(blue,armrelay)
    clawcontrol(blue,clawrelay)
    

#INITIALIZATION OF OBJECTS:
armpiston=RelayControl(8)#for up down motion
clawpiston=RelayControl(7)#for claw open close
signal=Bluetooth()#to recieve bluetooth signals from phone bluetooth terminal app -> "Bluetooth Electronics"


#MAIN PROGRAM
while True:
    bval=signal.getsignal()
    #if bval exists
    if bval:
        control(bval,clawpiston.relay,armpiston.relay)
        
        
