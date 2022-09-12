t=(1,2,3,False,[10,20,30],"Ravi",1.1,1.2,1.3,"Tops",True,100,200,300,"Python")
print(t)
print(t.count(100))
print(t.index(100))
print(t.count(300))
print(t.index(3))
print(t.count(2))
print(t[3])
print(t.count(1))
print(t.count(0))

for i in t:
    print(i,end=",")

for i in t:
    print(i)

print(1.2 in t)
print(t[5])










