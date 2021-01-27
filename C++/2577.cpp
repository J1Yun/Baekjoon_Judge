#include <iostream>
#include <string>
using namespace std;
int main()
{
	char n[10] = { '0','1','2','3','4','5','6','7','8','9' };
	int a, b, c, x, count,i=0;
	cin >> a >> b >> c;
	x = a * b * c;
	string y = to_string(x);
	while (i<10) {
		count = 0;
		for (int j = 0; y[j]; j++) {
			if (n[i] == y[j])
				count++;
		}
		cout << count << endl;
		i++;
	}
	
}