#Code By MrRobot

b = 0
for i in range(1,101):
    a = i*i
    b = a + b

c = 0
for j in range(1,101):
    c = c+j
    d = c*c 

print(d-b)
