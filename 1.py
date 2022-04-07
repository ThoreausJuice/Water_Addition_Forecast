#!/usr/bin/env python3

# 加水预测试作

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

# # 加载类别标签
# with open('202101_category.csv', encoding='utf-8') as a:
#     a_original_string = a.read()

# a_first_processing = a_original_string.split(',')
# i = 0
# for ele in a_first_processing:
#     # print(i,ele)
#     i+=1


# 正文如下：
# 数据读入及预处理
training_list = Basic_file_processing('202101_training.csv')
test_list = Basic_file_processing('202101_test.csv')

# 设定k值
k = 3
# 设定精度（具体值）
accuracy = 0.9
# 设定精度（误差占比：误差÷真实值）
error_percentage = 5 / 1000
# 测试计数
correct = 0

# 测试开始
for x in test_list:
    x_converted = convert(x)
    # 初始化 计算值 数组，该者为多对数组组成的二维数组
    calculated_value_array = []
    for y in training_list:
        y_converted = convert(y)
        # 初始化 计算值：[预测值， 距离]，其为一对数组成的一维数组
        calculated_value = []
        # 计算二者间的 欧氏距离
        Euclidean_distance = np.linalg.norm(x_converted[1:] - y_converted[1:])
        # 先把预测值加入数组
        calculated_value.append(y_converted[0])
        # 再把对应的 欧氏距离 加入数组
        calculated_value.append(Euclidean_distance)
        # 最后将二者一并加入 二维数组
        calculated_value_array.append(calculated_value)
        # 对 二维数组 进行 排序 和 裁剪
        if len(calculated_value_array) > k:
            # 将 二维数组 转换成 numpy 可用
            calculated_value_array = np.array(calculated_value_array)
            # 这一步是对二维数组进行排序，排序依据为最后一列（猪上天）
            calculated_value_array = calculated_value_array[np.lexsort(calculated_value_array.T)]
            # 删除最后一个元素
            calculated_value_array = np.delete(calculated_value_array, k, 0)
            # 将 二维数组 变回列表
            calculated_value_array = calculated_value_array.tolist()
        # print(Euclidean_distance)
    # if abs(x_converted[0] - calculated_value_array[0][0]) < accuracy:
    if abs(x_converted[0] - calculated_value_array[0][0])/x_converted[0] < error_percentage:
        correct += 1
        print('实际值：', x_converted[0], '预测值：', calculated_value_array[0][0])
        print('预测正确')
    else:
        print('实际值：', x_converted[0], '预测值：', calculated_value_array[0][0])
        print('Prediction Error')

prediction_accuracy = correct / len(test_list) * 100
print('\n正确率：', prediction_accuracy, '%')
# print(calculated_value_array)