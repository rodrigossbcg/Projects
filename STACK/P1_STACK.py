import numpy as np
import webbrowser


# STACK (List implementation)______________________________________________________________________________

class StackList:

    def __init__(self):
        self.__stack = []
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def clear(self):
        self.__stack = []

    def push(self, elem):
        self.__stack.append(elem)
        self.__size = self.__size + 1

    def pop(self):
        if not self.is_empty():
            elem = self.__stack.pop()
            self.__size = self.__size - 1
            return elem
        raise IndexError('Stack is empty')

    def peek(self):
        if not self.is_empty():
            return self.__stack[-1]
        raise IndexError('Stack is empty')

    def size(self):
        return self.__size


# STACK (Array implementation)_____________________________________________________________________________

class StackArray:

    def __init__(self, n):
        self.__stack = np.zeros(n)
        self.__curr = 0     # this represents the current stack position
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return len(self.__stack) == self.__size

    def clear(self):
        self.__size = 0
        self.__curr = 0

    def push(self, elem):
        if not self.is_full():
            self.__stack[self.__curr] = elem
            self.__curr = self.__curr + 1
            self.__size = self.__size + 1
        else:
            raise IndexError('Stack is full')

    def pop(self):
        if not self.is_empty():
            elem = self.__stack[self.__curr - 1]
            self.__curr = self.__curr - 1
            self.__size = self.__size - 1
            return elem

    def peek(self):
        return self.__stack(self.__curr - 1)

    def size(self):
        return self.__size


# Ex1: Book stack___________________________________________________________________________________________

book = StackList()
book.push(('1984', 'George Orwell'))                           # add book to stack
book.push(('Problem solving using python', 'Miller Ranum'))    # add book to stack
book.push(('Permanent Record', 'Edward Snowden'))              # add book to stack
book.pop()                                                     # remove 'permanent record'
book.push(('Lusíadas', 'Luís de Camões'))                      # add book
book.push(('The stranger', 'Albert Camus'))                    # add book to stack
book.peek()                                                    # read cover of 'The stranger'
book.pop()                                                     # remove 'The stranger'
book.size()                                                    # count the number of books the stack
book.clear()                                                   # take all books out of the stack


# Ex2: Web browsing_____________________________________________________________________________________________

class WebBrowser:

    def __init__(self):
        self.__left = StackList()
        self.__current_url = 0
        self.__right = StackList()

    def new_url(self, url):
        if self.__current_url == 0:
            self.__current_url = url
        else:
            self.__left.push(self.__current_url)
            self.__current_url = url

    def backwards(self):
        if not self.__left.is_empty():
            self.__right.push(self.__current_url)
            self.__current_url = self.__left.pop()
            return self.__current_url

    def forwards(self):
        if not self.__right.is_empty():
            self.__left.push(self.__current_url)
            self.__current_url = self.__right.pop()
            return self.__current_url

    def exit(self):
        self.__left.clear()
        self.__current_url = 0
        self.__right.clear()


def command():
    w = WebBrowser()
    url = input('Enter url:')
    w.new_url(url)
    webbrowser.open(url, new=0)
    commands = input('n - new url | b - backwards | f - forward | e - exit')
    while commands != 'e':
        if commands == 'n':
            url = input('Enter url:')
            w.new_url(url)
            webbrowser.open(url, new=0)
        if commands == 'b':
            webbrowser.open(w.backwards(), new=0)
        if commands == 'f':
            webbrowser.open(w.forwards(), new=0)
        commands = input('n - new url | b - backwards | f - forward | e - exit')
    w.exit()
