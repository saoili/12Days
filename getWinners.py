import random

names = open('names.csv','r').read().split(', ')

winners = 0

while winners not in range (1,13):
    print "How many winners? (between 1 and 12)"
    winners = int(raw_input(">"))

print "the winners are"
print random.sample(names, winners)
    
    
 