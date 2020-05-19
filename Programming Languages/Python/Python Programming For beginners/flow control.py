spam = 0
while spam < 5:
    print('hello world')
    spam = spam + 1
#continue
total = 0
for num in range(101):
    total = total + num
print(total)
egg = 0
while egg < 5:
    egg = egg + 1
    if egg == 3:
        continue
    print('egg is ' + str(egg))
name = 0
for i in range(12, 16):
    print('dude' + str(i))
#continue
name = ''
while name != 'your name':
    print('please enter a name.')
    name = input()
print('thanks')
#break
