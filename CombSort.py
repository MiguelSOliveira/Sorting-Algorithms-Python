'''
Created on Aug 14, 2014

@author: miguel
'''

import random, time
if __name__ == '__main__':
    
    def combSort(Array):
        
        n = len(Array)-1
        while n >= 1:
            for i in range(len(Array)-n):
                if Array[i] > Array[i+n]:
                    Array[i], Array[i+n] = Array[i+n], Array[i]
            n = int(n / 1.3)

        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(Array)-1):
                if Array[i] > Array[i+1]:
                    Array[i+1], Array[i] = Array[i], Array[i+1]
                    sorted = False
                
    A = [random.randint(1, 10000) for _ in range(1000000)]
    start = time.clock()
    combSort(A)
    print time.clock() - start
                