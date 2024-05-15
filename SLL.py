""" Singly Linked List Implementation """
class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = None

class SLL:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start = n
    def insert_at_end(self,data):
        

