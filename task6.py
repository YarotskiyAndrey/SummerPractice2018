import sys , math
try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except:
    print(" Usage : " , sys.argv[0] , " infile outfile ")
    sys.exit(1)
ifile = open(infilename, 'r')
ofile = open(outfilename, 'w')

def myfunc ( y ):
    if y >= 0.0:
        return y**5* math.exp(-y)
    else :
        return 0.0

for line in ifile :
    line = line.split()
    line = [float(i) for i in line[:]]
    average = sum(line)/len(line)

    for num in range(len(line)):
        ofile.write('%12.6f ' % line[num])
    ofile.write('%12.6f\n' % average)
    print(average)

ifile.close()
ofile.close()