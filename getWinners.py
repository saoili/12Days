import random

names = open('names.csv','r').read().split('\n')

winners = 0

while winners not in range (1,13):
    print "How many winners? (between 1 and 12)"
    winners = int(raw_input(">"))

winnerNames = random.sample(names, winners)

if winners == 1:
    print "The Winner Is:"
    print winnerNames[0]

else:
    print "The Winners Are:"
    for name in winnerNames:
        print name
