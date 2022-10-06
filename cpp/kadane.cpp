#include<bits/stdc++.h>
using namespace std;

int main(){
	//Implementation of Kadane's Algorithm
	int n;
	// cout<<"Enter the total elements in array"<<endl;
	cin>>n;
	int a[n];
	// cout<<"Enter the array elements : "<<endl;
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	int sum=0,max_sum=INT_MIN;
	for(int i=0;i<n;i++){
		sum=max(sum + a[i],a[i]);
		if(sum > max_sum){
			max_sum=sum;
		}
	}
	cout<<max_sum<<endl;
}
// TEST CASE 1 :
// 6
// -1 10 15 20 -12 8
// OUTPUT : 45 
// TEST CASE 2 :
// 5
// 10 1100 -2020 1211 -233
// OUTPUT : 1211