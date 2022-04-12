for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0,110,10):
    print(j, end=' ')
print()

for l in range(20,0,-1):
    print(l, end=' ')
print()

number = int(input('Please enter a number:'))
star = ''
for i in range(number):
    star += '*'
print(star)


k = 0
stars = '*'
while k < number:
    print(stars)
    stars += '*'
    k += 1
