class LinkedList:
    head = None
    class Node:
        def __init__(self, x):
            self.value = x
            self.next = None
    def insert(self,value):
        toAdd = self.Node(value)
        if self.head == None:
            self.head = toAdd
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = toAdd
    def display(self):
        temp = self.head
        if self.head == None:
            print("ERROR : You are trying to Print Empty Linked List")
            return
        while temp.next != None:
            print(temp.value)
            temp = temp.next
        print(temp.value)
    def delete(self,x):
        temp = self.head
        if self.head == None:
            print("ERROR : You are trying to Delete Empty Linked List")
            return
        if temp.value == x:
            self.head = temp.next
            return
        while temp.next.value != x:
            temp = temp.next
            if temp.next == None:
                return
        temp.next= temp.next.next
    def count(self):
        x = 0
        temp = self.head
        if self.head == None:
            return x
        while temp.next != None:
            x = x+1
            temp = temp.next
        return x+1
    def help(self):
        print("""        1.Use insert(value) to Insert Value in linked list
        2.Use delete(Value) to Delete from Node
        3.Use count() to count Number of Elements
        4.Use display() to Display all Elements of Node
        """)
obj = LinkedList()
#print(obj.count())
for x in range(0,10,1):
    obj.insert(x+1)
obj.help()
#obj.delete(9)
#print(obj.count())
#obj.display()