import os
import configparser


def get_filename_from_path(path):
    base_name = os.path.basename(path)  # 获取路径的基本名称
    file_name, _ = os.path.splitext(base_name)  # 去掉文件扩展名
    return file_name


def run(my_cpp_filename, correct_cpp_filename):
    # 运行程序并输出结果
    os.system(f'{my_cpp_filename}.exe < data.txt > {my_cpp_filename}.dat')
    os.system(f'{correct_cpp_filename}.exe < data.txt > {correct_cpp_filename}.dat')


def check(my_cpp_filename, correct_cpp_filename):
    # 逐行对比运行结果
    with open(f'{my_cpp_filename}.dat', 'r') as my, open(f'{correct_cpp_filename}.dat', 'r') as correct,open('log.txt', 'w') as log:
        log.write('-----------All Error-----------\n')
        for (i, (a, b)) in enumerate(zip(my, correct)):
            if a != b:
                log.write('line ' + str(i + 1) + '\n')
                log.write('---MY:' + a)
                log.write('---AC:' + b)
                return False
    return True


def main():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')
    my_cpp_path = config.get('DEFAULT', 'my')
    correct_cpp_path = config.get('DEFAULT', 'correct')

    # 获取文件名
    my_cpp_filename = get_filename_from_path(my_cpp_path)
    correct_cpp_filename = get_filename_from_path(correct_cpp_path)
    print(f"my_cpp_filename: {my_cpp_filename}")
    print(f"correct_cpp_filename: {correct_cpp_filename}")

    # 编译C++文件
    os.system(f'g++ {my_cpp_path} -o {my_cpp_filename}.exe')
    os.system(f'g++ {correct_cpp_path} -o {correct_cpp_filename}.exe')

    count = 1
    while True:
        print(f"比较次数: {count}")
        os.system('python data.py')
        run(my_cpp_filename, correct_cpp_filename)
        if not check(my_cpp_filename, correct_cpp_filename):
            print('WA')
            break
        else:
            print('AC')
        count += 1


if __name__ == '__main__':
    main()
