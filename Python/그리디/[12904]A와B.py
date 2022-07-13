s = input()
t = input()

s_len, t_len = len(s), len(t)
for _ in range(t_len-s_len):
    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
if s == t:
    print(1)
else:
    print(0)