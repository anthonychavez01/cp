i = int(input())
j = 1
while(j <= i):
    n, m = map(int,input().split())
    p = 2 **(n-m+1) + 2 * (m-1)
    print(p)
    j = j +1
 