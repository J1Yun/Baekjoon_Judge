#include<iostream>
using namespace std;
int main()
{
	int score[5], sum = 0;
	for (int i = 0; i < 5; i++) {
		cin >> score[i];
		if (score[i] < 40)
			score[i] = 40;
	}
	for (int i = 0; i < 5; i++)
		sum = sum + score[i];
	cout << sum / 5 << endl;
}
