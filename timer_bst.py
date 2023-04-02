from bst import tree
import random
import timeit
from tqdm import tqdm #command line progress bars (very nice)
from matplotlib import pyplot as plt

#Create tree with root value of n/2 and populate with n random values from 0 to n.
def maketree(n:int)->tree:
    t = tree(n//2)

    print(f"generating data of size {n}...")
    arr = [random.randint(0,n) for _ in tqdm(range(n))]
    print("creating tree...")
    for i in tqdm(arr):
        t.insert(i)

    return t

min_n = 1000
max_n = 100000
step = 1000
results = {'n':[],'r':[]}
for n in range(min_n,max_n,step):
    t = maketree(n)
    result = round(timeit.timeit(lambda: t.contains(random.randint(0,n)),number=10000)*1000,5)
    print(result)
    results['n'].append(n)
    results['r'].append(result)
    del t

plt.plot(results['n'],results['r'])
plt.xlabel("Number of tree nodes")
plt.ylabel("Total execution time (ms)")
plt.title("Time to check existence of node in n-node BST (time for 10000 attempts)")
plt.show()