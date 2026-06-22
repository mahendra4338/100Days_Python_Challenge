cart=list(map(int,input("Enter Cart Amount:").split()))
sum=0
for item in cart:
    if item==-1:
        continue
    else:
        sum+=item
print(f"Total Amount:{sum}")        