class DoctorNode:
    def __init__(self, DoctorName):
        self.name = DoctorName
        self.left = None
        self.right = None
    
     # Delete this line and implement the DoctorNode class



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, DoctorName, SecondDoctor, side,current_node=None):
        if self.root is None:
            print("The are no doctors in the tree.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == DoctorName:
            if side == "left":
                if current_node.left is None:
                    current_node.left = DoctorNode(SecondDoctor)
                    return True
                else:
                    print(f"Left doctor of {DoctorName} already exists.")
                    return False
            elif side == "right":
                if current_node.right is None:
                    current_node.right = DoctorNode(SecondDoctor)
                    return True
                else:
                    print(f"Right doctor of {DoctorName} already exists.")
                    return False

        added = False
        if current_node.left:
            added = self.insert(DoctorName, SecondDoctor, side, current_node.left)

        if not added and current_node.right:
            added = self.insert(DoctorName, SecondDoctor, side, current_node.right)

        if not added and current_node == self.root:
            print(f"Dr. '{DoctorName}' not found in the team tree.")

        return added
     # Delete this line and implement the DoctorTree class

    def print_tree(self, node=None, level=0):     
            if node is None:
                if level == 0:
                    if self.root is None:
                        print("The team tree is empty.")
                        return
                    node = self.root

            if node is not None:
                indent = "  " * level
                print(f"{indent}- {node.name}")
                self.print_tree(node.left, level + 1)
                self.print_tree(node.right, level + 1)


    def preorder_traversal(self, node=None, is_start=True):
    
        if node is None and is_start:
            node = self.root

        if node is None:
            return []

        return (
            [node.name]
            + self.preorder_traversal(node.left, False)
            + self.preorder_traversal(node.right, False)
        )

    
    def inorder_traversal(self, node=None, is_start=True):
        if node is None and is_start:
            node = self.root

        if node is None:
            return []

        return (
            self.inorder_traversal(node.left, False)
            + [node.name]
            + self.inorder_traversal(node.right, False)
        )
        
    def postorder_traversal(self, node=None, is_start=True):
        if node is None and is_start:
            node = self.root

        if node is None:
            return []

        return (
            self.postorder_traversal(node.left, False)
            + self.postorder_traversal(node.right, False)
            + [node.name]
        )

# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")

tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")

tree.print_tree()
print("Preorder traversal:", tree.preorder_traversal())
print("Inorder traversal:", tree.inorder_traversal())
print("Postorder traversal:", tree.postorder_traversal())