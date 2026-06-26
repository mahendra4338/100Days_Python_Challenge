num=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(len(num)):
    sum=0
    for j in range(len(num[i])):
        sum=sum+num[i][j]
    print(f"Row {i+1} = {sum}") 
