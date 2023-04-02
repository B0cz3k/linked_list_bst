'''
The following operations should be possible:
* adding an element to the structure X
* checking if the structure contains the element X
* removing the chosen element from the structure !!!
* checking max and min within the structure X
* checking the number of elements in the structure X
'''
import random
import timeit
class Node:
    def __init__(self, data, nxt=None) -> None:
        self.val = data
        self.next = nxt

    def add(self, data):
        while self.next is not None:
            self = self.next
        self.next = Node(data)
    
    def exist(self, data):
        while self.val != data and self.next is not None:
            self = self.next

        return self.val == data
        
    def remove(self, data):
        if not self.exist(data):
            print(f'Remove: given element ({data}) does not exist')
            return 

        if self.val == data: # removing the first element
            self.val = self.next.val
            self.next = self.next.next if self.next.next is not None else None
            print(f'Removed {data} succesfully')
            return

        while self.next is not None: # removing anything else
            if self.next.val == data and self.next.next is None:
                self.next = None
                print(f'Removed {data} succesfully')
                return
            elif self.next.val == data:
                self.next = self.next.next
            else:
                self = self.next

    def maxi(self, M=-2147483647):
        while self.next is not None:
            if self.val > M:
                M = self.val
            self = self.next

        return max(self.val, M)
        
    def mini(self, m=2147483647):
        while self.next is not None:
            if self.val < m:
                m = self.val
            self = self.next

        return min(self.val, m)
        
    def total_elements(self, count=0):
        if self.val is not None:
            count += 1

        while self.next is not None:
            count += 1
            self = self.next

        return count
            
    def __str__(self) -> str:
        s = f'{self.val}'
        while self.next is not None:
            self = self.next
            s += f' -> {self.val}'
        return s

if __name__ == "__main__":
    List = Node(5)
    List = Node(random.randint(0, 100000), List)
    List.add(3)
    List.add(1)
    List.add(2)
    List = Node(random.randint(0, 100000), List)
    List.add(4)
    print(f'Before removal: {List}')
    List.remove(5)
    List.remove(7)
    print(f'After removal: {List}')
    print(f'2 exists in the list: {List.exist(2)}')
    print(f'5 exists in the list: {List.exist(5)}')
    print(f'Max element: {List.maxi()}')
    print(f'Min element: {List.mini()}')
    print(f'Total elements: {List.total_elements()}')

    print('Linked List')
    list_times = []
    l = Node(random.randint(0, 100000))

    for i in range(1000, 101000, 1000):
        for _ in range(1000):
            l = Node(random.randint(0, 100000), l)
        
        result = round((timeit.timeit(lambda: l.exist(random.randint(0, 100000)), number=10000) * 1000) / 10000, 5)
        print(f'{i} elements: {result} s search time')
        list_times.append(result)