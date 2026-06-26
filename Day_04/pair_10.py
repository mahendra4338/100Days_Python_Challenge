numbers=[2,5,7,8,3] 
target=10

for i in numbers:
    for j in numbers:
        if i!=j:
            sum=i+j
            if sum==target:
                print(i,'+',j,'=',sum)

numbers=[2,5,7,8,3] 
target=24

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        m=numbers[i]+numbers[j]
        if m==10:
            print(f"{numbers[i]} + {numbers[j]}")