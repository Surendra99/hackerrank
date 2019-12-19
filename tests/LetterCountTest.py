import unittest
from letterCounter import LetterCounter
class LetterCountTest(unittest.TestCase):
    def test1(self):
        counter = LetterCounter()
        string=''
        self.assertEquals('', counter.count(string))
          
        string = 'h'
        self.assertEquals('h', counter.count(string))
          
        string='gg'
        self.assertEquals('g2', counter.count(string))
         
        string='hhh'
        self.assertEquals('h3', counter.count(string))
        
        string='eehhf'
        self.assertEquals('e2h2f1', counter.count(string))
        
        string='abbbccc'
        self.assertEquals('a1b3c3', counter.count(string))
        