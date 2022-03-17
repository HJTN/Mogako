# ��� Ŭ����.
# �����ڷ� �����Ϳ� �����͸� �޴´�.
# �����Ͱ� �Է��� �ȵ� ���, �ش� ��尡 �������̶�� �ǹ�.
class Node:
    def __init__(self, data, left_pointer=None, right_pointer=None):
        self.left_pointer = left_pointer
        self.data = data
        self.right_pointer = right_pointer

# ��ũ�帮��Ʈ Ŭ����.
# Ŭ���� ��ü ������ �����Ͱ� �������� �ʴ� ��带 �����Ѵ�.
# �ش� ����� �����Ͱ� �ٷ� Head.
class LinkedList(object):
    def __init__(self):
        self.head = Node(None)
        # ��ũ�帮��Ʈ�� ��� ������ �����ϴ� ���� size.
        self.size = 0

    # idx ��ġ�� �����ϴ� ��带 �޾ƿ´�.
    def get(self, idx):
        # �Էµ� �ε����� ��ũ�帮��Ʈ ������� Ŭ ���, ������ �߻�.
        if idx >= self.size:
            print("Index Error")
            return None
        # �ε����� 0�� ���, ��带 �޾ƿ���� �ǹ�
        if idx == 0:
            return self.head
        else:
            node = self.head
            for _ in range(idx):
                node = node.right_pointer
            return node

    # �����͸� ��ũ�帮��Ʈ ���������� �߰��Ѵ�.
    def append(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.size += 1
        else:
            node = self.head
            # �������� �����ʹ� None���� ����.
            while node.right_pointer != None:
                node = node.right_pointer

            new_node = Node(data)
            node.right_pointer = new_node
            new_node.left_pointer = node
            self.size += 1

    # �����͸� idx ��ġ�� �߰��Ѵ�.
    def insert(self, value, idx):
        if self.size == 0:
            self.head = Node(value)
            self.size += 1
        # idx�� 0�̶�°�, Head �ڸ��� ���ο� �����͸� �ִ´ٴ� �ǹ�.
        elif idx == 0:
            ############# ���� �ʿ�
            new_node = Node(value)
            self.head.right_pointer
            self.head = Node(value, self.head)
            self.size += 1
        else:
            node = self.get(idx - 1)
            if node == None:
                return

            new_node = Node(value)

            next_node = node.pointer
            # �����Ϸ��� idx ������ ����� �����͸� ���ο� ���� ����
            node.pointer = new_node
            # ���� ����� �����͸� �����Ϸ��� idx ������ ���� ����
            new_node.pointer = next_node
            self.size += 1

    # idx ��ġ�� ��带 �����Ѵ�.
    def delete(self, idx):
        if self.size == 0:
            print("Empty Linked List")
            return
        elif idx >= self.size:
            print("Index Error")
            return
        elif idx == 0:
            self.head = self.head.pointer
            self.size -= 1
        else:
            node = self.get(idx - 1)
            node.pointer = node.pointer.pointer
            self.size -= 1

    def print_linked_list(self):
        node = self.head
        while node:
            if node.pointer != None:
                print(node.data, "-> ", end="")
                node = node.pointer
            else:
                print(node.data)
                node = node.pointer

LL = LinkedList()
LL.append("Data1")
LL.print_linked_list()
LL.append("Data2")
LL.print_linked_list()
LL.append("Data3")
LL.print_linked_list()
LL.insert("Data4", 1)
LL.print_linked_list()

LL.delete(0)
LL.print_linked_list()
LL.delete(2)
LL.print_linked_list()
LL.delete(0)
LL.print_linked_list()