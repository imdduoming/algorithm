import sys
import collections
input = sys.stdin.readline #빠른 입력
N=int(input())
class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def preorder(TreeNode):


    print(TreeNode.data,end='')
    if TreeNode.left is not None :
        preorder(tree[TreeNode.left])
    if TreeNode.right is not None:
        preorder(tree[TreeNode.right])

def inorder(TreeNode):

    if TreeNode.left is not None:
        inorder(tree[TreeNode.left])
    print(TreeNode.data, end='')
    if TreeNode.right is not None:
        inorder(tree[TreeNode.right])


def postorder(TreeNode):
    if TreeNode.left is not None :
        postorder(tree[TreeNode.left])
    if TreeNode.right is not None:
        postorder(tree[TreeNode.right])

    print(TreeNode.data, end='')

tree={}
for i in range(N):
    root,left,right=input().split()
    if left=='.':
        left=None
    if right=='.':
        right=None
    tree[root]=TreeNode(root,left,right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])



