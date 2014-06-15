__author__ = 'Deanne'

#Code to create the datafile.txt file used below.  Text file is provided, but you can uncomment to recreate it.
# X, Y, Z = 43,44,45
# S = 'Spam'
# D = {'a': 1, 'b': 2}
# L = [1, 2, 3]
#
# F = open('datafile.txt', 'w', newline='')
# F.write(S + '\n')
# F.write('%s,%s,%s\n' % (X, Y, Z))
# F.write(str(L) + '$' + str(D) + '\n')
# F.close()

#extracting strings from the first line of the text file
F = open('datafile.txt')
line = F.readline()
print(line)
print(line.rstrip())

#parsing the strings that will become numbers from the second line of the text file
line = F.readline()
print(line)
parts = line.split(',')
print(parts)

#converting strings to integers
print(int(parts[1]))
numbers = [int(P) for P in parts]
print(numbers)

#Converting the stored list and dictionary in the third line of the file
line = F.readline()
print(line)
parts = line.split('$')
print(parts)
print(eval(parts[0]))
objects = [eval(P) for P in parts]
print(objects)
