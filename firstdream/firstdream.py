import turtle as t

def wind_mill(center_x, center_y, color = "black"):

    t.pu()
    t.setpos(center_x, center_y)
    t.pd()
    
    # t.pencolor(color)
    t.begin_fill()

    for i in range(4):
        t.fd(30)
        t.lt(90)
        t.fd(40)
        t.setpos(center_x, center_y)

    t.end_fill()

def row_left(function, center_x, center_y, first_value, second_value, colors, n):

    if (n >=0 ):
        function(center_x, center_y, colors[n])
        
        # Work leftward
        row_left(function, center_x + first_value, center_y + second_value, first_value, second_value, colors, n - 1)

def row_right(function, center_x, center_y, first_value, second_value, colors, n):

    if (n >= 0 ):
        function(center_x, center_y, colors[n])
        
        # Work rightward
        row_right(function, center_x - first_value, center_y - second_value, first_value, second_value, colors, n - 1)


def row(function, center_x, center_y, first_value, second_value, colors, n):

    function(center_x, center_y, colors[n])
        
    row_left(function, center_x + first_value, center_y + second_value, first_value, second_value, colors, n - 1)
    
    row_right(function, center_x - first_value, center_y - second_value, first_value, second_value, colors, n - 1)
        
        
def main():

#    wind_mill(0, 0)
#    wind_mill(60, 40)
#    wind_mill(40, -60)
#    wind_mill(-40, 60)
#    wind_mill(-60, -40)
    #wind_mill(100, -20)
    
    #coord_center(wind_mill, 60, 40)
    # coord_center(wind_mill, 30, 40)

    colors = ["red", "orange", "green", "blue", "purple"]
    colors = ["black", "black", "black", "black", "black"]

    recursion_const = 4
    
    

    row(wind_mill, 0, 0, 60, 40, colors, recursion_const)

    
    for i in range(1, 4):
        row(wind_mill, i * 40, i * -60, 60, 40, colors, recursion_const) # Downward
        row(wind_mill, i * -40, i * 60, 60, 40, colors, recursion_const) # Upward

    
    #dynamic_center(60, 40, 60, 40)
    #wind_mill(60, 40)

    t.getscreen().getcanvas().postscript(file = "firstdream2.eps")
    
    

    
    while(True):
        t.lt(0)
    
    
if __name__ == "__main__":
    main()
