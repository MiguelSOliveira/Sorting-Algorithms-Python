'''
Created on Aug 14, 2014

@author: miguel
'''

import random, time, sys
if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    def quickSort(Array):
        if not Array:
            return []
        else:
            pivot = Array[0]
            left = [i for i in Array[1:] if i <= pivot]
            right = [i for i in Array[1:] if i > pivot]
            return quickSort(left) + [pivot] + quickSort(right)
        
    A = [random.randint(1, 10000) for _ in xrange(100000)]
    start = time.clock()
    quickSort(A)
    print time.clock() - start