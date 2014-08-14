'''
Created on Aug 14, 2014

@author: miguel
'''
import random, time
if __name__ == '__main__':
    
    def selectSort(Array):
        
        minIndex = 0
        i = 0
        while i < len(Array):
            minimum = 1000000
            for j, number in enumerate(Array[i:]):
                if number < minimum:
                    minimum = number
                    minIndex = j+i
            Array[i], Array[minIndex] = Array[minIndex], Array[i]
            i+=1
            
    start = time.clock()
    A = [random.randint(1, 10000) for _ in range(1000)]
    selectSort(A)
    print time.clock() - start