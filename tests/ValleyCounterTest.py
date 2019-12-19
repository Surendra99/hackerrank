import unittest
from easy.ValleyCounter import ValleyCounter
class ValleyCounterTest(unittest.TestCase):
    def test_valley(self):
        counter = ValleyCounter()
        
        n=0
        s=''
        self.assertEquals(0,counter.count_valleys(n,s))
           
        n=2
        s='UD'
        self.assertEquals(0,counter.count_valleys(n,s))
          
        n=8
        s='UDDDUDUU'
        self.assertEquals(1,counter.count_valleys(n,s))
         
        n=12
        s='DDUUDDUDUUUD'
        self.assertEquals(2,counter.count_valleys(n,s))
        
        n=10
        s='UDUUUDUDDD'
        self.assertEquals(0,counter.count_valleys(n,s))