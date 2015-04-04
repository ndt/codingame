import sys, math

LON = 2*math.pi/360 * float(raw_input().replace(",","."))
LAT = 2*math.pi/360 * float(raw_input().replace(",","."))
N = int(raw_input())

NAME = ""
DIST = 21000

for i in xrange(N):
    DEFIB = raw_input().split(";")
    DLON = 2*math.pi/360 * float(DEFIB[4].replace(",","."))
    DLAT = 2*math.pi/360 * float(DEFIB[5].replace(",","."))
    
    x = (LON - DLON) * math.cos( (LAT+DLAT)/2 )
    y = LAT - DLAT
    d = math.sqrt( x**2 + y**2) * 6371

    if d < DIST:
        DIST = d
        NAME = DEFIB[1]
    

print "%s" % NAME
