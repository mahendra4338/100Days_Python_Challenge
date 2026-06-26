numbers=[2,3,4,6,8] 
target=24

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        m=numbers[i]*numbers[j]
        if m==24:
            print(f"{numbers[i]} x {numbers[j]}")
