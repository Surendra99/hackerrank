import collections
class ClimbingLeaderBoard:
    
    def climbLeaderBoard(self,gameScores,aliceScores):
        aliceRanks = list()
        scores = set()
        nextIterationStartIndex = [0]
        for aliceScoreIndex in xrange(len(aliceScores)-1,-1,-1):
            aliceRanks.append(self.calculate(gameScores,aliceScores[aliceScoreIndex],scores,nextIterationStartIndex))
        aliceRanks.reverse()
        return aliceRanks
    
    def calculate(self,gameScores,aliceScore,scores,nextIterationStartIndex):
        for index in xrange(nextIterationStartIndex[0],len(gameScores)):
            if gameScores[index] <= aliceScore:
                nextIterationStartIndex[0] = index
                break
            else:
                scores.add(gameScores[index])
                nextIterationStartIndex[0] = index
        return len(scores)+1