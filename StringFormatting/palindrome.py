x, y = "I'm Adam'".lower().strip("i' ").strip().replace(" ", ''), 'Madam'.lower()

# method 1
if x == y:
    print('A palindrome')
else:
    print('Not a palindrome')

# method 2
index = len(y) - 1
lcount = 0
for i in x:
    if i == y[index]:
        lcount += 1
        index -= 1
    else:
        break
if lcount > len(x) and len(y) or lcount < len(x) and len(y):
    print('Not a palindrome')
else:
    print('A palindrome')

