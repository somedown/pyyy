class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def abc(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.abc(data)
      elif data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.abc(data)
    else:
      self.data = data

  def Tree(self):
    if self.left:
      self.left.Tree()
    print(self.data)  
    if self.right:
      self.right.Tree()

def s(self, find):
    if find < self.data:
      if self.left is None:
        return str(find)+" - не найдено"
      return self.left.s(find)
    elif find > self.data:
      if self.right is None:
        return str(find)+" - не найдено"
      return self.right.s(find)
    else:
      return str(self.data) + ' - найдено'

u = Node(int(input("корень = ")))
a = input("ветви: ").split()
for i in range(len(a)):
  u.abc(int(a[i]))
print("двоичное дерево: ")
u.Tree()

n = int(input("искомое число  = "))
print(u.s(n))

while(n != ""):
  n = input("искомое число  = ")
  if(n != ""):
    print(u.s(int(n)))
