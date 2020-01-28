value = int(input("Enter a number"))
#value = int(value)
total=0
for n in range(1, value):
    if value%n == 0:
        total += n
if value == total:
    print("This is a perfect number")
else:
    print("This is not a perfect number")

print(1234%3)
print(1234%2)