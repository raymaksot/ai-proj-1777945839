from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def _validate_key(key):
        """Ensure the key is comparable, raising TypeError if not."""
        try:
            # A dummy comparison to trigger a TypeError for uncomparable types
            _ = key < key
        except TypeError:
            raise TypeError(f"Key must be comparable, but got {type(key)}") from None

    def insert(self, key):
        self._validate_key(key)
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        try:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key)
                else:
                    self._insert_recursive(node.left, key)
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key)
                else:
                    self._insert_recursive(node.right, key)
        except RecursionError:
            raise RuntimeError("Maximum recursion depth exceeded; tree is too deep for recursive insertion.") from None

    def search(self, key):
        self._validate_key(key)
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        try:
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return self._search_recursive(node.left, key)
            else:
                return self._search_recursive(node.right, key)
        except RecursionError:
            raise RuntimeError("Maximum recursion depth exceeded during search.") from None

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        try:
            if node:
                self._inorder_recursive(node.left, result)
                result.append(node.key)
                self._inorder_recursive(node.right, result)
        except RecursionError:
            raise RuntimeError("Maximum recursion depth exceeded during inorder traversal.") from None

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        try:
            if node:
                result.append(node.key)
                self._preorder_recursive(node.left, result)
                self._preorder_recursive(node.right, result)
        except RecursionError:
            raise RuntimeError("Maximum recursion depth exceeded during preorder traversal.") from None

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        try:
            if node:
                self._postorder_recursive(node.left, result)
                self._postorder_recursive(node.right, result)
                result.append(node.key)
        except RecursionError:
            raise RuntimeError("Maximum recursion depth exceeded during postorder traversal.") from None

    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

def main():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Inorder traversal:", bst.inorder())
    print("Preorder traversal:", bst.preorder())
    print("Postorder traversal:", bst.postorder())
    print("Level-order traversal:", bst.level_order())

    print("Search 40:", bst.search(40))
    print("Search 123:", bst.search(123))

if __name__ == "__main__":
    main()