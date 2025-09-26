def smallest(n):
    digits = list(map(int, n))
    digits.sort()
    result = []
    for i in range(1, 11):
        limit = 10 - i
        for i, d in enumerate(digits):
            if d >= limit:
                result.append(str(d))
                digits.pop(i)
                break
    return ''.join(result)


t = int(input())
for _ in range(t):
    n = input().strip()
    print(smallest(n))
