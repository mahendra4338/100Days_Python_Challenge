nums=[12,5,8,21,14,7]
e,o=0,0
l,s=nums[0],nums[0]

for i in nums:
    if i%2==0:
        e+=1
    elif i%2!=0:
        o+=1

for i in nums:
    if i>l:
        l=i

for i in nums:        
    if i<s:
        s=i 
                   
print(f"Even={e} ")
print(f"Odd={o} ")
print(f"Largest={l} ")
print(f"Smallest={s} ")