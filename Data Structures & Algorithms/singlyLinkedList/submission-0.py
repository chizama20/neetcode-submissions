class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if not curr:
            return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        
        if not self.head:
            self.head = newNode
            return

        curr = self.head
        while curr.next:
            curr = curr.next 
        curr.next = newNode 

    def remove(self, index: int) -> bool:
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        prev = None

        while curr and index > 0:
            prev = curr
            curr = curr.next
            index -= 1
        if not curr:
            return False
        prev.next = curr.next
        return True

    def getValues(self) -> List[int]:
        res = []    
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
