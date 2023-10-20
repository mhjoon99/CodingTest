num = int(input())
sum=0

if num>=1 and num<=9 :
    sum += num
elif num>=10 and num<=99:
    sum += (num/10)    # 십의 자리
    sum += (num%10)     # 일의 자리
elif num>=100 and num<=999:
    sum += (num//100)   # 백의 자리
    sum += (num//10%10) # 십의 자리
    sum += (num%100)    # 일의 자리
else :
    sum += num//1000    # 천의 자리
    sum += num//100%10  # 백의 자리
    sum += num//10%10   # 십의 자리
    sum +=num%10        # 일의 자리

print(sum)