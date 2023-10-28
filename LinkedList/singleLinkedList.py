# Node represents individual node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# A class to represent a linked list itself
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        current = self.head
        if self.isEmpty():
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
        appendedNode = Node(data)
        current.next = appendedNode

    def prepend(self, data):
        # add at beginning of list
        # base case 1: check if head exist
        if self.isEmpty():
            self.head = Node(data)
        else:
            oldHead = self.head
            newHead = Node(data)
            newHead.next = oldHead
            self.head = newHead
        return

    def insert(self, data, position):
        # add at a particular position| position starts from 0
        index = 0
        if self.head == None:
            return "Cannot insert in empty list"
        if position > self.length() or position < 0:
            return "Out of bound"
        currentNode = self.head
        while index < position:
            currentNode = currentNode.next
            index += 1
        newNode = Node(data)
        newNode.next = currentNode.next
        currentNode.next = newNode
        return

    def delete(self, data):
        # delete a particular element
        pass

    def deleteAtPosition(self, position):
        # delete at a particular position
        pass

    def search(self, data):
        # search for a particular element
        pass

    def reverse(self):
        # reverse the linked list
        pass

    def length(self):
        # return length of linked list
        len = 0
        currentNode = self.head
        if currentNode == None:
            return 0
        else:
            while currentNode:
                len += 1
                currentNode = currentNode.next
        return len

    def getNthNode(self, position):
        # return the nth node
        pass

    def display(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" =>")
            currentNode = currentNode.next
        print()


# utility functions
def getRandomList(size):
    import random

    randomList = LinkedList()
    for i in range(size):
        randomList.append(random.randint(1, 10))
    return randomList


if __name__ == "__main__":
    print("Implementing Linked List\n Some random list:\n")
    myList = getRandomList(3)
    myList.display()
    print("Appending 10 the the list")
    myList.append(10)
    myList.display()
    print("Prepending 20 to the list")
    myList.prepend(20)
    myList.display()
    print(f"The length of list is: {myList.length()}")
