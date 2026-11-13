i = int(input())
n = i // 5
 
if(n == 0):
   if(i ==0):
      print(0)
   else:
      print(1)
 
if(n > 0):
   if(i%5 == 0):
      print(n)
   else:
      print(n + 1)
 