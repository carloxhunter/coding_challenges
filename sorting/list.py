#SelectionSort
#BubbleSort
#RecursiveBubbleSort
#InsertionSort
#RecursiveInsertionSort
#MergeSort
#IterativeMergeSort
#QuickSort
#IterativeQuickSort
#HeapSort
#CountingSort
#RadixSort
#BucketSort
#ShellSort
#TimSort
#CombSort
#PigeonholeSort
#CycleSort
#CocktailSort
#StrandSort
#BitonicSort
#PancakeSort
#InsertionSort
#BinaryInsertionSort
#BogoSort or Permutation Sort
#GnomeSort
#SleepSort
#StoogeSort
#TagSort


class SimpleNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next=next
    def printself(self):
        print('data',self.data)

class DoubleNode:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    def printself(self):
        print('data',self.data)

#they both quite similar, yet node and method differs
class SimpleLinkedList:
    def __init__(self):
        self.head = None #actually the first element
    def printList(self):
        print('SimpleLinkedList')
        node = self.head
        if not node:print('[]')
        else:
            while node:
                node.printself()
                node = node.next
    def push(self, data):
        node=self.head
        if not node: self.head=SimpleNode(data)
        else:
            while node.next:
                node=node.next
            #this should be the last node since the previous loop didnt go in coz
            #node.next is None
            node.next=SimpleNode(data)
            

class DoubleLinkedList:
    def __init__(self):
        self.head = None #actually the first element
        self.tail = None
    def printList(self):
        print('Doubple Linked List')
        node = self.head
        if not node:print('[]')
        else:
            while node:
                node.printself()
                node=node.next
    def push(self, data):
        node=self.head
        if not node: 
            theNode=DoubleNode(data)
            self.head=theNode
            self.tail=theNode
        else:
            while node.next:
                node=node.next
            endNode = DoubleNode(data,node)
            node.next=endNode
            self.tail=endNode
    def pushTop(self,data):
        node=self.tail
        if not node: 
            theNode=DoubleNode(data)
            self.head=theNode
            self.tail=theNode
        else:
            while node.prev:
                node=node.prev
            firstNode=DoubleNode(data,None,node)
            self.head=firstNode


        
SimpleL1=SimpleLinkedList()
SimpleL1.push(6)
SimpleL1.push(5)
SimpleL1.push(4)
SimpleL1.printList()

DoubleL2=DoubleLinkedList()
DoubleL2.push(6)
DoubleL2.push(5)
DoubleL2.push(4)
DoubleL2.pushTop(11)
DoubleL2.printList()

