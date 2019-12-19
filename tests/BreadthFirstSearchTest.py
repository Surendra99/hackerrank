from BreadthFirstSearch import BreadthFirstSearch
import unittest
class BreadthFirstSearchTest(unittest.TestCase):
    def test(self):
        bb = BreadthFirstSearch()
        
        n = 2
        m = 1
        edges = []
        start = 1
        self.assertEquals([-1], bb.calculate(n, m, edges, start))
        
        n = 3
        m = 1
        edges = [[1, 2]]
        start=1-1
        self.assertEquals([6], bb.calculate(n, m, edges, start))
    
