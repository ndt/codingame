import sys, math

while 1:
    SX, SY = [int(i) for i in raw_input().split()]
    MH = []
    for i in xrange(8):
        MH.append(int(raw_input())) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
    
    m = max(MH)
    p = [i for i, j in enumerate(MH) if j == m]
    
    if SX == p[0]:
        print "FIRE"
    else:
        print "HOLD"
