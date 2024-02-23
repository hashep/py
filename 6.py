a = set([1,2,3])
b = list(a)

print(a) #set(집합)은 순서가 없기에 a[1], a[2], ... 불가
print(b)
print(b[1])

c = set([1,2,3,4])
d = set([4,5,6,7])

print(c|d)

print(bool([1,2,3])) # 자료형에 뭔가 들어있다면 참, 아니면 거짓(기본설정)