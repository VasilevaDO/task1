class Stack:
    
    def __init__(self):
        
        self.items = [None]
        self.first = 0
        self.latest = 0
        self.stack_size = 1
        self.number_of_elements = 0
        self.remove_constant = 4  # power of two
    
    def __str__(self):
        return str(self.items)
    
    def isEmpty(self):
        try:
            # print('           ',self.first)
            return self.items[self.first] == None
        except IndexError:
            self.first = 0
            # print('           ',self.first)
            return self.items[self.first] == None

    def __add_element(self, item):
        self.items[self.latest] = item
        self.number_of_elements += 1
        self.latest += 1
    
    def remove_element(self):
        x = self.items[self.first]
        self.items[self.first] = None
        self.first += 1
        self.number_of_elements -= 1
        if self.number_of_elements * \
                self.remove_constant <= self.stack_size and self.stack_size > 1:
            if self.first >= self.latest:
                self.items = self.items[self.first:] + self.items[:self.latest]
            else:
                self.items = self.items[self.first:self.latest]
                self.stack_size //= self.remove_constant
                self.latest = self.number_of_elements
            
                self.first = 0
            # print(self.stack_size)
        # print(self.stack_size,self.first,self.latest)
        return x

    def push(self, item):
        try:
        # print(self.items)
        # print(item)
            if self.items[self.latest] == None:
                return self.add_element(item)
            else:
                return self.create_new_items(item)
                #print('Stack overflow!')
        except IndexError:
            self.latest = 0
            if self.items[self.latest] == None:
                return self.add_element(item)
            else:
                #print('Stack overflow!')
                    return self.create_new_items(item)

    def pop(self):
        try:
            # print(self.items)
            if self.items[self.first] != None:
                self.remove_element()
            else:
                print(self.peek())
        except IndexError:
            self.first = 0
            if self.items[self.first] != None:
                self.remove_element()
            else:
                print(self.peek())

    def peek(self):
        if self.items[self.first] != None:
            return self.items[self.first]
        else:
            return 'Stack is empty!'
                
    def create_new_items(self, item):

        self.latest = self.stack_size
    
        self.items = self.items[
            self.first:] + self.items[:self.first] + [None] * self.stack_size
        self.stack_size *= 2
        self.first = 0
        
        return self.push(item)


s = Stack()
for i in range(12):
    s.push(i)
    print(s)
for i in range(13):
    s.pop()
    print(s)
for i in range(50, 55):
    s.push(i)
    print(s)

# s.push(156)
# print(s)
'''while not s.isEmpty():
    print(s.pop())'''