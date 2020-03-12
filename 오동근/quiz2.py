print('첫번째 수를 입력하세요')
first = input()
print('두번째 수를 입력하세요')
second = input()
print('연산기호를 입력하세요')
i = input()

answer = 0

if( i == '+') : answer = int(first) + int(second)
if (i == '-') : answer = int(first) - int(second)
if (i == '*') : answer = int(first) * int(second)
if (i == '/') : answer = int(first) / int(second)


print('answer : ' + str(answer))