seats=[1,0,1,1,0,0,1]
c,o,uo=0,0,0

for i in seats:
    c+=1

for i in seats:
    if i==1:
        o+=1
    elif i==0:
        uo+=1
        
print(f"Occupied={o}")
print(f"Empty={uo}")
print(f"Occupancy={((o/c)*100):.2f}")