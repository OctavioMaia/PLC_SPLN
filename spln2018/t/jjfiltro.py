#!/usr/bin/python3
"""
 template for filters
"""
import sys, getopt, fileinput

try: 
    _op, A =getopt.getopt(sys.argv[1:], "a:e")
    opt=dict(_op)
except getopt.GetoptError as err:
    print(str(err))
#    usage()
    sys.exit(2)

for line in fileinput.input(A):
    line = line.strip()
    print(line);
