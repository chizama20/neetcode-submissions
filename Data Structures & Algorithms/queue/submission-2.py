class ListNode:

    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head is None

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        if self.isEmpty():
            self.head = self.tail = newNode
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        val = self.tail.val

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return val
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
            
        val = self.head.val

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return val