import numpy as np
##生成正态分布

class variation:
    def __init__(self,name,mean,std,size):
        self.name = name
        self.mean = mean
        self.std = std
        self.size = size
        self.data = np.random.normal(mean, std, size)
        self.relmean = np.mean(self.data)



toxe = variation('toxe',2.73e-9, 1.0e-9, 500)

'''
meanToxe = 2.73e-9

stdToxe  = 1.0e-9

meanH0  =   4.0000e-06
stdH0   =   1.0e-6

dataWriteTofile = 'inputDATA.dat'

toxe    =   np.random.normal(meanToxe, stdToxe, 500)
h0      =   np.random.normal(meanH0, stdH0, 500)


f = open(dataWriteTofile.'w')

##使成为二维数组
z = np.column_stack((toxe, h0))
print(z)
##输出toxe均值
print(np.mean(z[:, 0]))
##输出toxe中位数
print(np.median(z[:, 0]))
##输出两组数据相关系数
print(np.corrcoef(z[:, 0 ], z[:, 1]))
##输出toxe标准差
print(np.std(z[:, 0]))


'''