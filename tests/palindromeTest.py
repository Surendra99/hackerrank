from easy.PalindromIndex import PalindromIndex

import unittest

class PalindromeTest(unittest.TestCase):
    def test(self):
        
        pn = PalindromIndex()
        str1 = "aa"
        self.assertEquals(-1,pn.find_index(str1))
         
        str1 = "aaa"
        self.assertEquals(-1,pn.find_index(str1))
         
        str1 = "aaab"
        self.assertEquals(3,pn.find_index(str1))
         
        str1 = "baa"
        self.assertEquals(0,pn.find_index(str1))
         
        str1 = "quyjjdcgsvvsgcdjjyq"
        self.assertEquals(1,pn.find_index(str1))
         
        str1 = "hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh"
        self.assertEquals(8,pn.find_index(str1))
        
        str1 = "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"
        self.assertEquals(44,pn.find_index(str1))
        