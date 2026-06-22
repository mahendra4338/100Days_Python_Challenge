prices=list(map(int,(input("Enter Prices:")).split()))
bill=0
discount=0
for item in prices:
    if item>1000:
        discount=int(discount+(item*0.10))
        bill=bill+item    
    else:
        bill=bill+item    
print(f"Total Bill:{bill}")
print(f"Discount:{discount}")
print(f"Final Bill:{bill-discount}")
   


