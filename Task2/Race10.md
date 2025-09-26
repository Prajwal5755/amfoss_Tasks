```
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
      int a,x,y;
        int flag=0;
        scanf("%d%d%d",&a,&x,&y);
        for(int b=1;b<100;b++){
            if(abs(b-x)<abs(a-x) && abs(b-y)<abs(a-y)){
                flag=1;
            }
        }
        if(flag==1){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }
    return 0;
}
```

```
Here they have mentioned distance of bob from x and y should be less than that of alice so i used abs() function its like modulas function and compared distaces
```

