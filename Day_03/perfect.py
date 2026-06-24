num=28
i=1
sum=0

while i<num:
    if num%i==0:
        sum+=i
    i+=1  
      
if sum==num:
    print(f"Perfect Number")
else:
    print(f"Not a Perfect Number")            