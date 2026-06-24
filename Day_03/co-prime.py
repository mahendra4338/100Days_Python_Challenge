a,b=8,15
i=1
hcf=1

while i<=a and i<=b:
    if a%i==0 and b%i==0:
        hcf=i
    i+=1  
      
if hcf==1:
    print(f"Co-Prime Numbers")
else:
    print(f"Not Co-Prime Numbers")    