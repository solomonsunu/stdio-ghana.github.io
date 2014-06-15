myDict = {"Bob": {"position": "waiter", "salary": 15},
          "Sue": {"position": "host", "salary": 17},
          "Rick": {"position": "cook", "salary": 20}
          }

#Write myDict to a file
f = open('testDictOut.txt', 'w')
try:
    f.write(myDict.__str__())
finally:
    f.close()

#Read myDict back
myNewDict = open('testDictOut.txt', 'r').read()
print(type(myNewDict), myNewDict)

#####################
#What happened?
#####################

#Lets try saving it using Pickles
import pickle
f = open("testDictOut.pkl", "wb")
pickle.dump(myDict, f)
f.close()

G = open("testDictOut.pkl", "rb")
myNewDict2 = pickle.load(G)
print(type(myNewDict2), myNewDict2)
######################
# What happened now?
######################

