class queue:
    def __init__(self):
        self.queue = []
    def add(self,data):
        self.data = data
        if data not in self.queue:
            current = data
            while current <= 50:
                print(current)
                self.queue.append(current)
                current += 10
            return True
        else:
            return False
    def printqueue(self):
        print(self.queue)

Pqueue = queue()
Pqueue.add(10)
Pqueue.printqueue()

            
    
