str = list(input())

for i in range(len(str)):
    if ord(str[i])>=97 and ord(str[i])<=122:
        str[i] = str[i].upper()

print(''.join(str))