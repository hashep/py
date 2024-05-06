f = open("what.txt", 'w')
for i in range(1,11):
    data = "%d번째 \n" % i
    f.write(data)
f.close()

f = open("what.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

with open("what.txt",'w') as f:
    f.write("faoiqjgqgw")
