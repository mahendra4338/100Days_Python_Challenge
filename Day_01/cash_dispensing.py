amount=int(input("Enter Amount: ")) #3700
temp=amount
while temp>100:
    if temp>=2000:
        q=temp//2000
        temp=temp%2000
        print(f"2000 x {q}")
    elif temp>=500:
        q=temp//500
        temp=temp%500
        print(f"500 x {q}")
    elif temp>=200:
        q=temp//200
        temp=temp%200
        print(f"200 x {q}")
    elif temp>=100:
        q=temp//100
        temp=temp%100
        print(f"100 x {q}")            

