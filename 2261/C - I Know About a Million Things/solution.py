i = int(input())
j = 1
while(j <= i):
    n = int(input())
    l = list(map(int,input().split()))
    m = 0
    odd = 0
    
    even = 0
    while(m < n):
        
        if(l[m]% 2 == 0):
            even = even +1
        elif(l[m]%2 != 0):
            odd = odd + 1
        m = m + 1
    if(n == 1):
        print("Moggity")
    elif(n == 2):
        if(odd == 1):
            print("Larpity")
        else:
            print("Moggity")
    elif(odd % 2 == 0):
        print("Moggity")
    elif(odd % 2 != 0 and even > 0):
        print("Moggity")
    elif(odd % 2 != 0 and even == 0 and odd == 3):
        print("Larpity")
    elif(odd % 2 != 0 and even == 0):
        print("Moggity")
    j = j +1