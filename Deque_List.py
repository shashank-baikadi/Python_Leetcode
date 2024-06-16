#define a class Deque to implement deque using list . define __init__() method to create a empty list object as instanc eobject menber of deque
class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items.pop(0) 
    def delete_rear(self):
        if self.is_empty():
            return "Deque is empty"
        else:
            self.items.pop()
    def get_front(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items[0]
    def get_rear(self):
        if self.is_empty():
            return "Deque is empty"
        return self.items[-1]
    def size(self):
        return len(self.items)
    
d=Deque()
d.insert_front(10)
d.insert_front(20)
d.insert_rear(30)
print(d.get_front())
print(d.get_rear())
print(d.size())
