#Code By MrRobot

s,c = 0,0
a,b = 1,2
l = [1,2]

while c<4000000:
    c = a+b
    l.append(c)
    a,b = b,c 

for i in l:
    if i%2==0:
        s = i+s

print(s)

