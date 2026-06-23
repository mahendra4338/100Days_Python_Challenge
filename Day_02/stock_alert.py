stock=[25,5,0,18,3,40]
c=0

for i in stock:
    if i>0:
        if i<10:
            c+=1
    continue

print("Products to Restock=",c)        