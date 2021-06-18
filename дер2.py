class c:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def ins(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = c(data)
        else:
          self.left.ins(data)
      elif data > self.data:
        if self.right is None:
          self.right = c(data)
        else:
          self.right.ins(data)
    else:
      self.data = data

  def tree(self):
    if self.left:
      self.left.tree()
    print(self.data)  
    if self.right:
      self.right.tree()

  def sss(self, find):
    if find < self.data:
      if self.left is None:
        return str(find)+" - не найдено"
      return self.left.sss(find)
    elif find > self.data:
      if self.right is None:
        return str(find)+" - не найдено"
      return self.right.sss(find)
    else:
      return str(self.data) + ' - найдено'
     
      

B = c(int(input("корень = ")))
a = input("ветви: ").split()
for i in range(len(a)):
  B.ins(int(a[i]))
print("двоичное дерево")
B.tree()

k = int(input("введите число = "))
print(B.sss(k))

while(k != ""):
  k = input("введите число = ")
  if(k != ""):
    print(B.sss(int(k)))
