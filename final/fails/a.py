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

# def range(hori_dist): #angle =58.03
#     theta_rad = math.radians(58.03)
#     v=calcspeed(120,243,hori_dist,theta_rad)
#     R = (v ** 2) * math.sin(2 * theta_rad) / g
#     return R

# r = [
#     1.3, 1.9, 1.8, 2.3, 2.35, 2.5, 2.2, 2.65, 2.55, 2.7, 3.4, 3.1, 3.35, 3.5, 3.7, 3.75,
#     3.3, 3.2, 3.6, 3.45, 3.9, 3.65, 4.1, 3.85, 4.0, 4.4, 4.5, 4.6, 4.7, 4.3, 2.25, 2.1,
#     2.6, 2.15, 2.4, 2.75, 3.0, 3.55, 3.8, 4.05, 4.25, 4.2, 4.45, 4.55, 4.9, 4.8, 5.1, 5.0,
#     5.3, 5.7, 5.4, 5.5, 5.6, 5.9, 5.8, 6.0, 6.2, 6.35, 6.3, 6.6, 6.5, 6.1
# ]
# r.sort()
# nr=[]
# h=[]
# rpm=[]
# i=1
# while i<7.0:
#     ra=round(range(i),2)
#     print(ra)
#     i+=0.01
#     print(i)
#     if ra in r:
#         nr.append(ra)
#         h.append(i)
#         rpm.append(calcrpm(120,243,i,58.03,6.35))
    
# print(nr)
# print(h)
# print(rpm)
