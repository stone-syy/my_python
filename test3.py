import os
import sys
class c1():
    pass

class Hello():
    data = "hello world"
    def stone(self, x):
        print(x)
a = Hello()
a.stone("Hello world good moronning")
print(a.data)
issubclass(Hello,c1)

print(os.getcwd())
print(sys.path)