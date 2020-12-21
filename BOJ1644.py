# 1644번 문제
import sys
import math

def primes_upto(limit):
    is_prime = [False] * 2 + [True] * (limit - 1)
    print(is_prime)
    for n in range(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


N = int(input())
if N==1:
    print(0)
    sys.exit()
sieve = [False for i in range(N+1)]
primeNumberArr = primes_upto(N)
start = 0
end = 0
result = 0
count = 0
length = len(primeNumberArr)
primeNumberArr.append(0)
while start<=end:
    if result >= N or end == length:
        result -= primeNumberArr[start]
        start += 1
    else:
        result += primeNumberArr[end]
        end += 1
    if result == N:
        count += 1
print(count)