#Code by Lilli Christoph 2016

#!usr/bin/python
import sys

num_cases = int(sys.stdin.readline())

for i in range(num_cases):
    raw_data = [int(x) for x in sys.stdin.readline().split()]
    #P prisoners, Q prisoners to be released
    P =[[1, raw_data[0]]]
    Q = raw_data[1]
    #R marks cells of prisoners 'to be released'
    R = [[int(x) for x in sys.stdin.readline().split()]]

    #next prisoner to be released is nearest to midpoint of sub-cell block
    #and within cell block!
    gold = 0

   
   

    while len(P) > 0:
        for j in range(len(P)):
            #print P, len(P), len(P[0]), j
            #print R, len(R), len(R[0])
            #determine which prisoner gets released next
            #find k for R[j][k]=Rmid prisoner going to be released
            if(len(P[j]) > 1):
                Pmid = float(P[j][0] + P[j][1])/2.0
                delta_cells = raw_data[0] + 1  #out of range cell number to start
                for x in range(len(R[j])):
                    delta_cells
                    if abs(R[j][x]-Pmid) < delta_cells:
                        delta_cells = abs(R[j][x]-Pmid)
                        k = x
            else:
                Pmid = float(P[j][0])
                k = 0
            Rmid = R[j][k]

            gold = gold + P[j][1] - P[j][0]
            #print gold
            #print delta_cells , k, R[j][k]

            if(len(R[j]) == 1):
                #only one person in sub-block and they are being released
                #corresponding R and P s-blocks should be removed
                R.pop(j)
                P.pop(j)
                break
                #print R, P, 'popout'
                #continue

            #if((j == len(R)-1) and (k == len(R[j])-1)):
            if (k == len(R[j])-1):
                #released highest# prisoner in sblock
                #don't create upper sblock in this case
                P[j][1] = Rmid-1
                R[j].pop(k)
                #print P, R, 'highest release'
                #continue
                break

            #if((j == 0) and (k == 0)):
            if(k == 0):
                #releasing lowest# prisoner in sblock
                #Don't create lower sblock in this case
                P[j][0] = Rmid+1
                R[j].pop(k)
                #print P, R, 'lowest release'
                #continue
                break

            upper = P[j][1]
            P[j][1] = Rmid - 1
            P.insert(j+1, [Rmid+1, upper])
            Rupper = [R[j][x] for x in range(k+1, len(R[j]))]
            Rlower = [R[j][x] for x in range(0, k)]
            R.pop(j)
            R.insert(j, Rlower)
            R.insert(j+1, Rupper)
            #print P, R, 'typical release'

    print 'Case #{}: {} '.format(i+1, gold)
