a,b=12,18
num= a if a>b else b
i=1

while i<=num:
    if a%i==0 and b%i==0:
        print(i,end=' ')
    i+=1

a,b=12,18
i=1
s=""
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        s+=str(i)+','
    i+=1
print(s[:-1])