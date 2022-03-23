# �끂�뱶 �겢�옒�뒪.
# �깮�꽦�옄濡� �뜲�씠�꽣��� �룷�씤�꽣瑜� 諛쏅뒗�떎.
# �룷�씤�꽣媛� �엯�젰�씠 �븞�맂 寃쎌슦, �빐�떦 �끂�뱶媛� 醫낅떒�젏�씠�씪�뒗 �쓽誘�.
class Node:
    def __init__(self, data, left_pointer=None, right_pointer=None):
        self.left_pointer = left_pointer
        self.data = data
        self.right_pointer = right_pointer

# 留곹겕�뱶由ъ뒪�듃 �겢�옒�뒪.
# �겢�옒�뒪 媛앹껜 �깮�꽦�떆 �뜲�씠�꽣媛� 議댁옱�븯吏� �븡�뒗 �끂�뱶瑜� �깮�꽦�븳�떎.
# �빐�떦 �끂�뱶�쓽 �룷�씤�꽣媛� 諛붾줈 Head.
class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        # 留곹겕�뱶由ъ뒪�듃�쓽 �끂�뱶 媛쒖닔瑜� ����옣�븯�뒗 蹂��닔 size.
        self.size = 0

    # idx �쐞移섏뿉 議댁옱�븯�뒗 �끂�뱶瑜� 諛쏆븘�삩�떎.
    def get(self, idx):
        # �엯�젰�맂 �씤�뜳�뒪媛� 留곹겕�뱶由ъ뒪�듃 �궗�씠利덈낫�떎 �겢 寃쎌슦, �삤瑜섍�� 諛쒖깮.
        if idx >= self.size:
            print("Index Error")
            return None
        # �씤�뜳�뒪媛� 0�씤 寃쎌슦, �뿤�뱶瑜� 諛쏆븘�삤�씪�뒗 �쓽誘�
        if idx == 0:
            return self.head
        else:
            node = self.head
            for _ in range(idx):
                node = node.right_pointer
            return node

    # �뜲�씠�꽣瑜� 留곹겕�뱶由ъ뒪�듃 醫낅떒�젏�쑝濡� 異붽���븳�떎.
    def append(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.size += 1
        else:
            node = self.head
            # 醫낅떒�젏�쓽 �룷�씤�꽣�뒗 None媛믪쓣 媛�吏�.
            while node.right_pointer != None:
                node = node.right_pointer

            new_node = Node(data)
            node.right_pointer = new_node
            new_node.left_pointer = node
            self.size += 1

    # �뜲�씠�꽣瑜� idx �쐞移섏뿉 異붽���븳�떎.
    def insert(self, value, idx):
        if self.size == 0:
            self.head = Node(value)
            self.size += 1
        # idx媛� 0�씠�씪�뒗嫄�, Head �옄由ъ뿉 �깉濡쒖슫 �뜲�씠�꽣瑜� �꽔�뒗�떎�뒗 �쓽誘�.
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
            # �궫�엯�븯�젮�뒗 idx �씠�쟾�쓽 �끂�뱶�쓽 �룷�씤�꽣瑜� �깉濡쒖슫 �끂�뱶濡� �꽕�젙
            node.right_pointer = new_node
            new_node.left_pointer = node
            # �쁽�옱 �끂�뱶�쓽 �룷�씤�꽣瑜� �궫�엯�븯�젮�뒗 idx �씠�썑�쓽 �끂�뱶濡� �꽕�젙
            new_node.right_pointer = next_node
            next_node.left_pointer = new_node
            self.size += 1

    # idx �쐞移섏쓽 �끂�뱶瑜� �궘�젣�븳�떎.
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

# Doubly Linked List �깮�꽦
DLL = DoublyLinkedList()

while(1):
    command = input("紐낅졊�뼱瑜� �엯�젰�븯�꽭�슂(�룄���留�: help �엯�젰): ")

    if command == 'help':
        print(" \
            append: N媛쒖쓽 �뜲�씠�꽣 �븳 踰덉뿉 異붽��\n \
            insert: �듅�젙 �쐞移섏뿉 �뜲�씠�꽣 異붽��\n \
            delete: �듅�젙 �쐞移섏쓽 �뜲�씠�꽣 �궘�젣\n \
            delete_all: �뜲�씠�꽣 �쟾遺� �궘�젣\n \
            print: DLL�뿉 �엳�뒗 �뜲�씠�꽣 異쒕젰\n \
            print_rev: DLL�뿉 �엳�뒗 �뜲�씠�꽣 �뿭�닚�쑝濡� 異쒕젰\n \
            exit: �봽濡쒓렇�옩 醫낅즺\n \
        ")

    elif command == 'append':
        # Data �닔 �엯�젰
        data_num = int(input("異붽���븷 �뜲�씠�꽣�쓽 �뼇�쓣 �엯�젰�븯�꽭�슂: "))

        # Data �옄�룞 �깮�꽦
        data_list = []
        for idx in range(1, data_num+1):
            data = f'Data{idx}'
            data_list.append(data)

        # DLL�뿉 data �엯�젰
        for idx in range(data_num):
            DLL.append(data_list[idx])

    elif command == 'insert':
        position, value = input("異붽���븷 �뜲�씠�꽣�쓽 �쐞移섏�� 媛믪쓣 �엯�젰�븯�꽭�슂: ").split()
        DLL.insert(value, int(position))

    elif command == 'delete':
        position = int(input("�궘�젣�븷 �뜲�씠�꽣�쓽 �쐞移섎�� �엯�젰�븯�꽭�슂: "))
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