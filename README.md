# Water_Addition_Forecast
    加水预测图形界面（试作）

## 文件功能介绍
    
### 数据集
    原始数据来源：
        202101.csv
    数据集制作：
        数据集制作.py
            功能：将202101.csv拆成三个文件：
                类表标签文件：202101_category.csv
                测试集文件：202101_test.csv
                训练集文件：202101_training.csv

### 预测程序相关文件
    算法核心及正确率展示：
        主文件：
            knn算法展示.py
        主文件涉及到的附属文件：
            Data_Processing_Function.py
            202101_test.csv
            202101_training.csv
        操作步骤：
            在主文件所在目录启动cmd，命令为：python knn算法展示.py
            运行结果包括：
                具体误差
                前k个值 eg: [[预测值, 距离],[],……,[]]
                实际值，预测值
                预测是否正确
                    最终正确率
        程序可更改项及对应影响：
            k值：
                决定算法选取前k个数据（当前并未对这些数据做额外处理，仅取距离最小的值，后续如有需要可以做加权平均等等额外处理，数组已备好，并已在运行结果中展示）
            精度：
                精度有两种，一个是具体值，一个是误差占比。每种精度都在程序后部分有相应的判断条件，更改精度将会直接影响正确率。举个例子：具体值精度设定为0.9，意味着最终结果在真实值的±0.9之间，这个正确率可以达到98.36%
                误差占比的设定为：误差÷真实值。设定这个判断标准的初衷是因为加水量存在一个较大的变动，有280的、190的、150的、0的，所以如需改为误差占比的正确率判断，可将第53和54行的注释符互换，如设定误差占比为千分之五，正确率可达到96.72%
    
    图形界面程序：
        主文件：
            加水预测图形界面.py
        主文件涉及到的附属文件：
            Data_Processing_Function.py
            202101_category.csv
            202101_training.csv
            加水预测.png
            历史数据.png
            The-Majority-Voting-KNN-K6.png
        操作步骤：
            在主文件所在目录启动cmd，命令为：python 加水预测图形界面.py
            运行结果为：
                一个图形界面，
                其中包括算法图片原理展示及算法文字介绍
                设有分页功能：
                    历史数据展示
                    预测数据输入及展示
                        预测数据输入若为空，程序会自动填充为0 
                        正确填写数字会根据程序预设的k值进行历史最优数据展示
                        并给出算法推荐的数据
        程序可更改项及对应影响：
            k值：
                与预测程序相同，并不会对结果产生影响，但由于图形界面存在展示功能，因此更改k值会影响展示的数据数量
        后续可升级项：
            1.如有额外需要可在“加水预测”分页栏下增添新的选项卡，进行其他的数据展示
            2.如有其他算法需要展示，可将算法说明部分重写，进行“算法选项卡”的设置，相当于将当前knn的说明界面、历史数据、预测数据作为一个大选项卡的其中一栏。
            3.当前程序并未对预测输入的值进行正规化，仅仅为了方便测试将空值记为0，后续可对非规范化输入进行判断并提示

### 程序打包相关事项
    使用pyinstaller进行打包，相关参数及影响如下：
        -F：将文件打包成一个exe文件
        -D：将文件打包成多个文件的文件夹，其中包括一个启动用的exe文件
        -w：去掉背后的黑色cmd框框
    具体命令及影响：
        pyinstaller -F -w 加水预测图形界面.py
            上述命令将会生成一个单独的exe文件，大小大概为280M，其中的问题为启动太慢，而且一个exe文件感觉上不太“正规”
        pyinstaller -D -w 加水预测图形界面.py
            上述命令将会生成一个文件夹，大小大概为700M，虽然更大了，但解决了启动太慢的问题，并且文件繁多，看上去就很“正规”
        最后解释一下文件过大及启动慢的问题：
            其根本原因在anaconda上，anaconda会在打包的过程中自行打包许多用不上的模块，因此单一的exe文件会先载入所有的模块然后在启动，因此花费的时间非常长。
            解决办法有两个，一个是在纯净的python环境下安装所需的模块后进行打包。另一种就是直接打包成文件夹。我选的是后者，因为看起来很像一个正规软件。
    文件存放位置：
        若想打包后的程序正常运行，需将所需文件放置在exe同级文件夹中。
        图形化程序所需的文件有：
            加水预测.png
            历史数据.png
            The-Majority-Voting-KNN-K6.png
            202101_category.csv
            202101_training.csv