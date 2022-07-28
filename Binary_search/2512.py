import sys

n = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))
maximum = int(sys.stdin.readline())

#sum이 maximum보다 커서 상한액을 정해야 하는 경우. 
lt = 0
rt = max(money)
while lt <= rt:
    mid = (lt+rt) // 2
    res = 0
    for i in money:
        if i < mid:
            res += i
        else:
            res += mid

    if res > maximum:
        rt = mid - 1
    else:
        lt = mid + 1
    print("lt:" , lt)
    print("mid:" , mid)
    print("rt:" , rt)

        