results=['P','P','F','F','F','P']
c=0
for i in results:
    if i=='F':
        c+=1
        if c==3:
            print(f"{c} Consecutive Failures Found")
            break 
    else:
        c=0 
if c<3:
    print(f"{c} Consecutive Failures Found")            
          