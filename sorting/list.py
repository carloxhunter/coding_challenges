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
        self.elements = 0
    def printList(self):
        print('SimpleLinkedList')
        node = self.head
        if not node:print('[]')
        else:
            while node:
                node.printself()
                node = node.next
    def push(self, data):
        self.elements+=1
        node=self.head
        if not node: self.head=SimpleNode(data)
        else:
            while node.next:
                node=node.next
            #this should be the last node since the previous loop didnt go in coz
            #node.next is None
            node.next=SimpleNode(data)
    def select_ith(self,ith):
        if not self.head: return None
        elif ith >= self.elements or ith < 0: return None
        else:
            C=0
            node=self.head
            while node.next and C!= ith:
                node=node.next
                C+=1
            return node
    def getMax(self):
        if not self.head: return None
        else:
            M=-1
            i=-1
            C=0
            node = self.head
            nodeReturn = None
            while node:
                if node.data > M:
                    M = node.data
                    i = C
                    nodeReturn=node
                node=node.next
                C+=1
            return (nodeReturn, i)
    def getMin(self):
        if not self.head: return None
        else:
            m=99999999
            i=-1
            C=0
            node = self.head
            nodeReturn = None
            while node:
                if node.data < m:
                    m = node.data
                    i = C
                    nodeReturn=node
                node=node.next
                C+=1
            return (nodeReturn, i)   
    def helper_popMax(self):
        if not self.head: return None
        else:
            node = self.head
            prevNode = None
            nodeReturn = None
            prevnodeReturn = None
            M=-1   
            while node:
                if node.data > M:
                    M = node.data
                    nodeReturn=node
                    prevnodeReturn=prevNode
                prevNode=node
                node=node.next
            return prevnodeReturn,nodeReturn

                

            

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
SimpleL1.push(0)
SimpleL1.push(15)
SimpleL1.push(5)
SimpleL1.push(4)
SimpleL1.push(13)
SimpleL1.printList()

DoubleL2=DoubleLinkedList()
DoubleL2.push(6)
DoubleL2.push(5)
DoubleL2.push(4)
DoubleL2.pushTop(11)
#DoubleL2.printList()

#ith=2
#print('ith',ith)
#Anode = SimpleL1.select_ith(ith)
#if Anode: Anode.printself()
#else: print('node not found')


#Max1,ii= SimpleL1.getMax()
#Max1.printself()
#min1= SimpleL1.getMin()
#print(min1)

PrevMax1, CurrentMax1 = SimpleL1.helper_popMax()
print('jiro')
PrevMax1.printself()
CurrentMax1.printself()