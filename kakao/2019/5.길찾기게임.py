# input
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
nodeinfo = [[5, 3]]
# answer: 

# algo
# 재귀 한도를 풀어줘야 한다..
import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, head):
        self.head = head
        self.pre = []
        self.post = []

    def insert(self, data, node=None):
        if node == None:
            node = self.head
        if node.data[0] < data[0]:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(data, node.right)
        else:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(data, node.left)

    def preorder(self, node):
        if node is None:
            return 
        self.pre.append(node.data[-1])
        self.preorder(node.left)
        self.preorder(node.right)
        

    def postorder(self, node):
        if node is None:
            return 
        self.postorder(node.left)
        self.postorder(node.right)
        self.post.append(node.data[-1])
        

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i] = nodeinfo[i]+[i+1]

    nodes = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    tree = Tree(Node(nodes[0]))

    for node in nodes[1:]:
        tree.insert(node)

    tree.preorder(tree.head)
    tree.postorder(tree.head)

    return [tree.pre, tree.post]

print(solution(nodeinfo))