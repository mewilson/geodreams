import turtle as t


def square():

    for i in range(4):
        t.forward(50)
        t.lt(90)

    t.forward(50)
    t.lt(45)
    t.forward(20)
    t.lt(45)
    t.forward(50)
    t.lt(90 + 45)
    t.forward(20)
    
    t.lt(-45)
    t.forward(50)
    t.rt(90 + 45)
    t.forward(20)
    
    t.rt(45)
    t.forward(50)
    
def reset_turtle(pos_x, pos_y):
    t.pu
    t.setpos(pos_x, pos_y)
    t.pd

def main():

    square()
    
    while(True):
        t.lt(0)


if __name__ == "__main__":
    main()
