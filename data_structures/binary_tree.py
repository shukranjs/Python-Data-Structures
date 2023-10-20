"""
A binary tree is an ordered tree with the following properties:
    1. Every node has at most two children.
    2. Each child node is labeled as being either a left child or a right child.
    3. A left child precedes a right child in the order of children of a node.
                                            root
                                          /      \
                                      documents  photos
                                       /   \      /   \
                                    file  file   pics  selfies

"""

# ========================================== Node implementation ===================================================

from typing import Optional, List, Dict


class Node:
    def __init__(self, data: int):
        """
        Initialize a Node with the given data.

        Args:
            data (int): The data to be stored in the node.
        """
        self.data: int = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinaryTree:
    def __init__(self, root: int):
        """
        Initialize a binary tree with a root node containing the given data.

        Args:
            root (int): The data for the root node.
        """
        self.root: Node = Node(root)

    def insert(self, data: int) -> None:
        """
        Insert a new node with the given data into the binary tree.

        Args:
            data (int): The data to be inserted into the tree.
        """
        self._insert_recursively(self.root, data)

    def _insert_recursively(self, current: Node, data: int) -> None:
        """
        Helper method to insert a new node with the given data into the binary tree recursively.

        Args:
            current (Node): The current node being considered.
            data (int): The data to be inserted into the tree.
        """
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursively(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursively(current.right, data)

    def search(self, data: int) -> bool:
        """
        Search for a node with the given data in the binary tree.

        Args:
            data (int): The data to search for.

        Returns:
            bool: True if the data is found in the tree, False otherwise.
        """
        return self._search_recursively(self.root, data)

    def _search_recursively(self, current: Node, data: int) -> bool:
        """
        Helper method to search for a node with the given data in the binary tree recursively.

        Args:
            current (Node): The current node being considered.
            data (int): The data to search for.

        Returns:
            bool: True if the data is found in the tree, False otherwise.
        """
        if current is None:
            return False
        if current.data == data:
            return True
        elif data < current.data:
            return self._search_recursively(current.left, data)
        else:
            return self._search_recursively(current.right, data)

    def inorder_traversal(self) -> List[int]:
        """
        Perform an inorder traversal of the binary tree.

        Returns:
            List[int]: A list of node values in ascending order.
        """
        result: List[int] = []
        self._inorder_traversal_recursively(self.root, result)
        return result

    def _inorder_traversal_recursively(self, node: Node, result: List[int]) -> None:
        """
        Helper method to perform an inorder traversal of the binary tree recursively.

        Args:
            node (Node): The current node being considered.
            result (List[int]): The list to store the traversal result.

        Returns:
            None
        """
        if node:
            self._inorder_traversal_recursively(node.left, result)
            result.append(node.data)
            self._inorder_traversal_recursively(node.right, result)


# Example usage of the binary tree
tree: BinaryTree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

print("Inorder Traversal:")
print(tree.inorder_traversal())

search_value: int = 7
if tree.search(search_value):
    print(f"{search_value} is in the tree.")
else:
    print(f"{search_value} is not in the tree.")

# Another real example of Binary Tree


class TreeNode:
    def __init__(self, name: str, is_directory: bool = False):
        """
        Initialize a tree node.

        Args:
            name (str): The name of the node (file or directory).
            is_directory (bool, optional): True if the node represents a directory, False for a file. Defaults to False.
        """
        self.name: str = name
        self.is_directory: bool = is_directory
        self.children: Dict[str, TreeNode] = {}


class FileSystem:
    def __init__(self):
        """
        Initialize a file system with a root directory.
        """
        self.root: TreeNode = TreeNode("/", is_directory=True)

    def create_directory(self, path: str) -> None:
        """
        Create a directory at the specified path.

        Args:
            path (str): The path at which to create the directory.
        """
        current: TreeNode = self.root
        components: List[str] = path.strip("/").split("/")
        for component in components:
            if component not in current.children:
                current.children[component] = TreeNode(component, is_directory=True)
            current = current.children[component]

    def create_file(self, path: str) -> None:
        """
        Create a file at the specified path.

        Args:
            path (str): The path at which to create the file.
        """
        components: List[str] = path.strip("/").split("/")
        filename: str = components[-1]
        directory_path: str = "/".join(components[:-1])
        current: TreeNode = self.root
        for component in directory_path.split("/"):
            if component in current.children and current.children[component].is_directory:
                current = current.children[component]
            else:
                print(f"Error: Directory '{component}' not found.")
                return
        if filename not in current.children:
            current.children[filename] = TreeNode(filename)

    def list_directory(self, path: str) -> None:
        """
        List the contents of the specified directory.

        Args:
            path (str): The path of the directory to list.
        """
        current: TreeNode = self.root
        components: List[str] = path.strip("/").split("/")
        for component in components:
            if component in current.children:
                current = current.children[component]
            else:
                print(f"Error: Directory '{component}' not found.")
                return
        if current.is_directory:
            for name in current.children:
                if current.children[name].is_directory:
                    print(f"Directory: {name}/")
                else:
                    print(f"File: {name}")


# Example usage
fs: FileSystem = FileSystem()
fs.create_directory("home")
fs.create_directory("home/user")
fs.create_file("home/user/file.txt")

print("List contents of 'home':")
fs.list_directory("home")

print("\nList contents of 'home/user':")
fs.list_directory("home/user")
