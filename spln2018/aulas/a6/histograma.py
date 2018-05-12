#!/usr/bin/python3.6
import fileinput
import matplotlib.pyplot as plt

#text = ''.join(fileinput.input())

f = plt.figure()

plt.plot([1,2,3,4], [1,4,9,16],"ro")
plt.plot([1,2,3,4], [16,3,4,5],"go")

#plt.axis([0, 6, 0, 20])

#plt.show()

f.savefig("img.pdf",format="pdf")
