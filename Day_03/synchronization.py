machine1,machine2=12,18
lcm=machine1 if machine1>machine2 else machine2
while True:
    if lcm%machine1==0 and lcm%machine2==0:
        print(lcm,"Minutes")
        break
    lcm+=1 
       
