class Node:
    def __init__(self,data=None,next=None):
        '''Create node '''
        self.data=data
        self.next=next
        
class Linked_list:
    def __init__(self):
        '''set head of linked list'''
        self.head=None
        
    def print(self):
        if self.head is None:
            print('your linked list is empty')
            return
        
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'--->'
            itr=itr.next
        print(llstr)   
    
    def append_left(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def append(self,data):
        if self.head is None:
            node=Node(data,self.head)
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
    def insert_list(self,list):
        self.head=None
        for data in list:
            self.append(data)

    def append_list(self,list):
        for data in list:
            self.append(data)
            
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove(self,index):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        
        elif index==0:
            self.head=self.head.next
            
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                itr.next=itr.next.next
            itr=itr.next
            count+=1
            
    def insert(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')
        elif index==0:
            node=Node(data,self.head)
            self.head=node
            
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
            itr=itr.next
            count+=1
            
        
ll=Linked_list()
ll.append_left(2)
ll.append_left(1)
ll.append(3)
ll.insert_list(['m','n'])
ll.append_list([1,2])
ll.insert(1,'muz')
ll.print()
    
    
            