c = input().split()
b = int(c[0])
m = int(c[1])
#смежности
a = [] 
for i in range (b):
  a.append([])

for i in range(m):
  s = input().split()
  first = int(s[0])-1
  second = int(s[1])-1
  a[first].append(second+1)
  a[second].append(first+1)
  

#исходная точка
v = int(input()) 
op = []
a_smezh = [False for i in range(len(a))]
def aaa(node):
  a_smezh[node-1] = True
  op.append(node)
  t = 0
  for neighbor in a[node-1]:
    if a_smezh[neighbor-1]:
      t = t + 1
    if not a_smezh[neighbor-1]:     
      aaa(neighbor)
    if t == len(a[node-1]):
      op.append(node-1)  

aaa(v)
print("смежность:")
print(a)
print("кол-во ходов:")
print(len(op))
print("точки:")
print(op)


