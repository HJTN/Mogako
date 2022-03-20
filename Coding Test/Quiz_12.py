class Node:
    def __init__(self, data, idx):
        self.data = data
        self.idx = idx
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, data, idx):
        self.root = Node(data, idx)

    def insert(self, data, idx):
        if self.root == None:
            self.set_root(data, idx)
        else:
            self.insert_node(self.root, data, idx)

    def insert_node(self, current_node, data, idx):
        if data == current_node.data:
            print(f"이미 {data}값이 존재합니다. 중복된 값은 삽입할 수 없습니다.")
            return
        if idx < current_node.idx:
            if current_node.left == None:
                current_node.left = Node(data, idx)
            else:
                self.insert_node(current_node.left, data, idx)

        elif idx > current_node.idx:
            if current_node.right == None:
                current_node.right = Node(data, idx)
            else:
                self.insert_node(current_node.right, data, idx)

def pre_order(node):
    if node == None:
        return
    print(f"{node.data}  ", end="")
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print(f"{node.data}  ", end="")
    in_order(node.right)

def post_order(node):
    if node == None:
        return
    post_order(node.left)
    post_order(node.right)
    print(f"{node.data}  ", end="")

result_preorder = [12,1,7,9,11,5,3,10,8,6,15,20] #[7,3,1,5,4,12,10,8]
result_inorder = [9,7,11,1,5,3,12,8,10,15,20,6] #[1,3,12,4,5,7,8,10]

BST = BinarySearchTree()
for num in result_preorder:
    for idx in range(len(result_inorder)):
        if num == result_inorder[idx]:
            BST.insert(num, idx)
            break

print('전위 순회 결과: ', end='')
pre_order(BST.root)
print('\n중위 순회 결과: ', end='')
in_order(BST.root)
print('\n후위 순회 결과: ', end='')
post_order(BST.root)