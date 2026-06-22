sales=[5000,7000,-1,9000,0,8000]
sum=0
for i in sales:
    if i==-1:
        continue
    elif i>0:
        sum=sum+i
    elif i==0:
        break
print(f"Total sales= {sum}")        