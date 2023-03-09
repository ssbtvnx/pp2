with open('smth.txt','r') as firstfile:
    with open('Z.txt','a') as secondfile:
        for line in firstfile:
            secondfile.write(line)