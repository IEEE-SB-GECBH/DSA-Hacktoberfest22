// An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371

#include<iostream>
#include<cmath>
using namespace std;
int main()
{
int i,num,sum=0,b,d,power;
cout<<"enter the no of digits of number";
cin>>d;
cout<<"enter num to check armstrong number";
cin>>num;
i=num;
while (num != 0)
{
    b=num%10;
    num=num/10;
    power= round(pow(b,d));
    // round returns the equivalent integer 
    // // pow() returns a double value
    // double is a primitive datatype that can store upto 15 decimal points without rounding them off
    // float is a primitive datatype that can store upto 7 decimal points & rounds off the rest of the digits
    sum += power;
}
 
if (i==sum)
{
    cout<<"armstrong number";
}
else
{
    cout<<"not armstrong number";
}

return 0;
}
