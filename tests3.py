#test
import os
movie = []
for root, dirs, files in os.walk('d:\movie'):
    for name in files:
        print(os.path.join(root, name))
        if str(name).endswith is not None:
            movie.append(name)
print(movie, '\n文件个数为{}个。'.format(len(movie)))
