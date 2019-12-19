import unittest
from climbingLeaderBoard import ClimbingLeaderBoard
class ClimbingLeaderBoardTest(unittest.TestCase):
    def testsample(self):
        cl = ClimbingLeaderBoard() 
        gameScores = [0]
        aliceScores = [0]
        self.assertEquals([1], cl.climbLeaderBoard(gameScores, aliceScores))
 
        gameScores = [10]
        aliceScores = [5]
        self.assertEquals([2], cl.climbLeaderBoard(gameScores, aliceScores))
         
        gameScores = [10]
        aliceScores = [10]
        self.assertEquals([1], cl.climbLeaderBoard(gameScores, aliceScores))
          
        gameScores = [5]
        aliceScores = [10]
        self.assertEquals([1], cl.climbLeaderBoard(gameScores, aliceScores))
        
        gameScores = [10, 5]
        aliceScores = [3]
        self.assertEquals([3], cl.climbLeaderBoard(gameScores, aliceScores))
         
        gameScores = [10, 10]
        aliceScores = [5]
        self.assertEquals([2], cl.climbLeaderBoard(gameScores, aliceScores))
         
        gameScores = [10, 8, 5]
        aliceScores = [9]
        self.assertEquals([2], cl.climbLeaderBoard(gameScores, aliceScores))
         
        gameScores = [20, 12, 10, 9]
        aliceScores = [8]
        self.assertEquals([5], cl.climbLeaderBoard(gameScores, aliceScores))
         
        gameScores = [100 , 100, 50, 40, 40, 20, 10]
        aliceScores = [25] 
        self.assertEquals([4], cl.climbLeaderBoard(gameScores, aliceScores))
        
        gameScores = [100 , 100, 50, 40, 40, 20, 10]
        aliceScores = [5 , 25 , 50 , 120] 
        self.assertEquals([6, 4, 2, 1], cl.climbLeaderBoard(gameScores, aliceScores))
        
if __name__ == '__main__':
    unittest.main()
