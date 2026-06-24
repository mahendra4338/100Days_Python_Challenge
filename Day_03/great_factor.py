num=36
i=1
h=0

while i<num:
    if num%i==0:
        if i>h:
            h=i   
    i+=1
    
print(f'Greatest Factor:{h}')            