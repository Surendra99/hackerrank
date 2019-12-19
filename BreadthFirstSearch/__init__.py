class BreadthFirstSearch:
    def calculate(self, n, m, edges, start):
        if len(edges) == 0:
            return [-1] * (n - 1)
        matrixd = [[-1 for x in range(n)] for y in range(n)]
        tat = [-1] * n 
        travelledPositions = [-1] * n
        for value in edges:
            matrixd[value[0] - 1][value[1] - 1] = 1
            matrixd[value[1] - 1][value[0] - 1] = 1
            
        self.__travel(start,matrixd,travelledPositions,tat)  
        print matrixd    
        return tat
        