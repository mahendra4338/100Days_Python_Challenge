d=[[10,20,30],[50,60,70],[15,25,35]]
h=[]
for i in range(len(d)):
    sum=0
    for j in range(len(d[i])):
        sum+=d[i][j]
    h+=[sum]
g=h[0]
row=1
for i in range(len(h)):
    if h[i]>g:
        g=h[i]
    row=i    
print(f"Row {row}")
print(f'Total={g}')

d=[[10,20,30],[50,60,70],[15,25,35]]
g=0
row=1
for i in range(len(d)):
    sum=0
    for j in range(len(d[i])):
        sum+=d[i][j]
    if sum>g:
        g=sum
        row+=i  
print(f"Row {row}")
print(f'Total={g}')       
    

