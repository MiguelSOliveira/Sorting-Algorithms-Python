'''
Created on Aug 14, 2014

@author: miguel
'''

import random
if __name__ == '__main__':
    
    def mSort(array):
        if len(array) < 20:
            return sorted(array)
        else:
            middle = int(len(array) / 2)
            left = mSort(array[:middle])
            right = mSort(array[middle:])
            i = 0
            j = 0
            res = []
            while i < len(left) and j < len(right):
                
                if left[i] > right[j]:
                    res.append(right[j])
                    j+=1
                else:
                    res.append(left[i])
                    i+=1
            res += left[i:]
            res += right[j:]
            return res
        
    A = [random.randint(1, 100) for _ in xrange(100)]
    print mSort(A)
    
    
        
    