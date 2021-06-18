import random
import string
def symb(n):
  k = string.ascii_letters + string.digits
  return random.sample(k, n)   

t = "Хеширование – расширенный вариант поиска с использованием индексирования по ключу, применяемый в наиболее типовых приложениях"
b = t.split()
d = {}
c = symb(len(b))

for i in range(len(b)):
  d[b[i]] = c[i]
print(d)
