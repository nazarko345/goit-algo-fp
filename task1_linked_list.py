"""Завдання 1. Однозв'язний список: реверс, сортування злиттям, об'єднання."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None


class LinkedList:
    def __init__(self, values: Iterable[int] = ()):
        self.head: Optional[Node] = None
        for value in values:
            self.append(value)

    def append(self, value: int) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def to_list(self) -> list[int]:
        result, current = [], self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __str__(self) -> str:
        return " -> ".join(map(str, self.to_list())) + " -> None"


def reverse_linked_list(head: Optional[Node]) -> Optional[Node]:
    """Реверсує список, змінюючи посилання між вузлами (O(n), O(1))."""
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


def merge_sorted_nodes(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    """Об'єднує два відсортовані ланцюги без створення копій вузлів."""
    dummy = Node(0)
    tail = dummy
    while a and b:
        if a.value <= b.value:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a if a else b
    return dummy.next


def merge_sort(head: Optional[Node]) -> Optional[Node]:
    """Сортування злиттям однозв'язного списку: O(n log n)."""
    if head is None or head.next is None:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    right = slow.next
    slow.next = None
    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right)
    return merge_sorted_nodes(left_sorted, right_sorted)


if __name__ == "__main__":
    linked = LinkedList([7, 2, 9, 1, 5, 3])
    print("Початковий список:", linked)
    linked.head = merge_sort(linked.head)
    print("Після сортування:", linked)
    linked.head = reverse_linked_list(linked.head)
    print("Після реверсу:", linked)

    first = LinkedList([1, 4, 7])
    second = LinkedList([2, 3, 8])
    merged_head = merge_sorted_nodes(first.head, second.head)
    merged = LinkedList()
    merged.head = merged_head
    print("Об'єднання двох відсортованих списків:", merged)
