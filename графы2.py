a = int(input())
b = int(input())
aa = [] 
for i in range (a):
  aa.append([])
for i in range(b):
  с = input().split()
  first = int(с[0])-1
  second = int(с[1])-1
  aa[first].append(second+1)
  aa[second].append(first+1)
for i in range(a):
  k = str(sorted(aa[i]))
  k= k.replace('[', '')
  k= k.replace(']', '')
  print(i+1, ":", k)  
