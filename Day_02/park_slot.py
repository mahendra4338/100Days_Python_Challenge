vehicles=['C','B','C','T','B','C']
b,c,t=0,0,0
for i in vehicles:
    if i=='C':
        c+=1
    elif i=='B':
        b+=1
    elif i=='T':
        t+=1
print(f"Cars= {c}")
print(f'Bikes= {b}') 
print(f"Trucks= {t}")               
