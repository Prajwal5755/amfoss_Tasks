```
test=int(input())

for _ in range(test):
    n=int(input())
    array=list(map(int,input().split()))
    array.sort()
    mini=min(array)
    maxi=max(array)
    if (mini%2==maxi%2):
        print(0)
    else:
        even = sum(1 for x in array if x%2==0)
        odd =  n - even
        print(min(even,odd))
```
        
```
Here to make it as perfect array in if case i am checking weather both are even or both are odd if true it prints 0, Otherwise  eg 2,4,5,7 is present in else case  even will get 2,4 and odd will get 5,7 then min of even, odd is 2 so output is 2 like either  remove 2 odd or 2 even like that
```
    

