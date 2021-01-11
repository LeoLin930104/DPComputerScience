class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head
        # Stores Length of the list
        self.length = 0

    def append(self, data) -> int:
        n = Node(data)
        if self.is_empty():
            # List is empty, so n is first Node
            self.head.next = n
            self.tail.prev = n
            n.prev = self.head
            n.next = self.tail
        else:
            # List is not empty, insert after last Node
            n.next = self.tail
            n.prev = self.tail.prev
            self.tail.prev.next = n
            self.tail.prev = n
        self.length += 1
        return self.length
        # Previous Code
        # def append(self, data) -> int:
        #     # Creating New Node to hold New Data
        #     n = Node(data)
        #     # Case of List is Empty
        #     if self.is_empty():
        #         self.head = n
        #         self.curr = n
        #         self.tail = n
        #     # Case of List is Not Empty
        #     else:
        #         n.prev = self.tail
        #         self.tail.next = n
        #         self.tail = n
        #     # Updating Length of List
        #     self.length += 1
        #     return self.length

    def insert(self, index, data) -> int:
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
            n.next = self.head.next
            n.prev = self.head
            self.head.next.prev = n
            self.head.next = n
        # Case of Index is within List
        else:
            tmp = self.head
            for i in range(index):
                tmp = tmp.next
            n.prev = tmp
            n.next = tmp.next
            tmp.next.prev = n
            tmp.next = n

        self.length += 1
        return self.length

    def remove(self, index) -> int:
        # Case of Index targeted is out of Bound
        if index >= len(self) or index < 0:
            raise IndexError("Index Out of Bound")
        # Case of Index targeted is the End of List
        elif index == len(self) - 1:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
        # Case of Index targeted is the Start of List
        elif index == 0:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        # Case of Index is within List
        else:
            tmp = self.head
            for i in range(index):
                tmp = tmp.next
            tmp.next = tmp.next.next
            tmp.next.prev = tmp
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
        # Displacing curr to next Node
        self.curr = self.curr.prev
        # Secure Data
        return self.curr.data

    def reset_next(self) -> None:
        self.curr = self.head

    def reset_prev(self) -> None:
        self.curr = self.tail

    def has_next(self) -> bool:
        return self.curr.next is not self.tail and self.curr.next is not None

    def has_prev(self) -> bool:
        return self.curr.prev is not self.head or self.curr.prev is not None

    def is_empty(self) -> bool:
        return self.head.next is self.tail

    def emptify(self) -> None:
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.head
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def get_list(self) -> list:
        result = []
        self.reset_next()
        while self.has_next():
            result.append(l.get_next())
        return result


if __name__ == "__main__":
    l = LinkedList()
    for i in range(10):
        l.append(i)
    for i in range(len(l)):
        l.remove(i)
        l.insert(i, i)
    print(l.get_list())