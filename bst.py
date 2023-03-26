'''
The following operations should be possible:
* adding an element to the structure
* checking if the structure contains the element
* removing the chosen element from the structure
* checking max and min within the structure
* checking the number of elements in the structure
'''

from graphviz import Digraph
import random

def print_tree(root):
    dot = Digraph("Tree",strict=False)
    dot.format='png'
    dot.node("RT",str(root.val))
    def add_rec(dot:Digraph,node,name,parent_name="RT"):
        if node == None:return
        dot.node(name,str(node.val))
        if not name == "RT":dot.edge(parent_name,name)

        add_rec(dot,node.left,name+"L",name)
        add_rec(dot,node.right,name+"R",name)

    add_rec(dot,root,"RT")
    dot.view()

class tree_node:
    def __init__(self,val,parent=None,left=None,right=None) -> None:
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

class tree:
    def __init__(self,val) -> None:
        self.anchor = tree_node(-float("inf")) #we need an anchor so that every node with a value has a parent
        self.root_node = self.anchor
        self.insert(val)
        self.root_node = self.anchor.right
    
    def insert(self,value):
        curr = self.root_node
        while curr != None:
            if value >= curr.val:
                if curr.right == None:
                    curr.right = tree_node(value,curr)
                    return 0
                else:
                    curr = curr.right
            else:
                if curr.left == None:
                    curr.left = tree_node(value,curr)
                    return True
                else:
                    curr = curr.left
        return False
    
    #returns node with value from subtree with root=root or None if value is not in tree
    def getnode(self,value,root = None):
        curr = self.root_node if root == None else root
        while(curr != None):
            if value == curr.val:return curr
            else:
                if value > curr.val: curr = curr.right
                else: curr = curr.left
        return None
    def contains(self,value):
        return bool(self.getnode(value))
    
    def min(self,node = None):
        curr = self.root_node if node == None else node
        min = curr.val
        while (curr := curr.left) != None:
            if curr.val < min: min = curr.val
        return min
    
    def max(self,node = None):
        curr = self.root_node if node == None else node
        mx = curr.val
        while (curr := curr.right) != None:
            if curr.val > mx: mx = curr.val
        return mx

    def num_elements(self,node = None):
        if node == None: node = self.root_node
        return 1 + (self.num_elements(node.left) if node.left != None else 0) + (self.num_elements(node.right) if node.right != None else 0) 
    
    def remove(self,value,root = None):
        n = self.getnode(value,self.root_node if root == None else root)
        if n == None:
            print(f"Node with value {value} does not exist") 
            return False

        if n.left == None and n.right == None:
            if n.parent.val <= n.val: n.parent.right = None
            else: n.parent.left = None
            del n
        elif not(n.left == None or n.right == None):
            n.val = self.min(n.right)
            self.remove(n.val,n.right)
        else:
            node_to_connect = n.left if n.left != None else n.right
            if n.parent.val <= n.val: n.parent.right = node_to_connect
            else: n.parent.left = node_to_connect
            node_to_connect.parent = n.parent
            if n == self.root_node: self.root_node = self.anchor.right
            del n

n=100
t = tree(n//2)

arr = [x for x in range(n)]
for i in [arr.pop(random.randint(0,n-i-1)) for i in range(n)]:
    t.insert(i)

print(t.num_elements())
t.remove(n//2)
t.remove(n//2)
print_tree(t.root_node)
