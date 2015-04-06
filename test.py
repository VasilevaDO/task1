class Stack :
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return (self.items == [])
    def __del__(self):
            while not self.is_empty():
                self.pop()

