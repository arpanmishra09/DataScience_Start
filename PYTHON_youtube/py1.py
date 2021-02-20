Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> \n
SyntaxError: unexpected character after line continuation character
>>> nums= [3, 45, 2, 5]
>>> nums.append(2)
>>> nums
[3, 45, 2, 5, 2]
>>> nums. insert ( 1, 34)
>>> nums
[3, 34, 45, 2, 5, 2]
>>> nums.remove (5)
>>> nums
[3, 34, 45, 2, 2]
>>> nums.pop(4)
2
>>> num
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    num
NameError: name 'num' is not defined
>>> nums
[3, 34, 45, 2]
>>> nums.pop()
2
>>> nums
[3, 34, 45]
>>> del nums [1]
>>> nums
[3, 45]
>>> nums.extend([29, 12, 14, 36])
>>> nums
[3, 45, 29, 12, 14, 36]
>>> min(nums)
3
>>> msx(nums)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    msx(nums)
NameError: name 'msx' is not defined
>>> max(nums)
45
>>> sum(nums)
139
>>> nums.sort(nums)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    nums.sort(nums)
TypeError: sort() takes no positional arguments
>>> nums.sort()
>>> nums
[3, 12, 14, 29, 36, 45]
>>> tup = (21, 36, 14, 25)
>>> tup[1]
36
>>> tup[1]= 3
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tup[1]= 3
TypeError: 'tuple' object does not support item assignment
>>> tup.count()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tup.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> s = {22, 25, 2}
>>> s
{25, 2, 22}
>>> s.add()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
>>> S.add[0:]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    S.add[0:]
NameError: name 'S' is not defined
>>> s.add[0:]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.add[0:]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> s.add
<built-in method add of set object at 0x000002694BB6DF20>
>>> 
>>> s.add()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
>>> s.add(0:3)
SyntaxError: invalid syntax
>>> s.add(0,3)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.add(0,3)
TypeError: set.add() takes exactly one argument (2 given)
>>> s.add (3)
>>> s
{25, 2, 3, 22}
>>> s.=-[pl