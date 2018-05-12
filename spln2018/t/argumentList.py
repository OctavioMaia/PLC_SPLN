#!/usr/bin/python3
"""
Apresenta a lista de opções, sendo estas agrupadas pelas opções

"""
import sys, getopt

argv = sys.argv
print ("Full argument list")
print (argv)

optlist, argv = getopt.getopt(argv[1:], 'abc:d:')

print ("Option list:")
print (optlist)
print ("Argument list: ") 
print (argv)
