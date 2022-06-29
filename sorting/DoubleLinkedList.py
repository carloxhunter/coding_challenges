#usare solo >= 0 ya que enrealidad no aftecta esa pega extra en el pensamiento
#del algoritmo

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


class DoubleNode:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    def printself(self):
        print('data',self.data)
              

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


DoubleL2=DoubleLinkedList()
DoubleL2.push(6)
DoubleL2.push(5)
DoubleL2.push(4)
DoubleL2.pushTop(11)
DoubleL2.printList()

