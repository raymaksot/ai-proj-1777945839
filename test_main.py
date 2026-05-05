import pytest
from main import BinarySearchTree

class Uncomparable:
    """A class that deliberately fails comparison operations."""
    def __lt__(self, other):
        raise TypeError("cannot compare")

    def __gt__(self, other):
        raise TypeError("cannot compare")

# ---------------- helper to create a sample tree ----------------
@pytest.fixture
def sample_bst():
    """Returns a BST with pre-inserted keys: 50,30,70,20,40,60,80"""
    bst = BinarySearchTree()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)
    return bst

# ---------------- tests start here ----------------
def test_empty_tree():
    bst = BinarySearchTree()
    assert bst.inorder() == []
    assert bst.preorder() == []
    assert bst.postorder() == []
    assert bst.level_order() == []
    assert bst.search(10) is False

def test_single_insert_and_search():
    bst = BinarySearchTree()
    bst.insert(42)
    assert bst.search(42) is True
    assert bst.search(7) is False
    assert bst.inorder() == [42]
    assert bst.preorder() == [42]
    assert bst.postorder() == [42]
    assert bst.level_order() == [42]

def test_insert_and_search(sample_bst):
    # existing values
    for v in [20, 40, 60, 80]:
        assert sample_bst.search(v) is True
    # non‑existing values
    for v in [10, 45, 90, 0]:
        assert sample_bst.search(v) is False

def test_inorder(sample_bst):
    expected = [20, 30, 40, 50, 60, 70, 80]
    assert sample_bst.inorder() == expected

def test_preorder(sample_bst):
    expected = [50, 30, 20, 40, 70, 60, 80]
    assert sample_bst.preorder() == expected

def test_postorder(sample_bst):
    expected = [20, 40, 30, 60, 80, 70, 50]
    assert sample_bst.postorder() == expected

def test_level_order(sample_bst):
    expected = [50, 30, 70, 20, 40, 60, 80]
    assert sample_bst.level_order() == expected

def test_duplicate_insert():
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    original_inorder = bst.inorder()

    # inserting duplicates should not change the tree
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    assert bst.inorder() == original_inorder
    # searching should still find them
    assert bst.search(10) is True

def test_insert_incomparable_key():
    bst = BinarySearchTree()
    with pytest.raises(TypeError):
        bst.insert(Uncomparable())

def test_insert_none_key():
    bst = BinarySearchTree()
    # None < None raises TypeError, so the validation should catch it
    with pytest.raises(TypeError):
        bst.insert(None)

def test_search_incomparable_key():
    bst = BinarySearchTree()
    bst.insert(1)
    with pytest.raises(TypeError):
        bst.search(Uncomparable())