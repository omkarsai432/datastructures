class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.data = None
    def printlist(self):
        head=self.data
        while head is not None:
            print(head.data)
            head = head.next
    def insertatbegininig(self,newdata):
        newnode = Node(newdata)
        newnode.next = self.data
        self.data = newnode

list = linkedlist()
list.data = Node("Mon")
N2 = Node("Tue")
N3 = Node("Wed")

list.data.next = N2
N2.next = N3

list.insertatbegininig("Sun")
list.printlist()
