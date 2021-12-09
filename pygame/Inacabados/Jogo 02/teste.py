listinha1 = [(0,1)]
listinha2 = [(0,0),(0,1),(1,0), (1,1)]


for num in range(len(listinha1)):
    for num2 in range(len(listinha2)):
        if listinha1[num] == listinha2[num2]:
            print("igual")
        else:
            print("diferente")

        
