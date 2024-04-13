import random

from problem1.dataRandom import random_string


def generate_data():
    # 随机生成整数T
    T = random.randint(1, 100)

    # 打开文件
    with open('data.txt', 'w') as f:
        # 写入T
        f.write(str(T) + '\n')

        # 生成T个数据样例
        for _ in range(T):
            # 随机生成字符串长度，上限为10^3
            str_length = random.randint(1, 10**3)
            # 生成比字符串长度小的整数
            num = 1 if str_length == 1 else random.randint(1, str_length - 1)

            # 写入整数和字符串
            f.write(str(num) + '\n')
            f.write(random_string(str_length) + '\n')

# 调用主函数
generate_data()

# 调用主函数
generate_data()