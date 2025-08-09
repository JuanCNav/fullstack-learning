print("for loops")
for i in range(1,6):
    print(i)
print("while loops")
count=1
while count<=5:
    print(count)
    count+=2
print("break usage")
for i in range(1,10):
    if i==4:
        break
    print(i)
print("continue")
for i in range(1,15):
    if i%2==0:
        continue
    print(i)
    