n = 0

while True:
    n +=20
    m = 0
    for i in range(1,21):
        if n%i==0:
            m +=1
        else:
            break
    
    if m == 20:
        break


print(n)