#!/usr/bin/python3
"""Defination of a class Node."""


class Node:
    """A class that defines a node of a linked list"""
    def __init__(self, data, next_node=None):
        """
        Initialize a Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data value of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the value of the node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class to represent a singly linked list
    """
    def __init__(self):
        """
        Initialize singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new node to the singly linked list
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return ('\n'.join(nodes))
