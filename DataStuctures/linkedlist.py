class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.curr = self.head
        self.length = 0

    def append(self, data) -> int:
        n = Node(data)
        if self.is_empty():
            self.head = n
            self.curr = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.length += 1
        return self.length

    def insert(self, data, index) -> int:
        n = Node(data)
        if index > len(self) or index < 0:
            raise IndexError("Index Out of Bound")
        elif index == len(self):
            return self.append(data)
        elif index == 0:
            n.next = self.curr
            self.curr.prev = n
            self.head = n
        else:
            self.reset_next()
            for i in range(index):
                self.curr = self.curr.next
            n.prev = self.curr.prev
            self.curr.prev.next = n
            n.next = self.curr
            self.curr.prev = n

        self.length += 1
        return self.length

    def remove(self, index) -> int:
        if index >= len(self) or index < 0:
            raise IndexError("Index Out of Bound")
        elif index == len(self) - 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        elif index == 0:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            self.reset_next()
            for i in range(index):
                self.curr = self.curr.next
            self.curr.prev.next = self.curr.next
            self.curr.next.prev = self.curr.prev
        self.length -= 1
        return self.length

    def get_next(self) -> any:
        if not self.has_next():
            raise IndexError("End of List")
        data = self.curr.next.data
        self.curr = self.curr.next
        return data

    def get_prev(self) -> any:
        if not self.has_prev():
            raise IndexError("Front of List")
        data = self.curr.next.data
        self.curr = self.curr.prev
        return data

    def reset_next(self):
        self.curr = self.head

    def has_next(self) -> bool:
        return self.curr.next is not None

    def has_prev(self) -> bool:
        return self.curr.prev is not None

    def is_empty(self) -> bool:
        return self.head is None

    def emptify(self):
        self.head = None
        self.tail = None
        self.curr = None

    def __len__(self) -> int:
        return self.length

    def get_list(self) -> list:
        result = []
        l.reset_next()
        result.append(l.curr.data)
        while l.has_next():
            result.append(l.get_next())
        return result


if __name__ == "__main__":
    l = LinkedList()
    for i in range(10):
        l.append(i)
    l.insert(10, 10)
    l.insert(11, 11)
    l.remove(0)
    print(l.get_list())