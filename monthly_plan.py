import os
from datetime import datetime

split = '__'

file_dict = dict(
    权益投资部='01' + split + '权益投资部',
    权益='01' + split + '权益投资部',
    固定收益部='02' + split + '固定收益部',
    固收='02' + split + '固定收益部',
    股权投资部='03' + split + '股权投资部',
    股权='03' + split + '股权投资部',
    另类投资部='04' + split + '另类投资部',
    另类='04' + split + '另类投资部',
    不动产投资部='05' + split + '不动产投资部',
    不动产='05' + split + '不动产投资部',
    研究发展部='06' + split + '研究发展部',
    风险管理部='07' + split + '风险管理部',
    信评部='08' + split + '信用评估部',
    信用评估部='08' + split + '信用评估部',
    财务部='09' + split + '财务部',
    交易部='10' + split + '交易部',
    综合部="11" + split + '综合部'
)


def rename(root_dir, old_name):
    [_name, ext] = os.path.splitext(old_name)
    if ext.lower() in ('.xlsx', '.xls'):
        for key in file_dict.keys():
            index = old_name.find(key)
            if index > -1:  # 存在需要重命名的文件
                new_name = file_dict.get(key) + old_name[index + len(key):]
                if old_name != new_name:
                    # 文件重命名
                    os.rename(os.path.join(root_dir, old_name), os.path.join(root_dir, new_name))
                    print("重命名文件: %s =>  %s" % (old_name, new_name))
                break


def deal(path):
    """
    rename -f "F:/test"
    按照约定规范重命名当前目录下的文件名
    """
    # 获取当前工作目录路径
    root_dir = os.path.abspath(path)
    print("开始搜索并重命名【%s】路径下的文件" % root_dir)
    for name in os.listdir(path):
        rename(root_dir, name)


if __name__ == '__main__':
    path1 = '.'
    deal(path1)
