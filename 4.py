a = [1,2,3,4,['a','b','c']]

print(a)
print(a[4])
print(a[-1][1])
print(a[0:1]) #1
print(a[0:0]) #
print(a[0:2]) #1, 2
print(a[:2])  #1, 2
print(a[1:2]) #2
print(a[2:3]) #3
print(len(a)) #5
print(str(len(a)) + " oh") #5 oh

a.append(6)
a.append([3,4,2])
a.reverse()
print(a)

b = [6,3,4,1]
b.sort() #1,3,4,6
print(b)

print(str(a.pop()) + ' is out from A !')
print(a)