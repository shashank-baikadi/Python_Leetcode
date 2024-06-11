# creating node where we havre 3 sub blocks prev item and next 
#when initial we have none value in prev that means its the first node because we have no refer in prev

#creating a class node have 3 sub blocks prev item and next
class Node:
  def __init__(self,item=None,prev=None,next=None):
    self.prev=prev
    self.item=item
    self.next=next 


#define a class DLL to  implement the doubly linked list with __init__ method and initialise start reference variable 
class DLL:
  def __initi__(self,start=None):
    self.start=start
    
#define a method is_empty to check whether the linked  list is empty in DLL
  def is_empty(self):
    return self.start==None #return true if the linked list is empty otherwise return false
  
  # define a method insert_at_start() to insert an element at the starting of the list
  def  insert_at_start(self,item):

