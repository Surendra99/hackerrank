import unittest
from lessPetrolCost import EfficientPetrolFiller
class PetrolFillerTest(unittest.TestCase):
    def test(self):
        epf = EfficientPetrolFiller()
        petrolBunkCapacity = []
        
        destination = 0
        petrolPrices = [0]
        distances = [0]
        self.assertEquals(0, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        destination = 1
        petrolPrices = [1]
        distances = [1]
        self.assertEquals(1, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        destination = 2
        petrolPrices = [1, 2]
        distances = [1, 1]
        self.assertEquals(2, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        destination = 2
        petrolPrices = [2, 1]
        distances = [1, 1]
        self.assertEquals(3, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        destination = 5
        petrolPrices = [3, 5]
        distances = [2, 3]
        self.assertEquals(15, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        destination = 10
        petrolPrices = [3, 2]
        distances = [7, 3]
        self.assertEquals(27, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        destination = 14
        petrolPrices = [1, 2, 3]
        distances = [4, 4, 6]
        self.assertEquals(14, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        destination = 12
        petrolPrices = [3, 2, 4]
        distances = [3, 3, 3]
        self.assertEquals(21, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        destination = 13
        petrolPrices = [7,8,6]
        distances = [1,11,1]
        self.assertEquals(90, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
    def test2(self):
            
        epf = EfficientPetrolFiller()
        destination = 0
        petrolPrices = [0]
        distances = [0]
        petrolBunkCapacity = [0]
        self.assertEquals(0, epf.printPetrolPrice(destination, petrolPrices, distances,petrolBunkCapacity))
        
        epf = EfficientPetrolFiller()
        destination = 1
        petrolPrices = [1]
        distances = [1]
        petrolBunkCapacity = [1]
        self.assertEquals(1, epf.printPetrolPrice(destination, petrolPrices, distances, petrolBunkCapacity))
        
        
        
        
        
        
        
        
        
        
        
        
