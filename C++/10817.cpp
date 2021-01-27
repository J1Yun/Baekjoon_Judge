#include<iostream>
using namespace std;
int main()
{
	int n[3], temp;
	for (int i = 0; i < 3; i++)
		cin >> n[i];
	for (int i = 0; i < 3; i++) {
		for (int j = i + 1; j < 3; j++) {
			if (n[i] > n[j]) {
				temp = n[i];
				n[i] = n[j];
				n[j] = temp;
			}
		}
	}
	cout << n[1] << endl;
}
