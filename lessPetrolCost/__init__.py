class EfficientPetrolFiller:
    def printPetrolPrice(self, destination, petrolPrices, distances,petrolBunkCapacity):
        if(len(petrolPrices) == 0):
            return 0    
        elif (len(petrolPrices) == 1):
            return petrolPrices[0] * destination 
        sum = 0
        min = petrolPrices[0]
        for x in range(len(petrolPrices)):
            if min > petrolPrices[x]:
                sum+=petrolPrices[x] * distances[x]
                min = petrolPrices[x]
            else:
                sum+=min*distances[x]    
        return sum        