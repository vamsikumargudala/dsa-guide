## Trees

# Implementing a tree using a list of lists

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]

    def __repr__(self):
        return f"Node({self.value})"
    
root = TreeNode("CEO")
first_child = TreeNode("CTO")
second_child = TreeNode("CFO")

root.add_child(first_child)
root.add_child(second_child)    

root.remove_child(first_child)

print(root)

    



