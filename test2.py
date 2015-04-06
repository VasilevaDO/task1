from test import Stack 

class Test :
    def test1(self):
        s = Stack()
        s.push(54)
        s.push(45)
        s.push("+")
        while not s.is_empty():
            print s.pop()

s = Test()
s.test1()

