'''
Created on Aug 14, 2014

@author: miguel
'''

# A slightly better version of Bubble Sort

import random, time
if __name__ == '__main__':
    
    
    def cocktailSort(Array):
        
        sorted = False
        indexOrder = range(len(Array)-1)
        while not sorted:
            sorted = True
            for index in (indexOrder, reversed(indexOrder)):
                for i in index:
                    if Array[i] > Array[i+1]:
                        sorted = False
                        Array[i], Array[i+1] = Array[i+1], Array[i]
                    
    A = [random.randint(1, 10000) for _ in xrange(10000)]
    start = time.clock()
    cocktailSort(A)
    print time.clock() - start 
