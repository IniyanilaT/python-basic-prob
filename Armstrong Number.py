n = int(input())
count = 0
temp = n 
while n > 0:
  n = n // 10
  count += 1
n = temp
summ =  0 
while n > 0:
  last = (n % 10) ** count
  summ = summ + last 
  n = n // 10
if summ == temp:
  print("Armstrong")
else:
  print("Not Armstrong")
