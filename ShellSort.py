'''
Created on Aug 14, 2014

@author: miguel
'''

import random, time
if __name__ == '__main__':
    
    def shellSort(Array):
        
        middle = int(len(Array) / 2)
        while(middle >= 1):
            for i in range(0, len(Array)-middle):
                if Array[i] > Array[i+middle]:
                    Array[i], Array[i+middle] = Array[i+middle], Array[i]
            middle /= 2
        
        # Bubble sort for when middle = 1
        sorted = False
        while not sorted:
            sorted = True
            for index in range(len(Array)-1):
                if Array[index] > Array[index+1]:
                    sorted = False
                    Array[index], Array[index+1] = Array[index+1], Array[index]
        
    A = [random.randint(1, 10000) for _ in xrange(100)]
    print A
    start = time.clock()
    shellSort(A)
    print A
    print time.clock() - start
    