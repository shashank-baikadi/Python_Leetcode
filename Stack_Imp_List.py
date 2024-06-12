# define a class stack to implement stack data structure using list .define  __init__() method to create  a empty list object as instance object member of stack.
class Stack:
    def __init__(self):
        self.item=[]          # i have created a list naming item and stored inside it

# define a method is_empty () to check if the stack is empty in Stack class    
    def is_empty(self):
        return len(self.item)==0
    
#in Stack class define  push() method to add data onto the stack
    def push(self,data):
       self.item.append(data) 
# deine pop() method to remove top element from the stack

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is empty")
# in Stack class ,define peek() method to return top element on the stack
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError('stack is empty')
        
#in the stack class, define size() method to return size of the stack that is number of items present in the stack
    def size(self):
        return len(self.item)
    


#s1 is a object

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top element is",s1.peek())
print("element removed is ",s1.pop())
print("Top element is ",s1.peek())
print()

