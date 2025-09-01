"""
Singly Linked List — Nodes linked forward only.

What it is:
    A linear collection of nodes where each node points to the next.

When to use:
    Use when you need efficient O(1) insertion/removal at the head, 
    and random access is not required. Common in streaming or queue-like scenarios.

Complexities:
    insert at head: O(1)
    delete at head: O(1)
    search/access:  O(n)
"""

from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.head is None

    def insert_at_head(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_head(self) -> Any:
        if self.is_empty():
            raise IndexError("Delete from empty list")
        data = self.head.data
        self.head = self.head.next
        return data

    def search(self, target: Any) -> bool:
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def to_list(self) -> list[Any]:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_head(10)
    sll.insert_at_head(20)
    print(sll.to_list())  # [20, 10]
    print(sll.search(10))  # True
    print(sll.delete_at_head())  # 20
    print(sll.to_list())  # [10]
