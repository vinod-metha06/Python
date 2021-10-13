#include <stdio.h>

int main() {

int m,n,p,count=0;
 scanf("%d%d%d",&m,&n,&p); 
 while(p>0||m>0||n>0){




if(p>0&&m>0&&n>0)
{ 
    count++;
    p--;
    m--;
    n--;
   
}else{

count++;
  if(p>0)p--;
   


if(m>0&&n>0) {
    m--;
    n--;}

// if(m>0&&n<1){
//  m --;
//  n--;
// }
if(m>0&&n<1){
    m=-2;
}
 if(n>0&&m<1) n -= 2;

}



}

printf("%d",count-1); return 0;



}