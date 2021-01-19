#include <iostream>
using namespace std;
int main()
{
	int n = 0, t = 0;
	char arr[100];
	cin >> arr;
	while (1)
	{
		for (int i= n; i < n+10; i++) {
			if (!arr[i]) break;
			cout << arr[i];
			t++;
		}
		n = t;
		cout << "\n";
		if (!arr[n]) break;
		else continue;

	}
	return 0;
}
