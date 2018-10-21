class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.data = None
    
    def insertatending(self,newdata):
       head = self.data
       while head is not None:
           print(head.data)
           head = head.next
           if head is None:
               newnode = Node(newdata)
               head = newnode
               print(head.data)
               break
list = linkedlist()
list.data = Node("Mon")
N2 = Node("Tue")
N3 = Node("Wed")

list.data.next = N2
N2.next = N3

list.insertatending("sun")
