lines=[]
new =[]
Ntimes=0
N = int(input('ENter no'))
if N>10 or N<1:
        print('N greater than 10')
count = 0
while count < N:
    user = input('ENter tweet')
    lines.append(user)
    count+=1

for line in lines:
    #for letter in line:
    hack = line.strip().lower()
    new.append(hack)
    if hack=="hackerrank":
        Ntimes+=1

if Ntimes == N:
    print(N)
    print(new)
else:
    print(new)






