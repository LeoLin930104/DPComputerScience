class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        # All list would need a head to point to the head
        #  "   "     "     "  " tail "    "   "   "  tail
        #  "   "     "     "  " curr "    "   "   "  current node
        self.head = None
        self.tail = None
        self.curr = self.head
        # Stores Length of the list
        self.length = 0

    def append(self, data) -> int:
        # Creating New Node to hold New Data
        n = Node(data)
        # Case of List is Empty
        if self.is_empty():
            self.head = n
            self.curr = n
            self.tail = n
        # Case of List is Not Empty
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        # Updating Length of List
        self.length += 1
        return self.length

    def insert(self, data, index) -> int:
        # Creating New Node to hold New Data
        n = Node(data)
        # Case of Index targeted is out of Bound
        if index > len(self) or index < 0:
            raise IndexError("Index Out of Bound")
        # Case of Index targeted is the End of List
        elif index == len(self):
            return self.append(data)
        # Case of Index targeted is the Start of List
        elif index == 0:
            n.next = self.head
            self.head.prev = n
            self.head = n
        # Case of Index is within List
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
        # Case of Index targeted is out of Bound
        if index >= len(self) or index < 0:
            raise IndexError("Index Out of Bound")
        # Case of Index targeted is the End of List
        elif index == len(self) - 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        # Case of Index targeted is the Start of List
        elif index == 0:
            self.head.next.prev = None
            self.head = self.head.next
        # Case of Index is within List
        else:
            self.reset_next()
            for i in range(index):
                self.curr = self.curr.next
            self.curr.prev.next = self.curr.next
            self.curr.next.prev = self.curr.prev
        self.length -= 1
        return self.length

    def get_next(self) -> any:
        # Check if Next Node does not Exist
        if not self.has_next():
            raise IndexError("End of List")
        # Displacing curr to next Node
        self.curr = self.curr.next
        # Secure Data
        return self.curr.data

    def get_prev(self) -> any:
        # Check is previous Node does not Exist
        if not self.has_prev():
            raise IndexError("Front of List")
        # Displacing prev to Previous Node
        self.curr = self.curr.prev
        # Secure Data
        return self.curr.data

    def reset_next(self) -> None:
        self.curr = self.head

    def has_next(self) -> bool:
        return self.curr.next is not None

    def has_prev(self) -> bool:
        return self.curr.prev is not None

    def is_empty(self) -> bool:
        return self.head is None and self.tail is None and self.curr is None

    def emptify(self) -> None:
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
    l.remove(0)
    l.insert(10, 9)
    print(l.get_list())