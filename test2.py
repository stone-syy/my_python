#学习九九乘法表
import os
import json
def chengfabiao():
    for i in range(1, 10):
        for j in range(1, 10):
            if i >= j:
                print("%d*%d=%d\t" %(i, j, i*j), end="")
        print()
info = input("现在开始学习九九乘法表，你愿意吗（YES/NO）?:")
if info.lower() == 'yes':
    chengfabiao()
    print("恭喜你，成功的学习了九九乘法表")
elif info.lower() == 'no':
    print("很遗憾你没能学习九九乘法表")
    exit()
else:
    print("请输入YES/NO")

print(os.getcwd())
print(os.stat('xie_zheng.txt'))
import re
str1 = 'jl.dsaf.dfa.f.dsaf.as.f.s.f.asdf.sd'
abc = str1.split('.')
print(abc)
data = json.dump()



