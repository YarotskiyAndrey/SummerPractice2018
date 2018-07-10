import sys
import math

args = sys.argv

args = [float(i) for i in args[1:]]


def printResult(name, args, res):
    print('\n' + name + " loop:")
    for i in range(len(args)):
        print("log(%s)%s" % (str(args[i]), res[i]))



def elementLoop(args):
    res = ['']*len(args)
    i = 0
    for r in args[0:]:
        if r > 0:
            res[i] = ' = ' + str(round(math.log(r),6))
        else:
            res[i] = ' is illegal'
        i += 1
    printResult('element',args,res)

def indexLoop(args):
    res = [''] * len(args)
    for i in range(len(args)):
        if args[i] > 0:
            res[i] = ' = ' + str(round(math.log(args[i]),6))
        else:
            res[i] = ' is illegal'
    printResult('index', args, res)

def whileLoop(args):
    res = [''] * len(args)
    i = 0
    while i < len(args):
        if args[i] > 0:
            res[i] = ' = ' + str(round(math.log(args[i]), 6))
        else:
            res[i] = ' is illegal'
        i += 1
    printResult('while', args, res)

def infiniteLoop(args):
    res = [''] * len(args)
    i = 0
    try:
        while 1:
            if args[i] > 0:
                res[i] = ' = ' + str(round(math.log(args[i]), 6))
            else:
                res[i] = ' is illegal'
            i += 1
    except:
        printResult('infinite', args, res)

elementLoop(args)
indexLoop(args)
whileLoop(args)
infiniteLoop(args)