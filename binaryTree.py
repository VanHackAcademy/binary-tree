class BinaryTree:
  def __init__(self, val=None):
    self.val = val
    self.leftChild = None
    self.rightChild = None
    
    
  def getBinaryTreeHeight(self, node):
    if node == None:
      return 0

    leftHeight = self.getBinaryTreeHeight(node.leftChild)
    rightHeight = self.getBinaryTreeHeight(node.rightChild)

    return max(leftHeight, rightHeight) + 1


  def insertValue(self, value):
    if self.val == None:
      self.val = BinaryTree(value)
      return

    treeHeight = self.getBinaryTreeHeight(self)
    nodeList = [self]

    i = 0
    while i < treeHeight:
      tempNodeList = []
      for node in nodeList:
        if node.leftChild == None:
          node.leftChild = BinaryTree(value)
          return
        else:
          tempNodeList.append(node.leftChild)
        if node.rightChild == None:
          node.rightChild = BinaryTree(value)
          return
        else:
          tempNodeList.append(node.rightChild)
      nodeList.clear()
      nodeList = tempNodeList[:]
      tempNodeList.clear()
      i += 1



bTree = BinaryTree()
bTree.insertValue(1)
bTree.insertValue(2)
bTree.insertValue(3)
bTree.insertValue(4)
bTree.insertValue(5)
bTree.insertValue(6)
bTree.insertValue(7)
bTree.insertValue(8)
bTree.insertValue(9)
bTree.insertValue(10)
bTree.insertValue(11)
bTree.insertValue(12)
bTree.insertValue(13)
bTree.insertValue(14)
bTree.insertValue(15)
bTree.insertValue(15)
print("binary tree height value is ", bTree.getBinaryTreeHeight(bTree))