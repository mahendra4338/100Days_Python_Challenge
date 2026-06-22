marks=list(map(int,input("Enter Marks:").split()))
pass_mark=35
p=0
f=0
for i in marks:
    if i>=pass_marks:
        p+=1
    else:
        f+=1
print(f'Passed={p}') 
print(f'failed={f}')             
