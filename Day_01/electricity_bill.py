units=list(map(int,input("Enter Units:").split()))
count=0
for i in units:
    count+=1
i=0
sum=0
while i<count:
    s=0
    r=units[i]-100
    if r>0:
        s=s+(100*5)+(r*8)
        sum=sum+((100*5)+(r*8))
        print(f"{units[i]} units cost is {s}")
    i+=1    
print(f"Total Bill:{sum}")        

