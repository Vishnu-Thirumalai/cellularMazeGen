class Node:
    
    def __init__(self, data, left, right):
    
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
            
        return "{} L{} R{}".format(self.data, self.left, self.right)  
        
class kdTree:

    def __init__(self, k):
        self.k = k
        self.head = None
        
    def add(self, data):
        """
            If it's the wrong dimensions or is equal to a node already in the tree, returns None.
            Else adds it to the tree, and returns the node
        """
        if len(data) != self.k:
            return None
            
        dim = 0
        curr = self.head
        
        if self.head is None:
            self.head = Node(data,None,None)
            return self.head
        
        while curr.data != data:
            if curr.data[dim] > data[dim]:#Left
                if curr.left == None:
                    curr.left = Node(data,None,None)
                    return curr.left
                else:
                    curr = curr.left
            else:
                if curr.right == None:
                    curr.right = Node(data,None,None)
                    return curr.right
                else:
                    curr = curr.right
            dim = (dim+1)%self.k          
            
        return None            
                                  
    def __str__(self):
        return str(self.head).replace('None',"")
        
data = [(30,40), (5,25), (10,12), (70,70), (50,30), (35,45),]
        
tree = kdTree(2)
for d in data:
    kdTree.add(tree,d)
    
print(tree)                    
