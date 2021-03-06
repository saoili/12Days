import random
import os

with open('names.csv','r') as namesFile:
    names = namesFile.read().split('\n')

with open('log.txt','r') as oldLogFile:
    oldLog = oldLogFile.read()
    
log = open('log.txt','a')
log.write('There are ' + str(len(names)) + ' names in the file\n')

winners = 0
while winners not in range (1,13):
    print "How many winners? (between 1 and 12)"
    winners = int(raw_input(">"))

winnerNames = random.sample(names, winners)
log.write("Today's winners are " + str(winnerNames) + "\n\n")

if winners == 1:
    print "The Winner Is:"
    print winnerNames[0]
else:
    print "The Winners Are:"
    for name in winnerNames:
        print name

for name in winnerNames:
    names.remove(name)
    
with open ('names.csv','w') as namesFile:
    namesFile.write("\n".join(names))

log.close()
