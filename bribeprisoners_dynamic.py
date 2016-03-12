#Code by Lilli Christoph 2016
#This dynamic algorithm was with much help from online sources below:
#http://www.necessaryandsufficient.net/2009/09/code-jam-2009-bribe-the-prisoners/
#I would have totally spent forever on the list dimension limits, etc

#!usr/bin/python


import sys

def minGold(left, right, minCost):

    if(right - left < 0):
        #indicates no prisoners to release on that side
        #either left or right side
        return 0
    if(minCost[left][right] >= 0):
        #I've already calc it, so just return the answer
        return minCost[left][right]

    cheapest = 1<<30 #largest 32 bit signed int, apparently
    for i in range(left, right+1, 1):
        cheapest = min(cheapest, R[right+1] - R[left-1] -2 +
                       minGold(left, i-1, minCost) +
                       minGold(i+1, right, minCost))
    minCost[left][right] = cheapest
    return cheapest


    
num_cases = int(sys.stdin.readline())

for i in range(num_cases):
    raw_data = [int(x) for x in sys.stdin.readline().split()]
    #P prisoners, Q prisoners to be released
    P =[[1, raw_data[0]]]
    Q = raw_data[1]
    #R marks cells of prisoners 'to be released'
    R = [int(x) for x in sys.stdin.readline().split()]
    R.append(raw_data[0] +1)
    R.insert(0, 0)
    #print R

    minCost = [[-1 for j in range(Q+1)] for k in range(Q+1)]
    #minCost[left][right] is lowest gold needed to release all prisoners between
    #R[left] and R[right] exclusive.....I think.
    
    print 'Case #{}: {} '.format(i+1, minGold(1, Q, minCost))
