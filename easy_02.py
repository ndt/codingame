import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in raw_input().split()]

# game loop
while 1:
    E = int(raw_input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    if TY < LY:
        direction = "S"
        TY+=1
    elif TY > LY:
        direction = "N"
        TY-=1
    else:
        direction = ""

    if TX < LX:
        direction += "E"
        TX+=1
    elif TX > LX:
        direction += "W"
        TX-=1
    
    print direction
