ratings=list(map(int,input("Enter Ratings:").split()))
s=0
c=0
for i in ratings:
    if i==0:
        continue
    s+=i
    c+=1
print(f"Average Rating= {(s/c):.1f}")    

