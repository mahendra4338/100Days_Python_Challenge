attendance=list(map(str,input("Enter Attendance:").split()))
count=0
for item in attendance:
    count=count+1
present=0
for j in attendance:
    if j=='P':
        present+=1
print(f"Present Days={present}")        
print(f"Attendance Percentage={(present/count)*100:.2f}")        
