import pytest
from Basic.linked_list import SinglyLinkedList


def test_insert_and_to_list():
    sll = SinglyLinkedList()
    sll.insert_at_head(1)
    sll.insert_at_head(2)
    sll.insert_at_head(3)
    assert sll.to_list() == [3, 2, 1]


def test_delete_at_head():
    sll = SinglyLinkedList()
    sll.insert_at_head(10)
    sll.insert_at_head(20)
    assert sll.delete_at_head() == 20
    assert sll.to_list() == [10]


def test_delete_from_empty():
    sll = SinglyLinkedList()
    with pytest.raises(IndexError):
        sll.delete_at_head()


def test_search():
    sll = SinglyLinkedList()
    sll.insert_at_head("a")
    sll.insert_at_head("b")
    assert sll.search("a") is True
    assert sll.search("z") is False
