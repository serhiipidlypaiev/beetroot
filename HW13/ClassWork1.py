string = '()0)aa()'
string_new = ''
i = 0

for i in range(len(string)):
    b = i+1
    if string[i] == '(' and string[b] == ')':
        string_new +='()'

if string_new[0] == '(' and string_new[-1] == ')':
    print('true')
else:
    print('False')