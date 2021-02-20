X = 1
Y = 2
Z = 3
N = 7

X += 1
Y += 1
Z += 1

tmp_list = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(tmp_list)
