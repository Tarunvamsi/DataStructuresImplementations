class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head= node

    def print(self):
        if self.head is None:   #blank linked list
            print("Linked list is empty")
            return     
        itr = self.head    #linked list is not blank ,assigning head to the temporary variable
        llstr = ''   #linkedlist string
        while itr: 
            llstr += str(itr.data)+'---->'   #appending the data to the string 
            itr=itr.next    #following the link in the linked list 
        print(llstr)


    def insert_End(self, data):
        if self.head is None:   #blank linked list
            self.head = Node(data, None)  #assign head to created node
            return 
        itr = self.head
        while itr.next :
            itr=itr.next
        itr.next=Node(data,None)  #next of last element is null , so creating a new node       

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_End(data)

    def get_length(self):
        count=0
        itr=self.head  #iterator pointing at the head
        while itr:     #iterator is not none
            count=count+1  
            itr=itr.next
        return count    

    def remove_at(self,index):
        if index<0 or index>= self.get_length(): #if index is negative or more than the lenght
            raise Exception("Invalid index")
        if index==0:    #index is 0, i.e., Pointing to head
            self.head = self.head.next
            return 
        count=0         #count to reach the given index
        itr = self.head
        while itr:
            if count==index-1:#we need to stop the element prior element that we want to remove and we need to modify the links
                itr.next=itr.next.next   #modifying the links
                break 
            itr=itr.next
            count+=1
            
    def insert_at(self,index, data):
        if index<0 or index>= self.get_length(): #if index is negative or more than the lenght
            raise Exception("Invalid index")
        if index==0:
            self.insert_at_begin(data)
            return  
        count=0
        itr=self.head
        while itr:
            if count==index-1: #stoppinfg at the previous element to modify the link 
                node = Node(data,itr.next)  #creating the node to insert at that index
                itr.next=node
                break
            itr=itr.next
            count=count+1




if __name__ == '__main__':
    ll= LinkedList()
    #ll.insert_at_begin(5)
    #ll.insert_at_begin(6)
    #ll.insert_End(1)
    #ll.insert_End(2)
    ll.insert_values(["a","b","c"])
    #ll.remove_at(2)
    ll.insert_at(0,"e")
    ll.print()
    ll.insert_at(2,"f")

    ll.print()
    print("lenght:",ll.get_length())



