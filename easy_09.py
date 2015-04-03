import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # Number of elements which make up the association table.
Q = int(raw_input()) # Number Q of file names to be analyzed.

table = dict()
for i in xrange(N):
    EXT, MT = raw_input().split()
    table[EXT.lower()] = MT

for i in xrange(Q):
    FNAME = raw_input() # One file name per line.
    res = FNAME.rsplit('.',1)
    if len(res) > 1:
        FILE, FEXT = res
        try:
            print table[FEXT.lower()]
        except KeyError:
            print "UNKNOWN"
    else:
        print "UNKNOWN"

