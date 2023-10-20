n = int(input())
result=1

for i in range(0,n+1):
    result = 1<<i
    print(result, end=' ')