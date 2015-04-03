import sys, math

state = -1
buf   = ""

for each_char in input():
    for each_bit in (format(ord(each_char), "07b")):
        if each_bit == state:
            buf += "0"
        else:
            buf += (" " if len(buf)>0 else "")
            print(buf, end='')
            
            buf = "00 0" if each_bit == "0" else "0 0"
            state = each_bit

print(buf)
