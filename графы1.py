n = int(input())
print(n,' - Кол-во вершин')
m = []
for i in range(n):
  m.append(input().split())
print('-----------')

for i in range(n):
  sum = 0
  k = ''
  for j in range(n):
    if(m[i][j] == '1'):
      sum = sum + 1
      k = k + str(j+1) + " "
  print("sum =", sum,",", i+1, ":", k) 

