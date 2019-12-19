import unittest
from journeyToMoon import JourneyToMoon
class JourneyToMoonTest(unittest.TestCase):
    def test(self):
        journey = JourneyToMoon()
        
        n=1 
        pairs = []
        self.assertEquals(0, journey.compute(n,pairs))
        
        n=2 
        pairs = []
        self.assertEquals(1, journey.compute(n,pairs))
        
        n=3
        pairs = []
        self.assertEquals(3, journey.compute(n,pairs))
        
        n=4
        pairs=[[0,2]]
        self.assertEquals(5, journey.compute(n,pairs))
         
        n=6
        pairs=[[1,4],[5,1],[2,3]]
        self.assertEquals(11, journey.compute(n,pairs))
        
        n=5
        pairs=[[0, 1],[2, 3],[0 ,4]]
        self.assertEquals(6, journey.optcomput(n,pairs))
        
        n=5
        pairs=[[0, 1],[1,2],[2,3],[1,2]]
        self.assertEquals(4, journey.optcomput(n,pairs))
        
#         [0,1,2,3],[4]
#         5
#           1,2,3,4,5 = 10
            
            
#         [0,1],[5,4],[1,5]
#             0- 0,1,5,4

            
#            a     b          c        d    e
#         [1,100],[2,99,89],[3,98],[4,97],[5,96]
        
#             a*b*c = 12
#             2*3+2*2+3*2 = 16

#           a*b + a*c + a*d + a*e + b*c + b*d + b*e + c*d + c*e + d*e
  
#             a(b+c+d+e) + b(c+d+e)+c(d+e)+d(e)+e(0)
          
#         [1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]   
        
        
#         a*b + (a+b)*c + (a+b+c)*d + (a+b+c+d)*e
#         a*b + a*c + a*d + b*c + b*d + c*d