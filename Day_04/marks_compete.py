marks=[85,70,92,78,88]

for i in marks:
    c=0
    
    for j in marks:
        if j>i:
            c+=1
    print(f'{i}->{c}')        