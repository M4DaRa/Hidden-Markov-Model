class Node:
    def __init__(self, n = 0):
        self.data = n
        self.next = None #NULL

class SLL: 
    def __init__(self):
        self.head = None
        self.size = 0

    
    def create(self):
        if self.size > 0:
            print("Linked List already created ")
            return False


        print("Creating a singly linked list")
        ch = 'y'
        while ch == 'y':

           
            x = int(input("Enter value for node "))
            n = Node(x)

            
            if self.head is None:
                self.head = n
            else:
                shadow.next = n

            
            self.size +=1

            
            shadow = n

            
            ch = input("create more nodes (y/n) : ")

    def count(self):
        return self.size

    def display(self):
        if self.size == 0:
            print("List is Empty")
        else:
            print()
            p = self.head
            while p is not None:
                print(p.data, end=" ")
                p = p.next 


def main():
   
    mylist = SLL()

    
    mylist.create()

    print("Number of nodes in SLL : ", mylist.count())

    mylist.display()

main()