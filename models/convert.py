#!/usr/bin/python

import sys

f=open(sys.argv[1],'r')

for l in f:
    ls=l.strip().split('|')
    out=ls[0]+"|||"+ls[3]+"|||"+ls[9]+" |||"+ls[6] + "|||" + ls[12]

    #print l
    print out
