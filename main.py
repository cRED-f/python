mat = [[1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
a = []
b = []
c = []
k = 2
flag = 0
for i in range(0, len(mat)):
    sum = 0
    for j in range(0, len(mat)):
        if mat[i][j] == 1:
            sum = sum+1
    a.append(sum)
n = len(a)
print(a)
for i in range(n):
    for j in range(0, n):
        if a[i] > a[j]:
            a[j] = a[n-1]
            n -= 1
            b.append(j)
        elif a[i] < a[j]:
            a[i] = a[n-1]
            n -= 1
            b.append(i)

if flag == 0:
    for i in range(0, k):
        c.append(b[i])
else:
    for i in range(0, k):
        c.append(i)

print(b)

print(c)
