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
        
        # currentNode = self.head

        # while True:
        #     if currentNode.nextNode == None:
        #         storagedValue = currentNode.value
        #         currentNode = None
        #         return storagedValue
        #     currentNode = currentNode.nextNode

        if self.head == None:
            return None
        
        savedElement = self.head.nextNode
        self.head = self.head.nextNode.nextNode

        return savedElement.value


    def insert_after(self, index, val):
        """Inserts an val in the list after the provided index. O(n)"""
        raise NotImplementedError

    def remove_element(self, index):
        """Removes element at the provided index. Returns the removed
        element. O(n)"""
        raise NotImplementedError

    def reverse(self):
        """Reverses the direction of the linked list. O(n)"""
        raise NotImplementedError