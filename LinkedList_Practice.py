#this is linked list practice

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None      
    def constructor_from_list(self, lis):
        self.head=Node(lis[0])
        h=self.head
        for i in lis[1:]:
            new=Node(i)
            h.next=new
            h=h.next
        return
    def printy(self):
        if self.head==None:
            print("empty")
            return
        else:
            h=self.head
            while h!=None:
                print(h.data)
                h=h.next
        return
    def length(self):
        if self.head==None:
            return 0
        count=0
        #can also make this as an attribute to give O(1) complexity for .length data member, but 
        # that is complex here, coz maybe we have to syncronize it...
        h=self.head
        while h!=None:
            count+=1
            h=h.next
        return count
    def remove(self, pos):
        if pos<=0 or pos>self.length() or self.head==None:
            print("wrong position")
            return
        
        if pos==1:
            self.head=self.head.next
        
        prev=self.head
        h=prev.next
        count=2
        while h!=None and count!=pos:
            #traverse till you reach count==pos
            prev=prev.next
            h=h.next
            count+=1
        
        if count==pos:
            #we have reached the pos to be deleted.
            prev.next=h.next
        return
    def remove_position_without_prev(self, pos):
        if pos<=0 or pos>self.length() or self.head==None:
            print("wrong position")
            return
        if pos==1:
            self.head=self.head.next
        count=1
        h=self.head
        while h!=None and count!=pos-1:
            #traverse till you reach count==pos
            h=h.next
            count+=1
        
        if count==pos-1:
            #we have reached the pos to be deleted.
            h.next=h.next.next
        return

'''print("successful")
new_obj=LinkedList()
new_obj.head=Node("manu")
new_obj.head.next=Node("sharma")
new_obj.printy()
print(new_obj.length())
print('------------')'''
'''obj=LinkedList()
obj.constructor_from_list(['manu ','sharma ', 'is ', 'fucking ', 'smart'])
print(obj.length())
obj.printy()'''

                
class dNode:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data=data
        self.next=next
        self.prev=prev


class doublyLinkedList:
    def __init__(self) -> None:
        self.head=None
    def printy(self):
        if self.head==None:
            print("empty")
            return
        else:
            h=self.head
            while h!=None:
                print(h.data)
                h=h.next
        return


'''obb=doublyLinkedList()
obb.head=dNode(50)
#print(obb.head.data)
next=dNode(100)
obb.head.next=dNode(75,next,obb.head)
next.prev=obb.head.next
obb.printy()'''

obf=LinkedList()
obf.constructor_from_list([1,2,3,4,5,6])
obf.printy()
print("-----")
obf.remove_position_without_prev(7)
obf.printy()