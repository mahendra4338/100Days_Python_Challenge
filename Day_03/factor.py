num=24
i=1
print("Factors=",end='')

while i<=num:
    if num%i==0:
        
        if i<num:
            print(i,end=',')
        else:
            print(i) 
    i+=1           


