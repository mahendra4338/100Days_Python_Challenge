chocolates,biscuits=24,36
lcm=chocolates if chocolates>biscuits else biscuits

while True:
    if lcm%chocolates==0 and lcm%biscuits==0:
        lcm=lcm
        break
    lcm+=1
    
hcf=(chocolates*biscuits)//lcm
print(hcf,"Gift Boxes")