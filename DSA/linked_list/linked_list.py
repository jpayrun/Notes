
class Node:

    def __init__(self, data = None):
        self.head = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node(data=None)

    def push(self, data):
        cur: Node = self.head
        if cur.head is None:
            self.head = Node(data)
        while cur.next:
            cur = cur.next

        cur.head = Node(data)
        
    def __len__(self) -> int:
        res: int = 0
        cur: Node = self.head
        if cur.head is not None:
            res+=1
        while cur.next:
            res+=1
            cur=cur.next
        return res


def main():
    l = LinkedList()
    l.push(7)
    l.push(3)
    print(len(l))

if __name__ == "__main__":
    main()
