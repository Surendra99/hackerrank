import unittest
from DivisibleSet import DivisibleSetCalculator
class DivisibleSet(unittest.TestCase):
    def test1(self):
        calculator = DivisibleSetCalculator()
        
        key=2
        numSet=[2]
        self.assertEquals(1, len(calculator.divisibleSetCalculator(key, numSet)))
           
        key=6
        numSet=[12]
        self.assertEquals(1, len(calculator.divisibleSetCalculator(key, numSet)))
           
        key=3
        numSet=[4,3]
        self.assertEquals(2, len(calculator.divisibleSetCalculator(key, numSet)))
          
        key=4
        numSet=[4,8]
        self.assertEquals(1, len(calculator.divisibleSetCalculator(key, numSet)))
          
        key=3
        numSet=[5,6,9]
        self.assertEquals(2, len(calculator.divisibleSetCalculator(key, numSet)))
          
        key=6
        numSet=[6,15,18]
        self.assertEquals(2, len(calculator.divisibleSetCalculator(key, numSet)))
          
        key=2
        numSet=[4,2,2]
        self.assertEquals(1, len(calculator.divisibleSetCalculator(key, numSet)))
         
 
        key=3
        numSet=[1,7,2,4]
        self.assertEquals(3, len(calculator.divisibleSetCalculator(key, numSet)))
        
        key=1
        numSet=[1]
        self.assertEquals(1, len(calculator.divisibleSetCalculator(key, numSet)))
        