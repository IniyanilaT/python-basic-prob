n  = int(input())
temp = n
summ =0 
while n > 0:
  last = n % 10
  total = 1
  
  for i in range(1,last + 1):
    total = total * i
  summ = summ + total  
  n = n // 10  
if summ == temp:
  print("Strong")
else:
  print("Not Strong")
  
