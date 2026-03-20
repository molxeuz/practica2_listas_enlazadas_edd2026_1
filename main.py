# Single Linked List
class Node:
    __slots__ = ('__value','__next')
    def __init__(self,value):
        self.__value = value
        self.__next = None
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, new_value):
        if new_value is None:
            raise ValueError("El valor del nodo no puede ser None.")
        self.__value = new_value
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next, Node):
            raise TypeError("El next solo puede ser un objeto Node o None.")
        self.__next = new_next
    def __str__(self):
        return str(self.__value)

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    @property
    def head(self):
        return self.__head
    @property
    def tail(self):
        return self.__tail
    @property
    def size(self):
        return self.__size

# Doubly Linked List
class NodeD:
    __slots__ = ('__value','__next','__prev')
    def __init__(self,value):
        self.__value = value
        self.__next = None
        self.__prev = None
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self,new_value):
        if new_value is None:
            raise ValueError("El valor no puede ser None.")
        self.__value = new_value
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self,node):
        if node is not None and not isinstance(node,NodeD):
            raise TypeError("next debe ser un nodo o None.")
        self.__next = node
    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self,node):
        if node is not None and not isinstance(node,NodeD):
            raise TypeError("prev debe ser un nodo o None.")
        self.__prev = node
    def __str__(self):
        return str(self.__value)

class DoublyLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    @property
    def head(self):
        return self.__head
    @property
    def tail(self):
        return self.__tail
    @property
    def size(self):
        return self.__size
