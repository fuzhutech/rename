import os
import sys


def test():
    # 获取当前路径
    print(os.getcwd())
    # 获取当前文件名
    print(sys.argv)
    # 获取当前文件名路径
    print(os.path.join(os.getcwd(), sys.argv[0]))

    print(os.path.abspath('.'))  # 获取当前工作目录路径
    print(os.path.abspath('test.txt'))  # 获取当前目录文件下的工作目录路径
    print(os.path.abspath('..'))  # 获取当前工作的父目录 ！注意是父目录路径
    print(os.path.abspath(os.curdir))  # 获取当前工作目录路径

    pathDir = os.listdir(sys.path[0])  # 文件创建在当前目录中，用来获取当前目录内所有文件名


def file_name(file_dir):
    for root_dir, child_dirs, file_names in os.walk(file_dir):
        print(root_dir)  # os.walk()所在目录路径
        print(child_dirs)  # os.walk()所在目录路径下所有子目录
        print(file_names)  # os.walk()所在目录路径下所有非目录子文件名


split = '__'

fileDir = dict(
    权益部本周工作总结及下周工作计划='01',
    固定收益部本周工作总结及下周工作计划='02',
    股权部本周工作总结及下周工作计划='03',
    另类及不动产投资部本周工作总结及下周工作计划='04',
    研究发展部本周工作总结及下周工作计划='05',
    风险管理部本周工作总结及下周工作计划='06',
    信评部本周工作总结及下周工作计划='07',
    财务部本周工作总结及下周工作计划='08',
    交易部本周工作总结及下周工作计划='09',
    综合部本周工作总结及下周工作计划="10"
)

fileDir_c = dict(
    权益部='01' + split + '权益部本周工作总结及下周工作计划',
    固定收益部='02' + split + '固定收益部本周工作总结及下周工作计划',
    股权部='03' + split + '股权部本周工作总结及下周工作计划',
    另类及不动产投资部='04' + split + '另类及不动产投资部本周工作总结及下周工作计划',
    研究发展部='05' + split + '研究发展部本周工作总结及下周工作计划',
    风险管理部='06' + split + '风险管理部本周工作总结及下周工作计划',
    信评部='07' + split + '信评部本周工作总结及下周工作计划',
    财务部='08' + split + '财务部本周工作总结及下周工作计划',
    交易部='09' + split + '交易部本周工作总结及下周工作计划',
    综合部="10" + split + '综合部本周工作总结及下周工作计划'
)


def rename(root_dir, old_name):
    for key in fileDir.keys():
        index = old_name.find(key)
        if index > -1:  # 存在需要重命名的文件
            new_name = fileDir.get(key) + split + old_name[index:]
            if old_name != new_name:
                # 文件重命名
                os.rename(os.path.join(root_dir, old_name), os.path.join(root_dir, new_name))
                print("重命名文件: %s =>  %s" % (old_name, new_name))
            break


def deal_r(path):
    # 获取指定目录下的子目录和文件名称
    print("开始搜索并重命名【%s】路径下的文件" % (os.path.abspath(path)))
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if os.path.splitext(file)[1].lower() in ('.xlsx', '.xls'):
                rename(root, file)


def rename_c(root_dir, old_name):
    [name, ext] = os.path.splitext(old_name)
    if ext.lower() in ('.xlsx', '.xls'):
        for key in fileDir_c.keys():
            index = old_name.find(key)
            if index > -1:  # 存在需要重命名的文件
                new_name = fileDir_c.get(key) + name[-8:] + ext
                if old_name != new_name:
                    # 文件重命名
                    os.rename(os.path.join(root_dir, old_name), os.path.join(root_dir, new_name))
                    print("重命名文件: %s =>  %s" % (old_name, new_name))
                break


def deal_f(path):
    """
    rename -f "F:/test"
    按照约定规范重命名当前目录下的文件名
    """
    # 获取当前工作目录路径
    root_dir = os.path.abspath(path)
    print("开始搜索并重命名【%s】路径下的文件" % root_dir)
    for name in os.listdir(path):
        rename_c(root_dir, name)


if __name__ == '__main__':
    path = '.'
    arg_f = False
    arg_r = False
    for arg in sys.argv[1:]:
        if arg == '-f':
            print("获取到参数[-f],简单规则强制修改文件名")
            arg_f = True
        elif arg == '-r':
            print("获取到参数[-r],遍历目录下所有文件，包括子目录")
            arg_f = True
        elif os.path.isdir(arg):
            print("获取到目录参数[%s]" % arg)
            path = arg

    if arg_f:
        deal_f(path)
    elif arg_r:
        deal_r(path)
    else:
        deal_f(path)
