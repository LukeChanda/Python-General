# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:04:23 2021

@author: Luke

A Point class capable of handling some simple linear algebra operations in 2D.
"""

from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)
    
    def __add__(self, P2):
        if isinstance(P2, Point):
            return Point(self.x + P2.x, self.y + P2.y)
        else:
            raise TypeError('Expected a Point object. Received %s' % type(P2))
            
    def __sub__(self, P2):
        if isinstance(P2, Point):
            return Point(self.x - P2.x, self.y - P2.y)
        else:
            raise TypeError('Expected a Point object. Received %s' % type(P2))
    
    def __mul__(self, p):
        if isinstance(p, Point):
            return self.x * p.x + self.y * p.y # return a scalar (inner product)
        elif type(p) == int or type(p) == float:
            return Point(self.x * p, self.y * p) # return a point (scalar product)
        else:
            raise TypeError('Multiplication with type undefined. Argument of type %s' % type(p))
    
    def __rmul__(self, p): # make multiplication commutitative
        if type(p) == int or type(p) == float:
            return Point(p * self.x, p * self.y) # return a point (scalar product)
        else:
            raise TypeError('Multiplication with type undefined. Argument of type %s' % type(p))
    
    def distance(self, p):
        if isinstance(p, Point):
            # calculate norm
            dx = (self.x - p.x)**2
            dy = (self.y - p.y)**2
            return sqrt(dx + dy)
        else:
            raise TypeError('Distance undefined. Argument of type %s' % type(p))