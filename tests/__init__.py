import unittest
from breakingRecords import RecordBreakingCalculator
class SampleTest(unittest.TestCase):
    
    def testrun(self):
        rc = RecordBreakingCalculator()
        
        scores = []
        self.assertEquals([0,0], rc.calculate(scores), 'No games played')

        scores = [0]
        self.assertEquals([0,0], rc.calculate(scores))
        
        scores = [1,1]
        self.assertEqual([0,0], rc.calculate(scores))

        scores = [1,2]
        self.assertEqual([1,0], rc.calculate(scores))

        scores = [2,1]
        self.assertEquals([0,1], rc.calculate(scores))
        
        scores = [1,2,2]
        self.assertEqual([1,0], rc.calculate(scores))
        
        scores = [2,1,1]
        self.assertEquals([0,1], rc.calculate(scores))
        
        scores = [1,2,3]
        self.assertEquals([2,0], rc.calculate(scores))

        scores = [3,2,1]
        self.assertEquals([0,2], rc.calculate(scores))
        
        scores = [2,3,1]
        self.assertEquals([1,1], rc.calculate(scores))
        
        scores = [2,3,5,1]
        self.assertEquals([2,1], rc.calculate(scores))
        
        scores = [10 ,5, 20 ,20, 4, 5, 2, 25 ,1]
        self.assertEquals([2,4], rc.calculate(scores))
        
        scores = [3 ,4 ,21 ,36 ,10 ,28 ,35 ,5 ,24, 42]
        self.assertEquals([4,0], rc.calculate(scores))

if __name__ == '__main__':
    unittest.main()