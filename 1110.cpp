#include<iostream>
using namespace std;
int main() {
	int n, r, count = 0;
	cin >> n ;
	r = n;
	do
	{
		r = (r % 10) * 10 + (r / 10 + r % 10) % 10;
		count++;

	} while(r != n);
	cout << count;
	return 0;
}