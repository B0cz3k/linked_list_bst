'''
Measure how much time it takes to check existence of an element depending on the number
of them. All your results should be presented using graphs.
'''

import linked_list
import bst
import random
import time
import numpy as np

# Linked list timings
list_times = []
List = linked_list.Node(5)

for i in range(1000, 11000, 1000):
    for _ in range(i):
        List.add(random.randint(-2147483647, 2147483647))
    
    start_time = time.time() 
    print(List.exist(random.randint(-2147483647, 2147483647)))
    stop_time = time.time()
    total = stop_time - start_time
    
    list_times.append(total)
    print(f'{i} elements : {(total)} s searching time')

np.savetxt('linked_list.txt', list_times, delimiter=' ')

# BST timings
