logins=[1,1,0,1,1,1,0,1,1,1,1]
c=0
e=[]

for i in logins:
    if i==1:
        c+=1
    if i==0:
        e+=[c]
        c=0

e+=[c] 
c=0

for i in e:
    if i>c:
        c=i
        
print("Longest Streak:",c)        