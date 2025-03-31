class ListBasedList:
    def __init__(self):
        self.data = []

    def length(self) -> int:
        return len(self.data)

    def append(self, element: str) -> None:
        self.data.append(element)

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, element)

    def delete(self, index: int) -> str:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data.pop(index)

    def deleteAll(self, element: str) -> None:
        self.data = [x for x in self.data if x != element]

    def get(self, index: int) -> str:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def clone(self) -> "ListBasedList":
        cloned_list = ListBasedList()
        cloned_list.data = self.data[:]
        return cloned_list

    def reverse(self) -> None:
        self.data.reverse()

    def findFirst(self, element: str) -> int:
        try:
            return self.data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str) -> int:
        try:
            return len(self.data) - 1 - self.data[::-1].index(element)
        except ValueError:
            return -1

    def clear(self) -> None:
        self.data.clear()

    def extend(self, elements: "ListBasedList") -> None:
        self.data.extend(elements.data[:])


def demo_list_operations(lst):
    print("Initial length:", lst.length())
    lst.append('A')
    lst.append('B')
    lst.append('C')
    lst.append('A')
    lst.append('D')
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

lb_list = ListBasedList()
print("\nDemonstrating ListBasedList:")
demo_list_operations(lb_list)