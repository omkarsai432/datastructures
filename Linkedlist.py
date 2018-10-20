class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


    def countnodes(head):
        count = 1
        current = head
        while current.next is not None:
            current = current.next
            count += 1
            if count == 2:
                break
        return count


nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print("This linked list's length is:")
print(Node.countnodes(nodeA))
