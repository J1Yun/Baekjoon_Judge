string = []
n = int(input())
for _ in range(n):
    string.append(input())

def palindrome(s, e, temp):
    while s <= e:
        if str[s] == str[e]:
            s += 1
            e -= 1
        else:
            if temp == 0:
                left = palindrome(s+1, e, temp+1)
                right = palindrome(s, e-1, temp+1)
                return min(left, right)
            else:
                return 2
    return temp

result = []
for str in string:
    s, e = 0, len(str)-1
    result.append(palindrome(s, e, 0))
        
for r in result:
    print(r)