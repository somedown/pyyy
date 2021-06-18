import random
import string

def a(b):
  a = string.ascii_letters + string.digits
  return random.sample(a, b)   

print(a(10))
