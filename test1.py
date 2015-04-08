class Stack:
    def __init__(self,stack_size):
        
        self.items = [None]*stack_size
        self.first = 0
        self.latest = 0
        
        
    def isEmpty(self):
        try:
                #print('           ',self.first)
                return self.items[self.first] == None
        except IndexError:
                self.first = 0
                #print('           ',self.first)
                return self.items[self.first] == None
        
    def push(self, item):
        try:
                if self.items[self.latest] == None:
                        self.items[self.latest] = item
                        self.latest+=1
                else:
                        print('Stack overflow!')
        except IndexError:
                self.latest=0
                if self.items[self.latest] == None:
                        self.items[self.latest] = item
                        self.latest+=1
                else:
                        print('Stack overflow!')

    def pop(self):
        try:
                if self.items[self.first] != None:
            
                        x=self.items[self.first]
                        self.items[self.first] = None
                        self.first+=1
                        
                        return x
                else:
                        print('Stack is empty!')
        except IndexError:
                self.first=0
                if self.items[self.first] != None:
                            
                        x=self.items[self.first]
                        self.items[self.first] = None
                        self.first+=1
                                
                        return x
                else:
                        print('Stack is empty!')



    def peek(self):
            if self.items[self.first] != None:
                    return self.items[self.first]
            else:
                    print('Stack is empty!')
        
    def Print(self):
            return self.items




s = Stack(3)	
s.push('hello')

s.push('true')

print(s.pop())

#print(s.peek())
print(s.Print())
s.push(7)
s.push(7)
s.push(7)
s.push(7)
s.push(7)
s.push(7)
print(s.Print())
s.push(3)
print(s.pop())
s.push(1212)
s.pop()
s.pop()
s.pop()
s.pop()
s.push(1212232)
while not s.isEmpty():
    print(s.pop())