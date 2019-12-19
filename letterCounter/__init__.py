class LetterCounter:
    def count(self,string):
        if len(string) <= 1:
            return string
        res=[]
        strlist = list(string)
        res.append(strlist[0])
        res.append('1')
        itera = len(strlist)-1
        for i in xrange(0,itera):
            if strlist[i]==strlist[i+1]:
                res[len(res)-1]=str(int(res[len(res)-1])+1)
            else:
                res.append(strlist[i+1])
                res.append('1')    
        return "".join(res)