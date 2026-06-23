orders=[500,800,-500,1000,-800]
p,n=0,0

for i in orders:
    if i >=0:
        p+=i
    else:
        n+=i

print(f"Sales={p}")
print(f"Returns={-n}")
print(f"Net Revenue={p-n}")            
