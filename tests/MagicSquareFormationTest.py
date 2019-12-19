import unittest
from MagicSquare import MagicSquareFormer
class MagicSquareFormatterTest(unittest.TestCase):
    
    def testFormation(self):
        
        msFormatter = MagicSquareFormer()

#         original = [[5]]
#         self.assertEquals(0, msFormatter.convertToMagicSquare(original))
#         
#         original = [[5],[3]]
#         self.assertEquals(2, msFormatter.convertToMagicSquare(original))
# #          
# #         original = [[5],[2]]
# #         self.assertEquals(3, msFormatter.convertToMagicSquare(original))
# #          
# #         original = [[4 ,9],[3, 5]]
# #         self.assertEquals(5,msFormatter.convertToMagicSquare(original))
#         
#         original = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
#         self.assertEquals(4, msFormatter.convertToMagicSquare(original))
#         
#         original=[[4,9,2],[3,5,7],[8,1,5]]
#         self.assertEquals(1, msFormatter.convertToMagicSquare(original)) 
# 
#         original = [[4 ,6 ,6],[2 ,4 ,1],[8 ,9 ,8]]
#         self.assertEquals(1, msFormatter.convertToMagicSquare(original))
#         
#         original = [[ 7,2,9],[6,6,2],[5,1,2]]
#         self.assertEquals(1, msFormatter.convertToMagicSquare(original))
        
        
#         6 9
# 422346306 940894801 696810740 862741861 85835055 313720373
#         k=5
#         s = [770528134, 663501748 ,384261537 ,800309024 ,103668401 ,538539662 ,385488901 ,101262949 ,557792122, 46058493]
#         self.assertEquals(6, msFormatter.nonDv(k, s))
        
        k=9
        s=[422346306,940894801,696810740,862741861,85835055,313720373]
        self.assertEquals(5, msFormatter.nonDv(k, s))