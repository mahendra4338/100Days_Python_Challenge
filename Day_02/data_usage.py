usage=[450,600,700,550]
s=0
c=0
limit=2000
for i in usage:
    s+=i
    c+=1
    if s>limit:
        break
print(f"Limit Exceeded On Day {c}")
print(f"Used = {s}MB")    
