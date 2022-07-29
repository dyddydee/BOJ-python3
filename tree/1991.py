class Node:
    def __init__(node, data, left_node, right_node):
        node.data = data
        node.left_node = left_node
        node.right_node = right_node
    
#전위 순회 함수 생성
def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])
    
#중위 순회 함수 생성
def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])
    
#후위 순회 함수 생성
def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')

n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split(' ')
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])