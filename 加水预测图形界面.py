#!/usr/bin/env python3

# 加水预测图形界面试作
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tf
from PIL import Image,ImageTk
from pyparsing import col
# 这是自己写的函数 ↓
from Data_Processing_Function import *


# 建立一个根窗口
win = Tk()

# 获取屏幕的尺寸
# 获取屏幕的长度
scr_x = win.winfo_screenwidth()
# 获取屏幕的宽度
scr_y = win.winfo_screenheight()

# 设定窗口的尺寸
# 窗口的长度：x
win_x = scr_x * (4/5)
# 窗口的宽度：y
win_y = scr_y * (4/5)

# 设置窗口大小和位置
x = (scr_x - win_x) / 2
y = (scr_y - win_y) / 2
win.geometry('%dx%d+%d+%d' % (win_x, win_y, x, y))
# print(win_x, win_y, x, y)
# 添加窗口标题
win.title('Knn加水预测 图形界面试作')

# 布局尝试
# 顶部黑条
black_top = Frame(win, bg='#000000', height = 100)
black_top.pack(expand='no', fill='x')

ft_1 = tf.Font(family='微软雅黑', size=20, weight='bold')
txt1 = 'B线润叶加水流量预测'
Label(black_top, text=txt1, bg='#000000', fg='#FFFFFF', font=ft_1, height = 3, width = 20).pack(side='left')

# 夹层介绍
mezzanine = Frame(win, bg='#FFFFFF', height = 100)
mezzanine.pack(side='top', expand='no', fill='x', padx = 40, pady = 20)

img1 = Image.open('The-Majority-Voting-KNN-K6.png')
img1 = img1.resize((430, 255))
img1 = ImageTk.PhotoImage(img1)
Label(mezzanine, image=img1).pack(side='left')

ft_2 = tf.Font(family='微软雅黑', size=20, weight='bold')
txt2 = 'K-近邻算法预测'
Label(mezzanine, text=txt2, bg='#FFFFFF', fg='#000000', font=ft_2, height = 2).pack(side='top')

ft_3 = tf.Font(family='微软雅黑', size=15, weight='normal')
txt3 = '''优点：精度高、对异常值不敏感、无数据输入假定。\n
缺点：计算复杂度高、空间复杂度高。\n
简单地说，K-近邻算法采用测量不同特征值之间的距离进行预测'''
Label(mezzanine, text=txt3, bg='#FFFFFF', fg='#777777', font=ft_3, justify='left').pack(side='top')

# 正文图表
data_display = Frame(win, bg='#FFFFFF')
data_display.pack(side='left', expand='yes', fill='both', padx=40, pady = 10)

# 选项卡
style1 = ttk.Style()
style1.configure('my.TNotebook', tabposition='wn')

img2 = Image.open('历史数据.png')
img2 = img2.resize((145, 39))
img2 = ImageTk.PhotoImage(img2)

img3 = Image.open('加水预测.png')
img3 = img3.resize((145, 39))
img3 = ImageTk.PhotoImage(img3)

# 添加选项卡容器
note = ttk.Notebook(data_display, style='my.TNotebook', )
# 子选项卡容器
pane1 = Frame()
pane2 = Frame(bg='#FFFFFF')

# 添加选项卡
note.add(pane1, image=img2)
note.add(pane2, image=img3)

note.pack()

# 以下开始是 历史数据 的选项卡部分
# 加载类别标签
with open('category.csv', encoding='utf-8') as a:
    a_original_string = a.read()

a_first_processing = a_original_string.split(',')

# 猪在飞
columns = []

for ele in a_first_processing[0:]:
    if ele != '':
        columns.append(ele)

columns[0] = 'timee1'
columns[1] = 'timee2'
columns[2] = 'timee3'

xscroll = Scrollbar(pane1, orient=HORIZONTAL)
yscroll = Scrollbar(pane1, orient=VERTICAL)

table = ttk.Treeview(
            master=pane1,  # 父容器
            height=30,  # 表格显示的行数,height行
            columns=columns,  # 显示的列
            show='headings',  # 隐藏首列
            xscrollcommand=xscroll.set,  # x轴滚动条
            yscrollcommand=yscroll.set,  # y轴滚动条
            )

for ele in columns:
    table.heading(column=ele, text=ele)
    table.column(ele, anchor=S)

training_list = Basic_file_processing('training.csv')

for x in training_list:
    first_processing = x.split(',')
    second_processing = []
    for y in first_processing:
        if y != '':
            second_processing.append(y)
    table.insert('', END, values=second_processing)  # 添加数据到末尾

xscroll.config(command=table.xview)
xscroll.pack(side=BOTTOM, fill=X)
yscroll.config(command=table.yview)
yscroll.pack(side=RIGHT, fill=Y)
table.pack(fill=BOTH, expand=True)

# print(columns)

# 以下开始是 加水预测 的选项卡部分

# 初始化表格坐标
# 左侧为输入栏，分三栏，每栏颜色不一样
data_input_a = Frame(pane2, bg='#FFFFFF')
data_input_a.pack(side='left', fill='y')

data_input_b = Frame(pane2, bg='#CCCCCC')
data_input_b.pack(side='left', fill='y')

data_input_c = Frame(pane2, bg='#FFFFFF')
data_input_c.pack(side='left', fill='y')

# 右侧为预测栏
data_forecast = Frame(pane2, bg='#CCCCCC')
data_forecast.pack(side='left', fill='both', expand='yes')

# 记录需要打印的标签
data_to_be_used = []

# 第一阶段标签及输入框载入
for ele in columns[4:8]:
    Label(data_input_a, text=ele, bg='#FFFFFF', width=30, pady = 5).pack(anchor='nw', padx = 5, pady = 5)
    d_t_b_u = Entry(data_input_a, width=30, relief='ridge', bg='#CCCCCC')
    d_t_b_u.pack(anchor='nw', padx = 5)
    data_to_be_used.append(d_t_b_u)

# 第二阶段标签及输入框载入
for ele in columns[8:12]:
    Label(data_input_b, text=ele, bg='#CCCCCC', width=30, pady = 5).pack(anchor='nw', padx = 5, pady = 5)
    d_t_b_u = Entry(data_input_b, width=30, relief='ridge', bg='#FFFFFF')
    d_t_b_u.pack(anchor='nw', padx = 5)
    data_to_be_used.append(d_t_b_u)

# 第三阶段标签及输入框载入
for ele in columns[12:]:
    Label(data_input_c, text=ele, bg='#FFFFFF', width=30, pady = 5).pack(anchor='nw', padx = 5, pady = 5)
    d_t_b_u = Entry(data_input_c, width=30, relief='ridge', bg='#CCCCCC')
    d_t_b_u.pack(anchor='nw', padx = 5)
    data_to_be_used.append(d_t_b_u)

# 预测区域设置

# 预测功能实现
# 数据读入及预处理
training_list = Basic_file_processing('training.csv')
# 设定k值
k = 3
# 打印值字体设定
ft_6 = tf.Font(family='微软雅黑', size=10, weight='normal')


def Water_addition_prediction():
    # 历史数据要用到的标签列表
    label_list = []
    real_data = []
    for ele in data_to_be_used:
        data_input_real = ele.get()
        if data_input_real != '':
            real_data.append(float(data_input_real))
        else:
            real_data.append(0)
    x_converted = np.array(real_data)
    # 初始化 计算值 数组，该者为多对数组组成的二维数组
    calculated_value_array = []
    for y in training_list:
        y_converted = convert(y)
        # 初始化 计算值：[预测值， 距离]，其为一对数组成的一维数组
        calculated_value = []
        # 计算二者间的 欧氏距离
        Euclidean_distance = np.linalg.norm(x_converted - y_converted[1:])
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
    # print(calculated_value_array)
    # print(x_converted)
    for ele in historical_best_data.winfo_children():
        ele.destroy()
    for ele in algorithmic_recommendation_data.winfo_children():
        ele.destroy()
    
    label_h_b_d = Label(historical_best_data, text='   历史最优数据：', font=ft_5, bg='#CCCCCC',  pady = 5)
    label_h_b_d.pack(anchor='n', expand = 'no', padx = 5, pady = 5)
    label_a_r_d = Label(algorithmic_recommendation_data, text=' 算法推荐数据：', font=ft_5, bg='#CCCCCC',  pady = 5)
    label_a_r_d.pack(anchor='n', expand = 'no', padx = 5, pady = 5)

    for i in range(k):
        label_list.append(Label(historical_best_data, text=calculated_value_array[i][0], font=ft_6, bg='#CCCCCC', width=30, pady = 5))
        label_list[i].pack(side='top', padx = 5, pady = 5)

    final_label = Label(algorithmic_recommendation_data, text=calculated_value_array[0][0], font=ft_5, bg='#FFFFFF', width=30, pady = 5)
    final_label.pack(side='top', padx = 5, pady = 5)


ft_4 = tf.Font(family='微软雅黑', size=20, weight='normal')
Label(data_forecast, text='预测区', font=ft_4, bg='#CCCCCC', width=30, pady = 5).pack(anchor='n', padx = 5, pady = 5)
ft_5 = tf.Font(family='微软雅黑', size=15, weight='normal')
Label(data_forecast, text='根据左侧输入数据进行预测', font=ft_5, bg='#CCCCCC', width=30, pady = 5).pack(anchor='n', padx = 5, pady = 5)

Button(data_forecast, text='开始预测', font=ft_5, command=Water_addition_prediction).pack(anchor='n', padx = 5, pady = 5)

historical_best_data = Frame(data_forecast, bg='#CCCCCC')
historical_best_data.pack(side='left', fill='y')

algorithmic_recommendation_data = Frame(data_forecast, bg='#CCCCCC')
algorithmic_recommendation_data.pack(side='right', fill='y')

# 进入等待与处理窗口事件
win.mainloop()