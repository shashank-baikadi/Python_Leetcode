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
    def insert_at_start(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n

    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next

    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next  


    # def delete_at_start(self):
    #     if not self.is_empty():
    #         self.start=self.start.next
    #     else:
    #         print('List is empty')

    def delete_first(self):
       if self.start is not None:
           self.start=self.start.next
    
    def delete_last(self):
        if self.start is None:
            print('List is empty')
        elif self.start.next is None:
        # what if we have a single node so we pass that node with none value
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def delete_item(self,data):
        if self.start is None:
            print('List is empty')
        elif self.start.item==data:
            self.start=self.start.next
        else:
            temp=self.start
            while temp.next is not None:
                if temp.next.item==data:
                    break
                temp=temp.next
            if temp.next is None:
                print('Item not found')
            else:
                temp.next=temp.next.next

    






# Driver Code 
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
print()
mylist.delete_item(25)
mylist.print_list()
print()

          
        
        

