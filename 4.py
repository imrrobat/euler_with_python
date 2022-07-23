max = 0

for i in range(100,1000):
    for j in range(100,1000):
        z = i*j
        y = str(z)
        x = y[::-1]
        if y==x:
            if z>max:
                max = z
            

print(max)