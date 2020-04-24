print(list('ert'))
print(list([True, False, 34.5, 60]))

print([True,False,34.5,    60])

print(float(False))

print(bool([]))

spreadsheet_list = [ ['Name','Age','GPA'], ['Bill', 25, 3.55], ['Rich', 26 , 4.00]]

print(spreadsheet_list[2][0])



x_dict = ({column : spreadsheet_list for row in spreadsheet_list  for column in row})

print(x_dict)

for (x , y) in (x_dict.items()):
    print(x,y, end= "\n")