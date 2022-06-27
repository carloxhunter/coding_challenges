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
        self.data = data,
        self.next=next

class DoubleNode:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

#they both quite similar, node and method differs
class SimpleLinkedList:
    def __init__(self):
        self.head = None #actually the first element

class DoubleLinkedList:
    def __init__(self):
        self.head = None #actually the first element

