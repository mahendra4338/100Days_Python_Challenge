password="Abc123x"
s,c,d=0,0,0

for i in password:
    if 'A'<=i<="Z":
        c+=1
    elif 'a'<=i<='z':
        s+=1
    elif '0'<=i<='9':
        d+=1
        
if s>0 and c>0 and d>0:
    print("Strong Password")
else:
    print("Weak Password")            
