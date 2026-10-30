n = int(input())
temp = n 
rev = 0
while n > 0:
  last = n % 10
  rev = rev * 10 + last
  n = n // 10
if rev == temp:
  print("Palindrome")
else:
  print(" Not Palindrome")
