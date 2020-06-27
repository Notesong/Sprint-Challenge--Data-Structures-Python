class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value} -> '
            current_node = current_node.next_node
        return output

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.value
            current_node = current_node.next_node

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    def contains(self, value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False

    def remove_head(self):
        return_value = None
        if self.head is not None:
            return_value = self.head.value
            self.head = self.head.next_node
            self.length -= 1
            if self.length < 2:
                self.tail = self.head
        return return_value

    def get_max(self):
        return max(self) if self.length > 0 else None


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = SinglyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        node = self.storage.remove_head()
        return node


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = SinglyLinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        value = self.storage.remove_head()
        return value


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        does_contain = False
        if self.value == target:
            does_contain = True
        elif target < self.value:
            if self.left is None:
                does_contain = False
            else:
                does_contain = self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                does_contain = False
            else:
                does_contain = self.right.contains(target)
        return does_contain

    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        fn(self.value)
        if self.right:
            self.right.for_each(fn)

    def in_order_print(self, node):
        node.for_each(print)

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while len(queue) > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
