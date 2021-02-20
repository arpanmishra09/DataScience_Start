marks=[]
fm= {}
n= int(input())
for a in range(0,n):
    marks.append([input(),float(input())])

marks.sort(key=lambda x:x[1])
marks.pop(0)
print(marks)
i=0
j=1
for i in range(n):
    if marks[i][1] == marks[j][1]:
        fm= [marks[i][1],marks[j][1]]
        fm.sort()
        break
    else:
        print(marks[i][0])
        break


