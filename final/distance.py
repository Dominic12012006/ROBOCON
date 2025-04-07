# from errorfit import corrected_distance
import math

def calcdist(width):
    unit_length = 50/ width #returns in cm (47.2 cm is outer diameter of hoop)
    const = 950
    measured_distance = unit_length * const
    # distance=corrected_distance(measured_distance)#comment to do without errorfit
    distance=measured_distance
    distance = round(distance, 2)
    return distance

def horizontal(distance):
    height= 68#height diff from hoop to bot
    a=(distance**2)-(height**2)
    if a>=0:
        h_dist= math.sqrt(a)
    else:
        h_dist=0
    return h_dist
