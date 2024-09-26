num = int(input())
z = 100 - num * 9
if z < 0:
    print("小明欠了", -z, "元")
else:
    print("小明還剩", z, "元")