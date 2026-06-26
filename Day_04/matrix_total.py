m=[[10,20,30],[40,50,60],[70,80,90]]
total_sum=0

for i in range(len(m)):
    sum=0
    for j in range(len(m[i])):
        sum=sum+m[i][j]
     
    total_sum+=sum
print(f"Total:{total_sum}")           
    