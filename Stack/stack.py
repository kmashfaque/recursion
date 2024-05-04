
class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]
    
    def pop(self):
        return self.items.pop()
    
    def push(self,item):
        return self.items.append(item)
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    



stack=Stack()

print(stack.is_empty())
stack.push(4)
stack.push("dog")
stack.push("bird")
stack.push("meow")
print(stack.items)
stack.pop()
print(stack.items)
print(stack.peek())
print(stack.size())    