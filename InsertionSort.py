'''
Created on Aug 14, 2014

@author: miguel
'''

import random, time
if __name__ == '__main__':
    
    def insertSort(Array):
        sortedArray = [Array[0]]
        for numberinUnsorted in Array[1:]:
            added = False
            for i, numberinSorted in enumerate(sortedArray):
                if numberinSorted > numberinUnsorted:
                    sortedArray.insert(i, numberinUnsorted)
                    added = True
                    break
            if not added:
                sortedArray.append(numberinUnsorted)
                    
    A = [random.randint(1, 10000) for _ in xrange(10000)]
    start = time.clock()
    insertSort(A)
    print time.clock() - start