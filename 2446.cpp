#include <iostream>
using namespace std;
int main()
{
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j < i; j++)
			cout << " ";
		for (int j = i * 2; j < n * 2 + 1; j++)
			cout << "*";
		cout << "\n";
	}
	for (int i = 1; i < n ; i++) {
		for (int j = i; j < n - 1; j++)
			cout << " ";
		for (int j = 1; j <= i * 2 + 1; j++)
			cout << "*";
		cout << "\n";
	}
	return 0;
}
