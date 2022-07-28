#가장 큰 30의 배수를 만들어라 .. 수를 다 더해서 3의 배수이고 끝자리가 0.
n = list(map(int, input()))
n.sort(reverse=True)

if sum(n)%3==0 and n[-1] == 0:
    print(''.join(map(str, n)))
else:
    print(-1)