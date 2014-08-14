'''
Created on Aug 14, 2014

@author: miguel
'''

import random
if __name__ == '__main__':
    
    unsortedArray = [random.randint(1, 100) for _ in xrange(1, 100)]

    sorted = False
    while not sorted:
        sorted = True
        for index in xrange(len(unsortedArray)-1):
            if unsortedArray[index] > unsortedArray[index+1]:
                sorted = False
                unsortedArray[index], unsortedArray[index+1] = unsortedArray[index+1], unsortedArray[index]
    print unsortedArray