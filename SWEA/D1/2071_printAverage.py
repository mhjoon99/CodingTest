T = int(input())
for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    avg = sum(num)/len(num)
    print("#" + str(test_case), end=" ")
    print(round(avg))