import math
g=980.665

def calcspeed(botheight,hoopheight,distance,angle):
    height=hoopheight-botheight
    numerator=g*distance*distance
    denominator=2*((distance*(math.tan(angle))-height)*(math.cos(angle)**2))
    velocitysq=numerator/denominator
    velocity=math.sqrt(velocitysq)
    return velocity

def calcrpm(botheight,hoopheight,distance,angle,radius):
    angle= math.radians(angle)
    v=calcspeed(botheight,hoopheight,distance,angle)
    rpm=(v*30)/((math.pi)*radius)
    #rpm=rpm*2
    return rpm#*3.431291748 #real to ideal ratio

# print(calcrpm(120,243,500,58.03,6.35))
#print(calcspeed(1.45,2.43,3,1.13446))
#print(calcrpm(1.45,2.43,5,0.645772,0.065))


    