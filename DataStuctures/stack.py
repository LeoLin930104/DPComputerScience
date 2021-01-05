# Stack is a FILO Data Stucture
# First In Last Out


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, data) -> int:
        # Create New Node
        n = Node(data)
        # Point node.next at whatever head is pointed at
        n.next = self.head
        # Point head at new node
        self.head = n
        # Increase Length
        self.length += 1
        return self.length

    def pop(self) -> any:
        if self.head is None:
            raise IndexError("Stack is Empty")
        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data

    def has_next(self):
        return self.head.next is not None

    def is_empty(self):
        return self.has_next()

    def empty(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length


if __name__ == "__main__":
    s = Stack()
    for i in range(10):
        s.push(i)
    for i in range(10):
        print(f"Data: {s.pop()}, Length: {len(s)}")