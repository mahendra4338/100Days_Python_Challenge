
a=12
b=18
x,y=a,b
while y!=0:
    x,y=y,x%y
hcf=x
if a==0 or b==0:
    lcm=0
else:
    lcm=(a*b)//hcf
print(hcf,lcm)


a=12
b=18
lcm=a if a>b else b
while True:
    if lcm%a==0 and lcm%b==0:
        print(lcm)
        break
    lcm+=1
hcf=(a*b)//lcm
print(hcf) 
  
a,b=12,18
hcf=1
i=1
while i<=a and i <=b:
    if a%i==0 and b%i==0:
        hcf=i
    i+=1
print(hcf)
print(f"{(a*b)//hcf}")    
