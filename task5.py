import sys,math
try:
    outfilename = sys.argv[1]
except:
    print(" Usage : " , sys.argv[0] , " infile outfile ")
    sys.exit(1)
ofile = open(outfilename, 'w')

def myfunc ( y ):
    if y >= 0.0:
        return y**5* math.exp(-y)
    else :
        return 0.0

for x,y in zip(sys.argv[2::2], sys.argv[3::2]):
    x = float(x)
    y = float(y)
    fy = myfunc(y)
    ofile.write('%g%12.5e\n ' % (x, fy))

ofile.close()
