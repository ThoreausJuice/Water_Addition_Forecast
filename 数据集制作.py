#!/usr/bin/env python3

# 加水预测，训练集（202101_training.csv）,测试集制作（202101_test.csv）,类别标签集制作（202101_category.csv）

from math import floor

with open('202101.csv', 'r', encoding='utf-8') as f:
    original_string = f.read()

# 预处理 + 去除文件结尾的空值
first_processing = original_string.split('\n')
if first_processing[-1] == '':
    first_processing.pop()

# 计算测试集应有多少数据
amount_of_data = len(first_processing)
volume_of_test_set = floor(amount_of_data * 0.2)

# 计算提取数据的间隔
interval = floor(amount_of_data / volume_of_test_set)

# 划分三个集合文件，注意从1开始，避开数据抬头
with open('202101_test.csv', 'w', encoding='utf-8') as a:
    with open('202101_training.csv', 'w', encoding='utf-8') as b:
        with open('202101_category.csv', 'w', encoding = 'utf-8') as c:
            for i in range(0,306):
                if i == 0:
                    c.write(first_processing[i])
                elif i % 5 == 0 and i != 0:
                    a.write(first_processing[i])
                    a.write('\n')
                else:
                    b.write(first_processing[i])
                    b.write('\n')