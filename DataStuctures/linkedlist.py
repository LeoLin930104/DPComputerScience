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
        curr = self.head
        for i in range(index):
            curr = curr.next
        if curr.has_next():
            n.next = curr.next
            curr.next.prev = n
        if curr.has_prev():
            n.prev = curr.prev
            curr.prev.next = n
        self.length += 1
        return self.length

    def remove(self, index) -> int:
        pass

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
        result.append(l.head.data)
        for i in range(len(l) - 1):
            result.append(l.get_next())
        return result


if __name__ == "__main__":
    l = LinkedList()
    l.append(4)
    l.append(5)
    l.append(6)

    print(l.get_list())
