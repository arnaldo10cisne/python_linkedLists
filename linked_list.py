class Node:

    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    """This is a linked list implementation"""
    def __init__(self):
        self.head = None

    def push_front(self, val):
        """Add a new element to the front of the linked list. O(1)"""
        self.head = Node(val, self.head)

    def get_element(self, index):
        """Returns the value of the element at the provided index. O(n)"""
        
        if self.head == None:
            raise Exception("Linked list is empty")
        
        currentNode = self.head
        for i in range(index):
            if currentNode.nextNode == None:
                raise Exception("index too large")
            currentNode =  currentNode.nextNode
        return currentNode.value

    def count(self):
        """Returns the number of elements in the list. O(1)"""
        
        if self.head == None:
            return 0

        numberOfNodes = 0
        currentNode = self.head

        while True:
            numberOfNodes += 1
            if currentNode.nextNode == None:
                break
            currentNode = currentNode.nextNode
            
        return numberOfNodes

    def pop_front(self):
        """Removes the val from the front of the list and returns the value
        of that val. O(1)"""

        if self.head == None:
            return None
        
        savedElement = self.head.value
        
        self.head = self.head.nextNode

        return savedElement


    def insert_after(self, index, val):
        """Inserts an val in the list after the provided index. O(n)"""
        
        # HEAD -> A(0) -> B(1) -> C(2) -> D(3)
        # insert_after(1, 'F')
        # HEAD -> A(0) -> B(1) -> F(2) -> C(3) -> D(4)

        if self.head == None:
            raise Exception("Linked list is empty")

        currentNode = self.head

        for i in range(index):
            currentNode = currentNode.nextNode

        currentNode.nextNode = Node(val, currentNode.nextNode)

    def remove_element(self, index):
        """Removes element at the provided index. Returns the removed
        element. O(n)"""
        
        if self.head == None:
            raise Exception("Linked list is empty")

        if index == 0:
            return self.pop_front()

        # HEAD -> A(0) -> B(1) -> F(2) -> C(3) -> D(4)
        # remove_element(1)
        # HEAD -> A(0) -> F(1) -> C(2) -> D(3)

        currentNode = self.head

        for i in range(index):
            currentNode = currentNode.nextNode

        savedElement = currentNode

        listOfNodes = currentNode.nextNode

        currentNode = self.head

        for i in range(index-1):
            currentNode = currentNode.nextNode

        currentNode.nextNode = listOfNodes

        return savedElement.value

    def reverse(self):
        """Reverses the direction of the linked list. O(n)"""
        
        if self.head == None:
            raise Exception("Linked list is empty")

        if self.count == 1:
            return

        # HEAD -> A(0) -> B(1) -> C(2) -> D(3) -> E(4) -> F(5)
        # reverse()
        # HEAD -> F(0) -> E(1) -> D(2) -> C(3) -> B(4) -> A(5)

        # currentNode = self.head

        # tail = None

        # for i in range(self.count()):
            
        #     aux = currentNode
        #     aux.nextNode = tail
        #     tail = aux

        #     if currentNode.nextNode != None:
        #         currentNode = currentNode.nextNode

        # self.head = tail
