from math import *

# Adds 2 tuples
def Tadd(a, b):
    c = []

    for i in range(len(a)):
        c.append(a[i] + b[i])

    return tuple(c)


# Divides a tuple by a float
def TdivF(a, f):
    c = []
    for i in range(len(a)):
        c.append(a[i]/f)

    return tuple(c)


# distance between 2 (x, y) tuples
def distance(a, b):
    c = []
    for i in range(len(a)):
        c.append((a[i]**2 + b[i]**2)**.5)

    return tuple(c)


def scalar_mult(a, b):
    return tuple([a * b[0], a * b[1]])


def add_angle(angle, vector):
    angle += get_angle(vector, (1, 0))
    return tuple([cos(angle), sin(angle)])


def dot_product(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1]


def get_angle(vector1, vector2):
    return acos(dot_product(vector1, vector2))
