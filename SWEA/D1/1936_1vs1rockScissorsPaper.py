#가위=1, 바위=2, 보=3
a,b = map(int, input().split())
if a == 1:
    if b == 2:
        print('B')
    else:
        print('A')
elif a == 2:
    if b == 1:
        print('A')
    else:
        print('B')
else:
    if b ==1:
        print('B')
    else:
        print('A')
