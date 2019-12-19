class MagicSquareFormer:
    def convertToMagicSquare(self,s):
        if len(s) == 1:
            return 0    
        else:
            sumOfArrays = set()
            for index in range(len(s)):
                sumOfArrays.add(sum(s[index]))
            leftD = list()
            rightD = list()    
            for index in range(len(s)):
                    leftD.append(s[index][index])
            for index in range(len(s)):
                    leng = len(s[index])
                    rightD.append(s[leng-1-index][index])
            sumOfArrays.add(sum(leftD))
            sumOfArrays.add(sum(rightD))
            cost = 0
            for element in sumOfArrays:
                cost+=abs(15-element)
        return cost
    
    def nonDv(self,k, s):
        sv = set();
        if len(s) == 1:
            if s[0]%k!=0:
                return 0
            else:
                return 1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                print str(s[i]) + "-" + str(s[j])+"-" + str((s[i]+s[j])%k)
                if((s[i]+s[j])%k!=0):
                    sv.add(s[i]);
                    sv.add(s[j]);
        print sv        
        return len(sv)