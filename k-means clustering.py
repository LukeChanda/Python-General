# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:01:52 2021

@author: Luke

2 - mean clustering algorithm
"""

import pointClass as Pnt

class Cluster(object):
    def __init__(self, x, y):
        self.center = Pnt.Point(x, y)
        self.points = []
        
    def __repr__(self):
        return "({}, {})".format(self.center.x, self.center.y)
    
    def update(self):
        sum_x = 0
        sum_y = 0
        
        x = 0
        y = 0
        
        for tpl in self.points:
            sum_x += self.points[x][0] 
            sum_y += self.points[y][1] 
    
            x = x + 1
            y = y + 1
      
        x_avg = sum_x / len(self.points)
        
        y_avg = sum_y / len(self.points)
        
        self.center = Pnt.Point(x_avg, y_avg)
        
    def add_point(self, point):
        self.points.append((point.x, point.y))

    
def compute_result(points):    
    # initial guesses
    a = Cluster(1,0)
    b = Cluster(-1,0)
    
    # store old clusters
    a_old = []
    b_old = []
    
    for _ in range(100): # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                a.add_point(point)
            else:
                b.add_point(point)
        if a_old == a.points:
            break
        
        a_old = a
        b_old = b
        
        a.update()
        b.update()
        
    
    return print(a), print(b)

# test case
points = [Pnt.Point(10, 0), Pnt.Point(-10, 0), Pnt.Point(-12, 0), \
          Pnt.Point(12, 0), Pnt.Point(20, 0)]

compute_result(points)