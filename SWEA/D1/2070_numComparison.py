T = int(input())
for test_case in range(1, T+1):
    a, b = map(int, input().split())

    if a > b:
        result = '>'
    elif a == b:
        result = '='
    else:
        result = '<'

    print("#"+str(test_case), end=" ")
    print(result)