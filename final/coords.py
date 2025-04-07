import math

pi=math.pi
def degtorad(deg):
    rad=(deg*pi)/180
    return rad
def coordinate(distance,angle):
    #angle is angle turned by shooting mech
    angle_rad=degtorad(angle)
    sin=math.sin(angle_rad)
    cos=math.cos(angle_rad)
    x=distance*sin
    y=distance*cos
    return x,y