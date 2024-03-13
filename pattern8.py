n=5
for x in range(1,n+1):
    p=n-x
    for y in range(1,n+1):
        print(chr(p + 65) + " ", end =" ")
        p = p+n
    print()