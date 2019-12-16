import time
start1 = time.perf_counter()
scale = 10
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(1)
print("\n"+"执行结束".center(scale//2, "-"))
end = time.perf_counter()
print("程序执行时间为{:.2f}s".format(end-start1))
print("你个哈狗输错了，必须输入一个数字才要的".center(30, "#"), end="")