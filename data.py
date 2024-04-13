import random

# 生成样例个数T
T = random.randint(1, 10000)

# 打开文件
with open('data.txt', 'w') as f:
    # 写入样例个数
    f.write(str(T) + '\n')
    # 生成每个样例
    for _ in range(T):
        # 生成k
        k = random.randint(1, 1 << 60)
        # 写入k
        f.write(str(k) + '\n')