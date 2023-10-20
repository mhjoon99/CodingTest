T = int(input())

for test_case in range(1, T + 1):
    date = input()

    year = date[:4]
    month = date[4:6]
    day = date[6:]
    correct = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    print('#' + str(test_case), end=' ')

    if int(month)>=1 and int(month)<=12 and int(day)<=correct[int(month)]:
        print("{}/{}/{}".format(year,month,day))
    else:
        print(-1)