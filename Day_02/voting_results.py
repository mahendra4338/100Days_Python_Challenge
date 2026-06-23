votes=['A','B','A','C','A','B','A','B','B']
a,b,c=0,0,0

for i in votes:
    if i=='A':
        a+=1
    elif i=='B':
        b+=1
    elif i=='C':
        c+=1

print(f'A={a}')
print(f'B={b}')
print(f'C={c}')

if a==b and a>c:
    print("Winners = A,B")
elif a==c and a>b:
    print("Winners = A,C")
elif b==c and b>a:
    print("Winners = B,C")
elif a>b and a>c:
    print("Winner = A")
elif b>a and b>c:
    print("Winner = B")
else:
    print("Winner = C")
 

  
