import array as arr
vals= arr.array ('i', [5,9,8,4,2])
new_value= arr.array(vals.typecode, (a**2 for a in vals))
for i in range(len(new_value)):
    print(new_value[i])