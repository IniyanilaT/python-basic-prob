size = int(input())
arr = list(map(int,input().split()))
evencount=oddcount=0
for x in arr:
  if x % 2 == 0:
    evencount += x
  else:
    oddcount += x
print(evencount,oddcount)
    
