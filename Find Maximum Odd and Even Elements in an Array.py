size = int(input())
arr = list(map(int,input().split()))
even = []
odd = []
for x in arr:
  if x % 2 == 0:
    even.append(x)
  else:
    odd.append(x)
if len(even) != 0:
  print(max(even))
else:
  print("None")
if len(odd) != 0:
  print(max(odd))
else:
  print("None")
    
    
