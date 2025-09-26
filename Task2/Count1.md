```
test=int(input())
for _ in range(test):
    n=int(input())
    s=input()
    one=s.count('1')
    zero=s.count('0')
    total=one*(one-1)+zero*(one+1)
    print(total)
```
    
```
Here Leo doing Like this assume i have string 110 so Leo change 010 100 111 Like this so output will be 5 ones, so this formula one*(one-1) [possible combinations for 1 if 2 ones 2 combinations 01 or 10 like this for 0 zero*(one+1) because zero is becoming 1 + 1 which allready their 11 were already their +1 which flipped by 0 1*(3)=3 so output is 5 
```
    

