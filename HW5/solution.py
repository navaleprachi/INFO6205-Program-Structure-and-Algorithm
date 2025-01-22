
############################################################
# Write code in file solution.py 
# Post� solution.py in Canvas along with 4 screen shots that shows Leetcode has passed. We will not use screen shot to give 100
# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run solution.py file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
               
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################

    # 1. Append: Add data to the end of the linked list and adjust pointers
    def append(self, val):
        new_node = ListNode(val)
        if not self._first:  # List is empty
            self._first = self._last = new_node
        else:
            self._last.next = new_node
            self._last = new_node
        self._len += 1

    # 2. Prepend: Add data to the start of the linked list and adjust pointers
    def prepend(self, val):
        new_node = ListNode(val)
        if not self._first:  
            self._first = self._last = new_node
        else:
            new_node.next = self._first
            self._first = new_node
        self._len += 1

    # 3. Find: Find the element at a specific position in the linked list
    def find(self, index):
        if index >= self._len or index < 0:
            return None
        current = self._first
        for _ in range(index):
            current = current.next
        return current.val if current else None

    # 4a. Delete last: Remove the last element from the linked list and adjust pointers
    def delete_last(self):
        if not self._first: 
            return None
        if self._first == self._last: 
            val = self._first.val
            self._first = self._last = None
        else:
            current = self._first
            while current.next != self._last:
                current = current.next
            val = self._last.val
            self._last = current
            self._last.next = None
        self._len -= 1
        return val

    # 4b. Delete front: Remove the first element from the linked list and adjust pointers
    def delete_first(self):
        if not self._first:
            return None
        val = self._first.val
        self._first = self._first.next
        if not self._first:
            self._last = None
        self._len -= 1
        return val

    # Utility function to get the size of the list
    def size(self):
        return self._len

    # Utility function to check if the list is empty
    def is_empty(self):
        return self._len == 0
  
  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    # Push an element onto the stack
    def push(self, x: int) -> None:
        self._s.append(x)

    # Pop the topmost element from the stack
    def pop(self) -> int:
        return self._s.delete_last()

    # Get the top element of the stack
    def top(self) -> int:
        if self._s._last:
            return self._s._last.val
        return None

    # Check if the stack is empty
    def empty(self) -> bool:
        return self._s.is_empty()


############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    # Push element x to the back of the queue
    def push(self, x: int) -> None:
        self._s.append(x)

    # Remove the element from the front of the queue and return it
    def pop(self) -> int:
        return self._s.delete_first() 

    # Get the front element
    def peek(self) -> int:
        return self._s.find(0) 

    # Return whether the queue is empty
    def empty(self) -> bool:
        return self._s.is_empty() 


############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

     # Insert an element into the circular queue, return True if successful
    def enQueue(self, value: int) -> bool:
        if self._s.size() < self._K:
            self._s.append(value)
            return True
        return False  

    # Delete an element from the circular queue, return True if successful
    def deQueue(self) -> bool:
        if not self._s.is_empty(): 
            self._s.delete_first()
            return True
        return False  

    # Get the front item from the queue
    def Front(self) -> int:
        if self._s.is_empty():
            return -1
        return self._s.find(0)

    # Get the last item from the queue
    def Rear(self) -> int:
        if self._s.is_empty():
            return -1
        return self._s.find(self._s.size() - 1)

    # Check if the queue is empty
    def isEmpty(self) -> bool:
        return self._s.is_empty()

    # Check if the queue is full
    def isFull(self) -> bool:
        return self._s.size() == self._K
 

############################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
    
    # Insert an element at the front of the deque, return True if successful
    def insertFront(self, value: int) -> bool:
        if self._s.size() < self._K:
            self._s.prepend(value) 
            return True
        return False 

    # Insert an element at the rear of the deque, return True if successful
    def insertLast(self, value: int) -> bool:
        if self._s.size() < self._K:
            self._s.append(value)
            return True
        return False 

    # Delete the front element, return True if successful
    def deleteFront(self) -> bool:
        if not self._s.is_empty():
            self._s.delete_first()
            return True
        return False 

    # Delete the last element, return True if successful
    def deleteLast(self) -> bool:
        if not self._s.is_empty(): 
            self._s.delete_last()
            return True
        return False 

    # Get the front element
    def getFront(self) -> int:
        if self._s.is_empty(): 
            return -1
        return self._s.find(0)

    # Get the rear element
    def getRear(self) -> int:
        if self._s.is_empty():
            return -1
        return self._s.find(self._s.size() - 1)

    # Check if the deque is empty
    def isEmpty(self) -> bool:
        return self._s.is_empty()

    # Check if the deque is full
    def isFull(self) -> bool:
        return self._s.size() == self._K