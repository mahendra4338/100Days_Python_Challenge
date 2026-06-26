sales=[500,900,700,1200]
count=0
for i in sales:
    count+=1

for i in range(count):
    r=1
    for j in range(count):
        if sales[j]>sales[i]:
            r+=1
    print(f"{sales[i]}->Rank{r}")

sales=[500,900,700,1200]

for i in sales:
    rank=1

    for j in sales:
        if j>i:
            rank+=1
            
    print(f"{i}->=Rank{rank}")    

