class JourneyToMoon:
    def compute(self,n,pairs):
        if len(pairs) == 0:
            return  ((n-1)*n)/2
        astr = [-1] * n
        cntr = []
        position=0
        cntrpostions={}
        for pair in pairs:
            if astr[pair[0]] == -1 and astr[pair[1]] == -1:
                astr[pair[0]] = position
                astr[pair[1]] = position
                cntr.append(0)
                cntrpostions[position] = []
                cntrpostions[position].append(pair[0])
                cntrpostions[position].append(pair[1])
                cntr[position]+=2
                position+=1
            else:
                if astr[pair[1]] == -1:
                    astr[pair[1]] = astr[pair[0]]
                    poste = cntrpostions[astr[pair[0]]]
                    poste.append(pair[1])
                    cntr[astr[pair[1]]]+=1
                elif astr[pair[0]] == -1:
                    astr[pair[0]] = astr[pair[1]]
                    poste = cntrpostions[astr[pair[1]]]
                    poste.append(pair[0])
                    cntr[astr[pair[1]]]+=1
                else:
                    newvalue = astr[pair[0]]
                    oldvalue = astr[pair[1]]
                    oldcntrpo = cntrpostions[oldvalue]
                    for idx, val in enumerate(oldcntrpo):
                            astr[val]=newvalue
                            cntrpostions[newvalue].append(val)
                            cntr[newvalue]+=1
                    cntr[oldvalue] =0        
                    del cntrpostions[oldvalue]
        for ast in astr:
            if ast == -1:
                cntr.append(1)
        sums=n
        bigsum=0
        for cnt in cntr:
            if cnt != 0:
                sums-=cnt
                bigsum+=(sums*cnt)
        return bigsum
    
    def optcomput(self,n,pairs):   
        total = (n*(n-1)/2)
        astr = [-1] * n
        cntr = []
        position=0
        cntrpostions={}
        for pair in pairs:
            if astr[pair[0]] == -1 and astr[pair[1]] == -1:
                total=total-1
                astr[pair[0]] = position
                astr[pair[1]] = position
                cntr.append(0)
                cntrpostions[position] = []
                cntrpostions[position].append(pair[0])
                cntrpostions[position].append(pair[1])
                cntr[position]+=2
                position+=1
            else: 
                if astr[pair[1]] == -1:
                    astr[pair[1]] = astr[pair[0]]
                    poste = cntrpostions[astr[pair[0]]]
                    total-=len(poste)
                    poste.append(pair[1])
                    cntr[astr[pair[1]]]+=1
                elif astr[pair[0]] == -1:
                    astr[pair[0]] = astr[pair[1]]
                    poste = cntrpostions[astr[pair[1]]]
                    total-=len(poste)
                    poste.append(pair[0])
                    cntr[astr[pair[1]]]+=1
                elif astr[pair[1]] != astr[pair[0]]:
                    newvalue = astr[pair[0]]
                    oldvalue = astr[pair[1]]
                    oldcntrpo = cntrpostions[oldvalue]
                    total-=len(oldcntrpo)*len(cntrpostions[newvalue])
                    for idx, val in enumerate(oldcntrpo):
                            astr[val]=newvalue
                            cntrpostions[newvalue].append(val)
                            cntr[newvalue]+=1
                    cntr[oldvalue] =0        
                    del cntrpostions[oldvalue]    
        return int(total)
                
                    