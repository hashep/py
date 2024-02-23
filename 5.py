a = (1,2,3,4,5) #튜플 => 값 변경 불가능

a = {1: 'shit'}
a[2] = 'what'
a[3] = [1,2,3]

print(a)

a[5] = 2

print(a)

del a[5]

print(a)
print(a[3])

b = {6: 'what'}
b[2] = 'that'

print(b) #숫자랑순서랑관계x

c = {1: 'say', 1: '?'} # 앞의 1say는 무시된다

print(c)
print(c[1])

#d = {[1, 2] : 'say'} 리스트는 Key로 설정 불가능

print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))