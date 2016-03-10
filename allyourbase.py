#!/usr/bin/python
import sys

num_cases = int(sys.stdin.readline())

for i in range(num_cases):
    #input data for case without whitespace/newline
    message = sys.stdin.readline().rstrip()
    #print message, len(message)
    
    alphabet = []
    message_to_alpha = []
    for j in range(len(message)):
        if message[j] not in alphabet:
            message_to_alpha += [len(alphabet)]
            alphabet += message[j]
        else:
            first_instance = alphabet.index(message[j])
            message_to_alpha += [first_instance]
    base = max(2, len(alphabet))
    #print alphabet, message_to_alpha
    
    #make mapping from message characters to numbers they represent
    #first character in message cannot be zero
    #otherwise leftmost char is lowest possible number
    #decoder[x] maps to alphabet[x]
    decoder = []
    decoder += [1]
    decoder += [0]
    if base > 2:
        for j in range(2,base):
            decoder += [j]
    #print decoder

    #now calculate numerical equivalent in base 10
    wartime = 0
    exponent = 0
    for j in range(len(message)-1, -1, -1):
        wartime += decoder[message_to_alpha[j]]*pow(base, exponent)
        exponent = exponent +1
    print 'Case #{}: {} '.format(i+1, wartime)
