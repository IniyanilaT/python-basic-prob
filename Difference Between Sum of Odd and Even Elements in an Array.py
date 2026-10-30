size = int(input())
arr = list(map(int,input().split()))
evensum = oddsum = 0
for x in arr:
  if x % 2 == 0:
    evensum += x
  else:
    oddsum += x 
diff = oddsum - evensum  
print(diff)
