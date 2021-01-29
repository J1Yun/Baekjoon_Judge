#include <iostream>
using namespace std;
int main()
{
	int h, m;
	cin >> h >> m;
	if (m < 45)
		if (h == 0) 
			cout << 23 << ' ' << 60 - (45 - m) << endl;
		else
			cout << h - 1 << ' ' << 60 - (45 - m) << endl;
	else
		cout << h << ' ' << m - 45 << endl;
	return 0;
	
}
