import turtle as t
import numpy as np

points = 3.0

for i in np.arange(0, 500, 1.33):
    t.right(360 / points + 0.5)
    t.forward(i)
    
while(True):
    t.left(0)
