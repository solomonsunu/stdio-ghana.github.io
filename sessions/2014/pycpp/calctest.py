#!/usr/bin/python3

from os import system

# Test whether our calculator is giving proper results
# For any two inputs, perform all 4 operations

a = int(input('First number? '))
b = int(input('Second number? '))

for op in '+-x/':
	print('op is:', op)
	system('./calc %d %c %d' % (a,op,b))
