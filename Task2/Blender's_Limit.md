import math

test = int(input())
for _ in range(test):
    n=int(input())
    x, y = map(int, input().split())
    if n==0:
        print(0)
        continue
        
    b=math.ceil(n/x)
    l=math.ceil(n/y)
    print(max(b,l))
    
```
Like here blending and loading occurs parallely it time depends upon max of both
```
    
    
