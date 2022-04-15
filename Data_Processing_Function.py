#!/usr/bin/env python3

# 《数据处理函数》
# 该文件包含加水预测中所用到的自写函数

import numpy as np

# 函数功能：对文件进行基本处理，形成以回车为分隔符的数组
def Basic_file_processing(file_name):
    # 加载训练集
    with open(file_name, 'r', encoding = 'utf-8') as b:
        b_original_string = b.read()

    b_first_processing = b_original_string.split('\n')
    
    # 处理掉文件结尾的空值
    if b_first_processing[-1] == '':
        b_first_processing.pop()
    
    return b_first_processing

# 函数功能：对单行数据进行数组转化，方便后续计算
def convert(one_line):
    one_line_list = one_line.split(',')
    converted_group = [] # 初始化 已转化组
    for i in range(16):
        if i > 2 and one_line_list[i] != '':
            converted_group.append(float(one_line_list[i]))  # 将 实际值 + 待测组 暂存至 已转化组

    return np.array(converted_group)