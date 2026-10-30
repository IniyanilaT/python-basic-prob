size = int(input())
arr = list(map(int,input().split()))
evensum=oddsum=0
for i  in range(len(arr)):
  if i % 2 ==0:
    evensum += arr[i]
  else:
    oddsum += arr[i]
print(evensum,oddsum)    
