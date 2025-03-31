class Node:
    def __init__(self, value: str):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def length(self) -> int:
        return self._length

    def append(self, element: str) -> None:
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self._length:
            raise IndexError("Index out of range")

        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self._length == 0:
                self.tail = new_node
        elif index == self._length:
            self.append(element)
            return
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node
        self._length += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        if index == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self._length - 1:
            value = self.tail.value
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            value = current.value
            current.prev.next = current.next
            current.next.prev = current.prev

        self._length -= 1
        return value

    def deleteAll(self, element: str) -> None:
        current = self.head
        while current:
            if current.value == element:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self._length -= 1
            current = current.next

    def get(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def clone(self) -> "DoublyLinkedList":
        cloned_list = DoublyLinkedList()
        current = self.head
        while current:
            cloned_list.append(current.value)
            current = current.next
        return cloned_list

    def reverse(self) -> None:
        current = self.head
        self.head, self.tail = self.tail, self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev

    def findFirst(self, element: str) -> int:
        current = self.head
        index = 0
        while current:
            if current.value == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: str) -> int:
        current = self.tail
        index = self._length - 1
        while current:
            if current.value == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self.head = self.tail = None
        self._length = 0

    def extend(self, elements: 'DoublyLinkedList') -> None:
        current = elements.head
        while current:
            self.append(current.value)
            current = current.next

def demo_list_operations(lst):
    print("Initial length:", lst.length())
    lst.append('A')
    lst.append('B')
    lst.append('C')
    print("After appending A, B, C:", [lst.get(i) for i in range(lst.length())])

    lst.insert('X', 1)
    print("After inserting X at index 1:", [lst.get(i) for i in range(lst.length())])

    lst.delete(2)
    print("After deleting index 2:", [lst.get(i) for i in range(lst.length())])

    lst.deleteAll('X')
    print("After deleting all X:", [lst.get(i) for i in range(lst.length())])

    print("\nTesting get() method:")
    try:
        print("Element at index 0:", lst.get(0))
        print("Element at index 1:", lst.get(1))
        print("Element at out-of-range index 10:", lst.get(10))
    except IndexError as e:
        print("Error:", e)

    print("\nFind first 'A':", lst.findFirst('A'))
    print("Find last 'A':", lst.findLast('A'))

    cloned_list = lst.clone()
    print("Cloned list:", [cloned_list.get(i) for i in range(cloned_list.length())])

    lst.reverse()
    print("Reversed list:", [lst.get(i) for i in range(lst.length())])

    new_list = lst.clone()
    new_list.append('Y')
    new_list.append('Z')

    print("New list before extending:", [new_list.get(i) for i in range(new_list.length())])

    lst.extend(new_list)
    print("After extending:", [lst.get(i) for i in range(lst.length())])

    new_list.append('W')
    print("After modifying new_list:", [new_list.get(i) for i in range(new_list.length())])
    print("Original list after new_list modification:", [lst.get(i) for i in range(lst.length())])

    lst.clear()
    print("After clearing:", lst.length())

dl_list = DoublyLinkedList()
print("Demonstrating DoublyLinkedList:")
demo_list_operations(dl_list)

