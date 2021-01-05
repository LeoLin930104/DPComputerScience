# Queue is a FIFO Data Stucture
# First In First Out


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, data) -> int:
        n = Node(data)
        if self.is_empty():  # If Queue is Empty
            # There is nothing, so both head and tail are new Node
            self.head = n
            self.tail = n
        else:  # If Queue is not Empty
            # Point tail.next at new Node
            self.tail.next = n
            # Point tail to the new Node
            self.tail = n
        self.length += 1
        return self.length

    def dequeue(self) -> any:
        if self.is_empty():
            raise IndexError("Queue is Empty")
        # Temporarily Store Data
        data = self.head.data
        # Point head to the next Node
        self.head = self.head.next
        self.length -= 1
        return data

    def has_next(self) -> bool:
        return self.head is not None

    def is_empty(self) -> bool:
        return not self.has_next()

    def empty(self) -> bool:
        self.head = None
        self.tail = None

    def __len__(self):
        return self.length


if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.enqueue(i)
    for i in range(10):
        print(f"Data: {q.dequeue()}, Length: {len(q)}")