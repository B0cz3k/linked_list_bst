'''
The following operations should be possible:
* adding an element to the structure
* checking if the structure contains the element
* removing the chosen element from the structure
* checking max and min within the structure
* checking the number of elements in the structure
'''
class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None

    def add(self, data):
        if self.next is not None:
            return self.next.add(data)
        else:
            self.next = Node(data)
    
    def exist(self, data):
        if self.val == data:
            return True
        elif self.next is not None:
            return self.next.exist(data)
        else:
            return False
        
    def remove(self, data):
        if not self.exist(data):
            return 'Given element does not exist'
        if self.next is not None:
            if self.next.val == data and self.next.next is None:
                self.next = None
            elif self.next.val == data:
                self.next = self.next.next
            else:
                return self.next.remove(data)
            
    def maxi(self, M=-2147483648):
        if self.val > M and self.next is not None:
            return self.next.maxi(self.val)
        elif self.val > M:
            return f'Maximum: {self.val}'
        elif self.next is not None:
            return self.next.maxi(M)
        else:
            return f'Maximum: {M}'
        
    def mini(self, m=2147483648):
        if self.val < m and self.next is not None:
            return self.next.mini(self.val)
        elif self.val < m:
            return f'Minimum: {self.val}'
        elif self.next is not None:
            return self.next.mini(m)
        else:
            return f'Minimum: {m}'
        
    def total_elements(self, count=0):
        return self.next.total_elements(count=count+1) if self.next is not None else f'Total number of elements: {count+1}'
            
    def __str__(self) -> str:
        return f'{self.val} -> {self.next}'
    
List = Node(5)
List.add(3)
List.add(1)
print(List.exist(2))
print(List.exist(5))
print(List)
print(List.maxi())
print(List.mini())
print(List.total_elements())