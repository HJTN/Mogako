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
class DoublyLinkedList(object):
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
            new_node = Node(value)
            self.head.left_pointer = new_node
            new_node.right_pointer = self.head
            self.head = new_node
            self.size += 1
        elif idx == self.size:
            node = self.get(idx - 1)
            if node == None:
                return

            new_node = Node(value)
            new_node.left_pointer = node
            node.right_pointer = new_node
            self.size += 1
        else:
            node = self.get(idx - 1)
            if node == None:
                return

            new_node = Node(value)

            next_node = node.right_pointer
            # 삽입하려는 idx 이전의 노드의 포인터를 새로운 노드로 설정
            node.right_pointer = new_node
            new_node.left_pointer = node
            # 현재 노드의 포인터를 삽입하려는 idx 이후의 노드로 설정
            new_node.right_pointer = next_node
            next_node.left_pointer = new_node
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
            if self.size == 1:
                self.head = Node(None)
            else:
                next_node = self.head.right_pointer
                next_node.left_pointer = None
                self.head = next_node
            self.size -= 1
        elif (idx + 1) == self.size:
            node = self.get(idx - 1)

            node.right_pointer = node.right_pointer.right_pointer
            self.size -= 1
        else:
            node = self.get(idx - 1)

            node.right_pointer.right_pointer.left_pointer = node
            node.right_pointer = node.right_pointer.right_pointer
            self.size -= 1

    def get_size(self):
        return self.size

    def print_linked_list(self):
        node = self.head
        while node:
            if node.right_pointer != None:
                print(node.data, "-> ", end="")
                node = node.right_pointer
            else:
                print(node.data)
                node = node.right_pointer
    
    def print_reverse_linked_list(self):
        node = self.head
        while node.right_pointer != None:
            node = node.right_pointer
        
        while node:
            if node.left_pointer != None:
                print(node.data, "-> ", end="")
                node = node.left_pointer
            else:
                print(node.data)
                node = node.left_pointer

# Doubly Linked List 생성
DLL = DoublyLinkedList()

while(1):
    command = input("명령어를 입력하세요(도움말: help 입력): ")

    if command == 'help':
        print(" \
            append: N개의 데이터 한 번에 추가\n \
            insert: 특정 위치에 데이터 추가\n \
            delete: 특정 위치의 데이터 삭제\n \
            delete_all: 데이터 전부 삭제\n \
            print: DLL에 있는 데이터 출력\n \
            print_rev: DLL에 있는 데이터 역순으로 출력\n \
            exit: 프로그램 종료\n \
        ")

    elif command == 'append':
        # Data 수 입력
        data_num = int(input("추가할 데이터의 양을 입력하세요: "))

        # Data 자동 생성
        data_list = []
        for idx in range(1, data_num+1):
            data = f'Data{idx}'
            data_list.append(data)

        # DLL에 data 입력
        for idx in range(data_num):
            DLL.append(data_list[idx])

    elif command == 'insert':
        position, value = input("추가할 데이터의 위치와 값을 입력하세요: ").split()
        DLL.insert(value, int(position))

    elif command == 'delete':
        position = int(input("삭제할 데이터의 위치를 입력하세요: "))
        DLL.delete(position)

    elif command == 'delete_all':
        cur_size = DLL.get_size()
        for idx in range(cur_size):
            DLL.delete(0)

    elif command == 'print':
        DLL.print_linked_list()

    elif command == 'print_rev':
        DLL.print_reverse_linked_list()

    elif command == 'exit':
        break

    else:
        print("No such command!!!")
        print("Use 'help' to check command")