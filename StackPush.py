class stack:
    def __init__(self):
        self.stack = []
    def add(self,data):
        self.data = data
        if data not in self.stack:
            current = data
            while current <= 50:
                print(current)
                self.stack.append(current)
                current += 10
            return True
        else:
            return False
    def peek(self):
        l = len(self.stack)
        print("The last element in stack:",self.stack[l-1])

Pstack = stack()
Pstack.add(10)
Pstack.peek()
            
    
