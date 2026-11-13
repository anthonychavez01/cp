i = int(input())
 
n = 1
while(n <= i):
   a, b = map(int,input().split())
   if(a == 0 and b == 0):
      print(0)
   elif(a > b ):
      if(a%2 == 0 and b%2 != 0):
         print(a + 1)
      elif(a%2 != 0 and b%2 == 0):
         print(a+1)
      else:
         print(a)
   elif(b - a >1):
      print(-1)
   elif(b > a):
      print(b)
   elif(a == b):
      print(b)
   n = n +1