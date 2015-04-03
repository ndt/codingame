import sys, math

N = int(raw_input()) # the number of temperatures to analyse

try:
    TEMPS = raw_input() # the N temperatures expressed as integers ranging from -273 to 5526
    min = 5527

    for el in TEMPS.split(' '):
        print >> sys.stderr, "{0} - {1}".format(el,min)
        if abs(int(el)) < abs(int(min)):
            min = el
        elif -int(el) == int(min):
            min = el
    print min

except EOFError:
    print "0"
