a,b=12,18
x,y=a,b

while y!=0:
    x,y=y,x%y
    hcf=x
    
print(f"HCF={hcf}")

a,b=12,18
i=1
hcf=1

while i<=a and i<=b:
    if a%i==0 and b%i==0:
        hcf=i
    i+=1
print(f"HCF={hcf}")             