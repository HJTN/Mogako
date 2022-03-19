class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_tree(idx):
    if idx == 0:
        root = Node(7)

        node_3 = Node(3)
        node_10 = Node(10)
        root.left = node_3
        root.right = node_10

        node_1 = Node(1)
        node_5 = Node(5)
        node_3.left = node_1
        node_3.right = node_5

        node_8 = Node(8)
        node_10.left = node_8

        node_4 = Node(4)
        node_5.left = node_4

        node_12 = Node(12)
        node_4.left = node_12

    elif idx == 1:
        root = Node(100)

        node_10 = Node(10)
        node_11 = Node(11)
        root.left = node_10
        root.right = node_11

        node_7 = Node(7)
        node_5 = Node(5)
        node_10.left = node_7
        node_10.right = node_5

        node_9 = Node(9)
        node_1 = Node(1)
        node_11.left = node_9
        node_11.right = node_1

        node_25 = Node(25)
        node_14 = Node(14)
        node_7.left = node_25
        node_5.right = node_14

        node_36 = Node(36)
        node_19 = Node(19)
        node_9.right = node_36
        node_1.left = node_19

        node_23 = Node(23)
        node_36.left = node_23

    elif idx == 2:
        root = Node(8)

        node_10 = Node(10)
        node_11 = Node(11)
        root.left = node_10
        root.right = node_11

        node_5 = Node(5)
        node_9 = Node(9)
        node_10.right = node_5
        node_11.left = node_9

    return root

def get_tree_height(node, cur_height):
    global max_height, d_node

    if node == None:
        return
    
    if max_height < cur_height:
        max_height = cur_height
        d_node = node
    
    get_tree_height(node.left, cur_height+1)
    get_tree_height(node.right, cur_height+1)

def answer(idx):
    global max_height, d_node
    max_height = 0

    root = get_tree(idx)
    get_tree_height(root, 0)
    print(f'가장 깊은 레벨에 존재하는 노드: {d_node.data}')
    print(f'Tree의 높이: {max_height}')

for idx in range(3):
    answer(idx)