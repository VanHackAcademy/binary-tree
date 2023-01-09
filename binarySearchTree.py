class BinarySearchTree:
  
  dia = 0 
  
  def __init__(self, val=None):
    self.val = val # value for the root node
    self.rightChild = None # value for the child node
    self.leftChild = None # value for the child node


  # inserting values to the binary tree ============================
  def insert(self, val):
    if self.val == None: # the tree is empty
      self.val = val
      return
    # checking for and ignoring duplicate values
    if self.val == val:
      return

    # the values to the left hand side must be less than the root/parent
    # the values to the right hand side must be greater than the root/parent

    if self.val > val:
      if self.leftChild != None:
        self.leftChild.insert(val) # recursive function/action/point
      else:
        self.leftChild = BinarySearchTree(val)
    else: # focus on the right node coz the value to insert is greater than the current node
      if self.rightChild:
        self.rightChild.insert(val)
      else:
        self.rightChild = BinarySearchTree(val)


  # deleting a node from the binary tree =========================
  def deleteNode(self, root, val):
    if root == None:
      return
    
    if root.val > val:
      root.leftChild = self.deleteNode(root.leftChild, val)
    elif root.val < val:
      root.rightChild = self.deleteNode(root.rightChild, val)
    else:
      if root.rightChild == None:
        return root.leftChild
      if root.leftChild == None:
        return root.rightChild

      tempVal = root.rightChild
      minVal = root.val
      while tempVal.leftChild:
        tempVal = tempVal.leftChild
        minVal = tempVal.val
      root.rightChild = self.deleteNode(root.rightChild, root.val)


  # getting the minimum value of the binary tree ============================
  def getMinimum(self):
    current_node = self
    while self.leftChild != None:
      current_node = current_node.leftChild
    return current_node.val


  # getting the maximum value of the binary tree ============================
  def getMaximum(self):
    current_node = self
    while self.rightChild != None:
      current_node = current_node.rightChild
    return current_node.val


  # checking if a value/node exist in the binary tree ============================
  def nodeExist(self, val):
    if self.val == val:
      return True
    
    if self.val > val: # focus is on the left nodes of the tree
      if self.leftChild == None:
        return False
      return self.leftChild.nodeExist(val) # recursive end

    if self.rightChild == None:
      return False
    return self.rightChild.nodeExist(val)


  # LeftChild -> Parent -> RightChild ===============================
  def inOrder(self, arr):
    if self.leftChild != None:
        self.leftChild.inOrder(arr)
    if self.val != None:
        arr.append(self.val)
    if self.rightChild != None:
        self.rightChild.inOrder(arr)
    return arr


  # Parent -> LeftChild -> RightChild ==============================
  def preOrder(self, arr):
    if self.val != None:
        arr.append(self.val)
    if self.leftChild != None:
        self.leftChild.preOrder(arr)
    if self.rightChild != None:
        self.rightChild.preOrder(arr)
    return arr


  # LeftChild -> RightChild -> Parent ===========================
  def postOrder(self, arr):
    if self.leftChild != None:
        self.leftChild.postOrder(arr)
    if self.rightChild != None:
        self.rightChild.postOrder(arr)
    if self.val != None:
        arr.append(self.val)
    return arr


  # binary tree height
  def binaryTreeHeight(self, root):
    if root == None:
      return 0

    leftHeight = self.binaryTreeHeight(root.leftChild)
    rightHeight = self.binaryTreeHeight(root.rightChild)

    return max(leftHeight, rightHeight) + 1


  def treeDiameter(self, root):
    if root == None:
      BinarySearchTree.dia = 0
      return BinarySearchTree.dia

    leftSubTreeDia = self.binaryTreeHeight(root.leftChild)
    rightSubTreeDia = self.binaryTreeHeight(root.rightChild)
    if (leftSubTreeDia + rightSubTreeDia) > BinarySearchTree.dia:
      BinarySearchTree.dia = max(leftSubTreeDia, rightSubTreeDia) + 1
    
    return BinarySearchTree.dia



nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
root = BinarySearchTree()
for num in nums:
  root.insert(num)


print("preOrder is ",root.preOrder([]))
print("postOrder is ", root.postOrder([]))
print("inOrder is ", root.inOrder([]))
print("binaryTreeHeight is ", root.binaryTreeHeight(root))
root.deleteNode(root, 18)
print("inOrder is again", root.inOrder([]))
print("tree diameter value is", root.treeDiameter(root))