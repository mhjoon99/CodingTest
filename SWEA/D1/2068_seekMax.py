T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    max = 0

    for i in num:
        if i >= max:
            max = i

    print("#"+str(test_case), end=" ")
    print(max)