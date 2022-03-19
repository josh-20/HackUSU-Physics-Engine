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