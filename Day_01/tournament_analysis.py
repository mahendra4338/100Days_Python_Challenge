runs=list(map(int,input("Enter Runs:").split()))
count=0
sum=0
highest=runs[0]
for i in runs:
    if i>highest:
        highest=i
    count+=1
    sum=sum+i
print(f"Total:{sum}")
print(f"Highest:{highest}")
print(f"Average:{(sum/count):.1f}")
