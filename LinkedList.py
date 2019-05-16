class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.data=None
    def listprint(self):
        head=self.data
        while head is not None:
            print(head.data)
	    print("Some changes")
	    print("git rel")
	    print("git featured")
            head=head.next
list=linkedlist()
list.data=node("Mon")
e2=node("Tue")
e3=node("Wed")

list.data.next=e2
e2.next=e3
list.listprint()
