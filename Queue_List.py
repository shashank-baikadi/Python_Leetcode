# define a class Queue to implement queue data structure using list .define  __init__() method to create  a empty list object as instance object member of queue.
class Queue:
    def __init__(self):
        self.items=[]
        # self.front=None
        # self.rear=None

# define a method is_empty () to check if the queue is empty in Queue class
    def is_empty(self):
        return len(self.items)==0
# define a method enqueue() to add data onto the queue
    def enqueue(self,data):
        self.items.append(data)
# define a method dequeue() to remove front element from the queue
    def dequeue(self):
        if not  self.is_empty():
             self.items.pop(0)# 0 is the index that means its first element
        else:
            raise IndexError("Queue is empty")
        
# '''
#     def get_front(self):
#         return self.items[0]

#     def get_rear(self):
#         return self.items[-1]
# '''

    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue is empty")
        
    def size(self):
        return len(self.items)
    

# Driver code
q1=Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e)

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front element is ",q1.get_front())
print("Rear element is ",q1.get_rear())
print("size of queue is ",q1.size())

try:
    q1.dequeue()
    print("queue has  now ",q1.size(),"elements")
except IndexError as e:
    print(e)