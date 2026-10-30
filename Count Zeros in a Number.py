n = int(input())
count = 0
if n == 0:
  count = 1
while n > 0:
  last = n % 10
  n = n // 10
  if last == 0:
    count += 1
print(int(count))    
