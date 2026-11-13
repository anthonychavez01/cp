i = 0
 
while(i<5):
   l = list(map(int,input().split()))
   j = 0
   while(j<5):
      if(l[j]==1):
         swaps = abs(i-2)+abs(j-2)
      j = j + 1
   i = i+1 
 
print(swaps)