class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
    
    def insert_helper(self, current, new_val):
    """Helper method - used this to create a 
        recursive insert solution."""
        if new_val< current.value:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)
        else:
            if current.right:
                self.insert_helper(current.right,new_val)
            else:
                current.right = Node(new_val)
    
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        print self.preorder_print(tree.root,"")[:-1]
        return ""
        
    def preorder_print(self, start, traversal):
        """Helper method - used this to create a 
        recursive print solution."""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def search(self, find_val):
        return self.search_helper(self.root, find_val)
    
    def search_helper(self, current, find_val):
    """Helper method - used this to create a 
        recursive search solution."""
        if current:
            if find_val == current.value:
                return True
            elif find_val<current.value:
                self.search_helper(current.left, find_val)
            elif find_val>current.value:
                self.search_helper(current.right, find_val)
        return False
    
# Set up tree
tree = BST(4)


# Insert elements
tree.insert(2)
#Should be 4-2
tree.print_tree()

tree.insert(1)
#Should be 4-2-1
tree.print_tree()

tree.insert(3)
#Should be 4-2-1-3
tree.print_tree()

tree.insert(5)
#Should be 4-2-1-3-5
tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
