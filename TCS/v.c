

#include<bits/stdc++.h>
using namespace std;

void prime(int n){
   int i;
  bool is_prime = true;

  if (n == 0 || n == 1) {
    is_prime = false;
  }

  for (i = 2; i <= n/2; ++i) {
    if (n % i == 0) {
      is_prime = false;
      break;
    }
  }

  if (is_prime)
    cout <<"TIsPrime";
  else
    cout <<"FNotPrime";
}


bool p_check(int n)
{
	int x = (int)(sqrt(n));
	string a=to_string(x);
	string b=to_string(x+1);
	
	if (x*(x+1)==n){
	cout<<"T"<<a+b;
	
		return true;
	}
	else{
	    prime(n);
	}
		
}


int main(void)
{
	int n = 380;
	p_check(n) ;
	
	return 0;
}
