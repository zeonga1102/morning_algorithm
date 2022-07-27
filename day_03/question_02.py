# https://www.acmicpc.net/problem/2941

alphabet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()

for i in alphabet_list:
    string.replace(i, '.')

print(len(string))