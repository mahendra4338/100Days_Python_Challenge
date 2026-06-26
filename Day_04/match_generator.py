teams=['A','B','C','D']
for i in range(len(teams)):
    for j in range(i+1,len(teams)):
        print(f"{teams[i]} vs {teams[j]}")
