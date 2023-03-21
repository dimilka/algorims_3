
a = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
# a = [[3, 0], [8, 0], [5, 1], [2, 3], [2, 4], [2, 5], [4, 2], [6, 1], [8, 1], [4, 5], [9, 0]]
# a = [[5, 0], [8, 0], [3, 2], [5, 2], [7, 1], [8, 2], [2, 6], [0, 7], [4, 5], [66, 0], [88, 0]]
a = sorted(a)
b = []
i = 0
while a:
    if len(a) == 1:
        b.append(a.pop(i))
    elif a[i][1] <= len(b):
        q = 0
        for j in range(len(b)):
            if b[j][0] >= a[i][0]:
                q += 1
        if q == a[i][1]:
            b.append(a[i])
            a.pop(i)
            i = 0
        else:
            if len(a) - 1 >= i + 1:
                i += 1
    else:
        if len(a) - 1 >= i + 1:
            i += 1

print(b)

