import numpy as np


# QUEUE (List implementation)____________________________________________________________________________

class QueueList:

    def __init__(self):
        self.__queue = []

    def enqueue(self, elem):
        self.__queue.append(elem)

    def dequeue(self):
        self.__queue.pop(0)

    def front(self):
        print(self.__queue[0])

    def is_empty(self):
        return self.__queue == []

    def clear(self):
        self.__queue = []

    def __str__(self):
        rep = ' Front -> [ '
        for i in self.__queue:
            rep = rep + ' ; ' + str(i)
        rep = rep + ' ] <- Rear'
        return rep


# CIRCULAR QUEUE (Array implementation)__________________________________________________________________

class QueueCircular:

    def __init__(self, n):
        self.__queue = np.zeros(n)
        self.__front = 0
        self.__rear = 0
        self.__size = 0

    def enqueue(self, elem):
        if self.__rear == self.__queue.size and self.__front != 0:
            self.__rear = 0
        if not self.is_full():
            self.__queue[self.__rear] = elem
            self.__rear = self.__rear + 1
            self.__size = self.__size + 1
        else:
            print('Queue is full')

    def dequeue(self):
        if self.__front == self.__queue.size:
            self.__front = 0
        if not self.is_empty():
            self.__queue[self.__front] = 0
            self.__front = self.__front + 1
            self.__size = self.__size - 1
        else:
            print('Queue is empty')

    def clear(self, n):
        self.__front = 0
        self.__rear = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__queue.size

    def size(self):
        return self.__size

    def __str__(self):
        string = ' [ '
        for i in range(0, self.__queue.size):
            if i == 0:
                string = string + str(self.__queue[i])
            else:
                string = string + ' ; ' + str(self.__queue[i])
        string = string + ' ] '
        return str(string)


# DEQUEUE (List implementation)______________________________________________________________________

class DequeList:

    def __init__(self):
        self._deque = []

    def isEmpty(self):
        return self._deque == []

    def addFront(self, elem):
        self._deque.insert(0, elem)

    def addRear(self, elem):
        self._deque.append(elem)

    def removeFront(self):
        if not self.isEmpty():
            elem = self._deque.pop(0)
            return elem
        else:
            print("Queue is empty")

    def removeRear(self):
        if not self.isEmpty():
            elem = self._deque.pop()
            return elem
        else:
            print("Queue is empty")

    def clear(self):
        self._deque = []

    def __str__(self):
        rep = ' Front -> [ '
        con = False
        for i in self._deque:
            if con is True:
                rep = rep + ' ; ' + str(i)
            else:
                rep = rep + ' ' + str(i)
                con = True
        rep = rep + ' ] <- Rear'
        return rep


# Ex1: Palindrome words or numbers __________________________________________________________________

def is_palindrome(x):
    deq = DequeList()
    for i in x:
        deq.addFront(i)
    for i in range(0, int(len(deq._deque) / 2)):
        if deq.removeFront() != deq.removeRear():
            return False
    return True


# Ex2: Social Security Queue ________________________________________________________________________

# input ----> ('InNumber', Condition (True or False))
    # Ex1 - ('352343514', False) - Users that do not have any disability
    # Ex2 - ('534525355', True)  Users that have one or more disabilities


class SSQ:

    def __init__(self):
        self.__regular = QueueList()
        self.__priority = QueueList()

    def dequeue(self):
        if self.__priority.is_empty():
            self.__regular.dequeue()
        else:
            self.__priority.dequeue()

    def enqueue(self, person):
        if person[1]:
            self.__priority.enqueue(person[0])
        else:
            self.__regular.enqueue((person[0]))

    def clear(self):
        self.__priority.clear()
        self.__regular.clear()

    def isEmpty(self):
        return self.__regular.is_empty() and self.__regular.is_empty()

    def front(self):
        if self.__priority.is_empty():
            self.__regular.front()
        else:
            self.__priority.front()


