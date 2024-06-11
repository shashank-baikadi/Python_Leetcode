# creating node where we havre 3 sub blocks prev item and next 
#when initial we have none value in prev that means its the first node because we have no refer in prev

#creating a class node have 3 sub blocks prev item and next
class Node:
  def __init__(self,prev=None,item=None,next=None):
    self.prev=prev
    self.item=item
    self.next=next 


#define a class DLL to  implement the doubly linked list with __init__ method and initialise start reference variable 
class DLL:
  def __init__(self,start=None):
    self.start=start
    
#define a method is_empty to check whether the linked  list is empty in DLL
  def is_empty(self):
    return self.start==None #return true if the linked list is empty otherwise return false
  
  # define a method insert_at_start() to insert an element at the starting of the list

  #note- first  node we have in that we have prev =None  we have item=data and in next we should keep next  node reference 
  def insert_at_start(self,data):
    n=Node(None,data,self.start)
    if not self.is_empty():
         self.start.prev=n #if the linked list is not empty then we have to set the previous reference of the first node to the new node
    self.start=n #set the start reference to the new node

  #define a method insert_at_last() to insert an element at the end of the list .......so we use traversing to reach the end of the list using temp reference variable
  

  def insert_at_last(self,data):
    temp=self.start
    if self.start!=None:
      while temp.next!=None:
        temp=temp.next
      n=Node(temp,data,None)
      if temp==None:
        self.start=n
      else:
        temp.next=n

#define a search() method to search an element in the list
  def search(self,data):
    temp=self.start
    while temp != None:
      if temp.item==data:
        return temp
      else :
        temp=temp.next
    return None   

# define a method insert_after() to insert an element after a given node in the list
  def insert_after(self,temp,data):
    if temp is not None:
      n=Node(temp,data,temp.next)
      if temp.next is not None:
        temp.next.prev=n
      temp.next=n  
# print all the elements of the list
  def print_list(self):
    temp=self.start
    while temp!=None:
      print(temp.item,end=' ')
      temp=temp.next
    print()

  def delete_first(self):
    if self.start is not None:
      self.start=self.start.next
      if self.start is not None:
        self.start.prev=None

  def delete_last(self):
    if self.start is not None:
      pass
    elif self.start.next is None:
      self.start=None
    else:
      temp=self.start
      while temp.next.next is not None:
        temp=temp.next
      temp.prev.next=None

  def delete_item(self,data):
    if self.start is None:
      pass
    elif self.start.next is None:
      if self.start.item==data:
        self.start=None
    else:
      temp=self.start
      if temp.item==data:
        self.start=temp.next
        temp.next.prev=None
      else:
        while temp is not None:
          if temp.item==data:
            if temp.next is not None:
              temp.prev.next=temp.next
            if temp.next is not None:  
              temp.next.prev=temp.prev
            else:
              self.start=temp.next  
            break  
          temp=temp.next
# if u want to create a iterator object you need to create iterator class 
  def __iter__(self):
     return DLLiterator(self.start) #return the iterator object
class DLLiterator:
  def __init__(self,start):
    self.current=start
  def __iter__(self):
    return self
  def __next__(self):
    if not self.current:
        raise StopIteration
    data = self.current.item
    self.current=self.current.next
    return data
  
mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),15)
for x in mylist:
  print(x,end=" ")
print()