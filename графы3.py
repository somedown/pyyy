a = int(input("количество вершин = "))
l = []
p = []
print("cписок смежности: ")
for i in range(a):
  s = input().split(":")
  s[1] = s[1].split(',')
  l.append(s[1])


for i in range(a):
  for j in range(len(l[i])):
    p.append([int(i+1),int(l[i][j])])
print("------------")
p2 = p.copy()
for i in range(len(p)):
  for j in range(len(p)):
    f1 = int(p[i][0])
    s1 = int(p[i][1])
    f2 = int(p[j][0])
    s2 = int(p[j][1])
    if(f1 == s2 and s1 == f2):
      p2.remove(p[i])
      p[i].reverse()
print("cписок ребер:")
for i in range(len(p2)):
  print(p2[i])
