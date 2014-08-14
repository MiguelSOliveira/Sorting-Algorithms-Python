'''
Created on Aug 14, 2014

@author: miguel
'''

import random, time
if __name__ == '__main__':
    
    def gnomeSort(Array):
        
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(Array)-1):
                if Array[i] > Array[i+1]:
                    Array[i], Array[i+1] = Array[i+1], Array[i]
                    sorted = False
                    j = i
                    while(j > 0 and Array[j] < Array[j-1]):
                        Array[j], Array[j-1] = Array[j-1], Array[j]
                        j -= 1
        
    A = [random.randint(1, 1000) for _ in xrange(10000)]
    start = time.clock()
    gnomeSort(A)
    print time.clock() - start
        