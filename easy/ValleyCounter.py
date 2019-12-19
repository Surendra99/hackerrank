class ValleyCounter:
    def count_valleys(self,n,s):
        sr = list(s)
        ar = {}
        ar['D'] = 0
        ar['U'] = 0
        v=0
        for i in range(0,n-1):
            print ar['U'],ar['D'],i,sr[i],'frst'
            if sr[i] == 'D' and ar['U'] == 0 and ar['D'] == 0:
                v+=1
            if sr[i] == 'D':
                if ar['U'] > 0:
                    ar['U']-=1
                else:
                    ar['D'] +=1
            if sr[i] == 'U':
                if ar['D'] > 0:
                    ar['D']-=1
                else:
                    ar['U'] +=1  
        return v