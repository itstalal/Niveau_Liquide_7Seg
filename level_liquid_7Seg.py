from gpiozero import LED, Button
from time import sleep
from signal import pause
#A=8,B=9,C=10,D=11,E=12,F=13,G=17
sega = LED(8)
segb = LED(9)
segc = LED(10)
segd = LED(11)
sege = LED(12)
segf = LED(13)
segg = LED(17)
led_red = LED(26)
led_green = LED(7)

#Alarm zones
zone1 = Button(22)
zone2 = Button(5)
zone3 = Button(6)
zone4 = Button(19)

#False= unarmed, True= armed
systemStatus = 0

def show0():
    #0
    sega.off()
    segb.off()
    segc.off()
    segd.off()
    sege.off()
    segf.off()
    segg.on()

def show1():
    #1
    sega.on()
    segb.off()
    segc.off()
    segd.on()
    sege.on()
    segf.on()
    segg.on()

def show2():
    #2
    sega.off()
    segb.off()
    segc.on()
    segd.off()
    sege.off()
    segf.on()
    segg.off()  
    
def show3():
    #3
    sega.off()
    segb.off()
    segc.off()
    segd.off()
    sege.on()
    segf.on()
    segg.off() 

def show4():
    #4
    sega.on()
    segb.off()
    segc.off()
    segd.on()
    sege.on()
    segf.off()
    segg.off() 

def show5():
    #5
    sega.off()
    segb.on()
    segc.off()
    segd.off()
    sege.on()
    segf.off()
    segg.off()  

def show6():
    #6
    sega.off()
    segb.on()
    segc.off()
    segd.off()
    sege.off()
    segf.off()
    segg.off() 

def show7():
    #7
    sega.off()
    segb.off()
    segc.off()
    segd.on()
    sege.on()
    segf.on()
    segg.on()     

def show8():
    #8
    sega.off()
    segb.off()
    segc.off()
    segd.off()
    sege.off()
    segf.off()
    segg.off()  

def show9():
    #9
    sega.off()
    segb.off()
    segc.off()
    segd.on()
    sege.on()
    segf.off()
    segg.off()    

def showA():
    #A
    sega.off()
    segb.off()
    segc.off()
    segd.on()
    sege.off()
    segf.off()
    segg.off()

def showL():
    sega.on()
    segb.on()
    segc.on()
    segd.off()
    sege.off()
    segf.off()
    segg.on()

def showH():
    sega.on()
    segb.off()
    segc.off()
    segd.on()
    sege.off()
    segf.off()
    segg.off()


def LedTurnOn(led):
    led.on()
       
def LedTurnOff(led):
    led.off()
    
     
LedTurnOn(led_green)
LedTurnOff(led_red)
showL()

def tresh_zone1():
    global systemStatus 
    if zone1.is_pressed and not zone2.is_pressed and not zone3.is_pressed and not zone4.ispressed:
        show1()
        systemStatus = 1
        LedTurnOn(led_green)
        LedTurnOff(led_red)

def tresh_zone2():
    global systemStatus
    if zone1.is_pressed and zone2.is_pressed and not zone3.is_pressed and not zone4.ispressed:
        show2()
        systemStatus = 2
        LedTurnOn(led_green)
        LedTurnOff(led_red)

def tresh_zone3():
    global systemStatus
    if zone1.is_pressed and zone2.is_pressed and zone3.is_pressed and not zone4.ispressed:
        show3()
        systemStatus = 3
        LedTurnOn(led_green)
        LedTurnOff(led_red)

def tresh_zone4():
    
    global systemStatus
    if zone1.is_pressed and zone2.is_pressed and zone3.is_pressed and zone4.ispressed:
        showH()
        systemStatus = 4
        LedTurnOn(led_red)
        LedTurnOff(led_green)

def tresh_NoZone():
    global systemStatus
    showL()
    systemStatus = 0
    LedTurnOn(led_green)
    LedTurnOff(led_red) 
                        
        
def UpdateSysStatus():
    global systemStatus 
    if systemStatus==0:
        tresh_zone1
    elif systemStatus == 1:
        tresh_zone2
    elif systemStatus == 2:
        tresh_zone3
    elif systemStatus == 3:
        tresh_zone4
    else:
        tresh_NoZone        

              
zones = [zone1,zone2,zone3,zone4]
for zone in zones:
    zone.when_pressed=UpdateSysStatus
    zone.when_released=UpdateSysStatus


pause()