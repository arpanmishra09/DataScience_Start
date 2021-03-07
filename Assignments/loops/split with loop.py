string1 = 'peter piper picked a peck of pickled peppers'
split_list = []
tmp = ''
for s in string1:
   if s == ' ':
       split_list.append(tmp)
       tmp = ''
   else:
       tmp += s
if tmp:
   split_list.append(tmp)

print(split_list)