a= input().split()
b=a[0]
c=a[1]
for i in len(b)//2:
    del b[2*i-1]
for i in len(c)//2:
    del b[2*i]
print(b,c)
