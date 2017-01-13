#!/usr/bin/env python

import readwrite
import function
import plot

[a,b,c]=readwrite.read()

print(a,b,c)

[x,y] = function.quadratic(a,b,c)

print(x,y)

plot.plot(x,y)
