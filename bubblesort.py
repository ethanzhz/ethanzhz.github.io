def bubbleSort(a):
    for j in range(len(a) - 1 ):
        for i in range(len(a) - 1 - j):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
a = []
while 1:
    num =input("请输入一个数：")
    if num == '':
        break
    else:
        a.append(int(num))
bubbleSort(a)
print(a)