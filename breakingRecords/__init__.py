class RecordBreakingCalculator:
    def calculate(self,gameScores):
        index=0
        array = [0,0]
        if len(gameScores) <= 1:
            return array
        minScore = gameScores[0]
        maxScore = gameScores[0]
        while(index < len(gameScores)-1):
            if minScore > gameScores[index+1]:
                minScore = gameScores[index+1]
                array[1]+= 1
            if maxScore < gameScores[index+1]:
                maxScore = gameScores[index+1]
                array[0]+= 1
            index+=1
        return array

if __name__ == '__main__':
    rc = RecordBreakingCalculator()
    rc.calculate()