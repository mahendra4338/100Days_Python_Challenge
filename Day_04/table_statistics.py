first=2
end=10
t,f,b=0,0,0

for i in range(first,end+1):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
        if i*j<20:
            t+=1
        elif i*j>50:
            f+=1
        else:
            b+=1 

print(f"Less Than 20= {t}") 
print(f"Between 20 and 50= {b}")
print(f"Greather 50= {f}")      
                    