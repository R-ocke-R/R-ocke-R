class Node:
    
    lineage = {'Phylum':'Chordata', 'Class':'Mammalia', 'Species':'Canis lupus'}
    all_dogs = []

    def __init__(self, fur_color, tail_length):
        self.fur_color = fur_color
        self.tail_length = tail_length
        self.all_dogs.append(self)  # class attributes can be accessed via the instance


    #def __init__(self, data=None, next=None):
    #    self.data=data
    #    self.next=next
    # Initially I structurized the data parameter to always pass a data value in order to initialize a node object, but, now an object with None in instance data is possible.


Bello = Node('white',50)
print('end')
print(Bello.fur_color)
#print(Node.fur_color)

#print(Node.all_dogs)
#print(Node.[0].fur_color)


#learnt a lot of things about python and its classes
''' 
python supports
 > class data members or class variables 
 > also private data members
 > many feautures of object-orieted paradigm are possible here. 
'''