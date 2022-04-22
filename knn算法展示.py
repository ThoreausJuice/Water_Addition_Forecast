#!/usr/bin/env python3

# 加水预测试作

import numpy as np
from Data_Processing_Function import *

# 正文如下：
# 数据读入及预处理
training_list = Basic_file_processing('training.csv')
test_list = Basic_file_processing('test.csv')

# 设定k值
k = 3
# 设定精度（具体值）
accuracy = 0.9
# 设定精度（误差占比：误差÷真实值）
error_percentage = 5 / 1000
# 测试计数
correct = 0
# 用于在对照数据集 和 测试集 都很大的情况下，实时显示正确率和进度用：
# 当前总数：
current_total = 0

# 测试开始
for x in test_list:
    x_converted = convert(x)
    # print(x_converted)
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
    # 误差δ
    δ = abs(x_converted[0] - calculated_value_array[0][0])
    if δ < accuracy:
    # if δ/x_converted[0] < error_percentage:
        correct += 1
        print('实际值：', x_converted[0], '预测值：', calculated_value_array[0][0])
        print('预测正确')
    else:
        print('实际值：', x_converted[0], '预测值：', calculated_value_array[0][0])
        print('Prediction Error')
    print(δ)
    print(calculated_value_array)

    current_total += 1

    print('当前正确率：', correct / current_total * 100, '%', '正确个数：', correct, '已跑数据量：', current_total, '/',len(test_list))

# print(correct, len(test_list))
prediction_accuracy = correct / len(test_list) * 100
print('\n总正确率：', prediction_accuracy, '%')