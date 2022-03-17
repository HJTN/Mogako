# 노드 클래스.
# 생성자로 데이터와 포인터를 받는다.
# 포인터가 입력이 안된 경우, 해당 노드가 종단점이라는 의미.
class Node:
    def __init__(self, data, left_pointer=None, right_pointer=None):
        self.left_pointer = left_pointer
        self.data = data
        self.right_pointer = right_pointer

# 링크드리스트 클래스.
# 클래스 객체 생성시 데이터가 존재하지 않는 노드를 생성한다.
# 해당 노드의 포인터가 바로 Head.
class LinkedList(object):
    def __init__(self):
        self.head = Node(None)
        # 링크드리스트의 노드 개수를 저장하는 변수 size.
        self.size = 0

    # idx 위치에 존재하는 노드를 받아온다.
    def get(self, idx):
        # 입력된 인덱스가 링크드리스트 사이즈보다 클 경우, 오류가 발생.
        if idx >= self.size:
            print("Index Error")
            return None
        # 인덱스가 0인 경우, 헤드를 받아오라는 의미
        if idx == 0:
            return self.head
        else:
            node = self.head
            for _ in range(idx):
                node = node.right_pointer
            return node

    # 데이터를 링크드리스트 종단점으로 추가한다.
    def append(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.size += 1
        else:
            node = self.head
            # 종단점의 포인터는 None값을 가짐.
            while node.right_pointer != None:
                node = node.right_pointer

            new_node = Node(data)
            node.right_pointer = new_node
            new_node.left_pointer = node
            self.size += 1

    # 데이터를 idx 위치에 추가한다.
    def insert(self, value, idx):
        if self.size == 0:
            self.head = Node(value)
            self.size += 1
        # idx가 0이라는건, Head 자리에 새로운 데이터를 넣는다는 의미.
        elif idx == 0:
            ############# 수정 필요
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
            # 삽입하려는 idx 이전의 노드의 포인터를 새로운 노드로 설정
            node.pointer = new_node
            # 현재 노드의 포인터를 삽입하려는 idx 이후의 노드로 설정
            new_node.pointer = next_node
            self.size += 1

    # idx 위치의 노드를 삭제한다.
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