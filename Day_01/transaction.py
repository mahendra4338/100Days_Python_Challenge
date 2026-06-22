transactions=list(map(int,input("Enter Amount:").split()))
balance=6000
for i in transactions:
    balance += i
    if balance < 0:
        print("Insufficient Balance")
        break
print(f"Final Balance:{balance}")            
    