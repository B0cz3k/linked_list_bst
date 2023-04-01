'''
Measure how much time it takes to check existence of an element depending on the number
of them. All your results should be presented using graphs.
'''
import matplotlib.pyplot as plt
import numpy as np

# Load and rearrange the data
linked_list = np.loadtxt('linked_list.txt', delimiter=' ')
#bst = np.loadtxt('bst.txt', delimiter=' ')
x = np.arange(len(linked_list))

# Plot
fig, ax = plt.subplots(1, 1)
ax.plot(x, linked_list, color='red', label='Linked List')
#ax.plot(x, bst, color='green', label='Binary Search Tree')

plt.scatter(x, linked_list, s=100, c='red', marker='o')#
#plt.scatter(x, bst, s=100, c='green', marker='o')#

plt.title('Linked List vs Binary Seach Tree')
plt.xlabel('number of elements')
plt.ylabel('time [s]')
plt.legend()
plt.grid(True)
plt.show()

'''
fig, ax = plt.subplots(1, 1)
ax.plot(x[:10], linked_list[:10], color='red', label='Linked List')
ax.plot(x[:10], bst[:10], color='green', label='Binary Search Tree')

plt.scatter(x[:10], linked_list[:10], s=100, c='red', marker='o')#
plt.scatter(x[:10], bst[:10], s=100, c='green', marker='o')#

plt.title('Linked List vs Binary Search Tree')
plt.xlabel('number of elements')
plt.ylabel('time [s]')
plt.legend()
plt.grid(True)
plt.show()
'''