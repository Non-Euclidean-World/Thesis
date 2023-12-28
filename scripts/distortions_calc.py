import math
from itertools import pairwise
import numpy as np


def port(p):
    d = np.linalg.norm(p)
    if d < 0.000001:
        return np.array([0, 0, 1])
    return np.concatenate([p / d * math.sin(d), [math.cos(d)]])


def dist(p1, p2):
    return np.linalg.norm(p1 - p2)


def sphericalDist(p1, p2):
    return 2 * math.asin(dist(p1, p2) / 2)


def translation(q, p, g):
    return p + 2 * p[2] * q - (p[2] + np.dot(p, q)) / (1 + q[2]) * (g + q)

def portSquare(points):
    ported = []
    for p in points:
        ported.append(port(p))
    ported.append(ported[0])
    edges = list(pairwise(ported))
    print("ported rectangle ", points, " and obtained side lengths")
    for e in edges:
        print(sphericalDist(e[0], e[1]))

def prettyPrintArray(a):
    print(np.array2string(a, separator=', ', formatter={'float_kind':lambda x: "%.3f" % x}).replace('[', '(').replace(']', ')'))

def translateSquare(points, to):
    g = (0, 0, 1)
    q = port(to)
    ported = []
    for p in points:
        ported.append(port(p))
    print("ported rectangle ", points, " and obtained new vertices")
    for p in ported:
        prettyPrintArray(p)
    print("translated rectangle ", points, " to ", to, "(ported as ", q, ")")
    for p in ported:
        prettyPrintArray(translation(q, p, g))


# translate, then port
points = [np.array([0, 0]), np.array([0.5, 0]), np.array([0.5, 0.5]), np.array([0, 0.5])]
portSquare(points)
points = [np.array([0.5, 0.5]), np.array([1, 0.5]), np.array([1, 1]), np.array([0.5, 1])]
print()
portSquare(points)

# port, then translate
points = [np.array([-0.5, -0.7]), np.array([0.5, -0.7]), np.array([0.5, 0.5]), np.array([-0.5, 0.5])]

print()
translateSquare(points, np.array([0.5, 0.5]))

print()
translateSquare(points, np.array([1.5, 1.7]))