i = int(input())
j = 1
while(j <= i):
    a, b, c = map(int,input().split())
    if(a + b == c or a + c == b or b + c == a):
        print("YES")
    else:
        print("NO")
    j = j+1
 
 