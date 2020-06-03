/*#include<iostream>
using namespace std;
int main()
{
	int burger[3], drink[2], min = 4000;
	for (int i = 0; i < 3; i++)
		cin >> burger[i];
	for (int i = 0; i < 2; i++)
		cin >> drink[i];
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 2; j++) {
			if (burger[i] + drink[j] < min)
				min = burger[i] + drink[j];
		}
	}
	cout << min - 50 << endl;
}
*/