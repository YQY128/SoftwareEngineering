import time
import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

i = 0
j = 0
d = 0
line = {}    #从文件中读取出的数据行
cubage = {}  #背包最大容量 
profit = {}  #各物品的价值
weight = {}  #各物品的重量
pw = {}      #各物品的价值/重量比
third = {}

#读取文件
with open('idkp1-10.txt') as f:
    for line[i] in f:
        i=i+1
i=int(input('希望查找第几组数据（0~10）：'))
cubage[i]=max(list(map(int,re.findall(r'\d+',line[i*8+3]))))
profit[i]=list(map(int,re.findall(r'\d+',line[i*8+5])))
weight[i]=list(map(int,re.findall(r'\d+',line[i*8+7])))
pw[i]=list(map(lambda x:x[0]/x[1],zip(profit[i],weight[i])))

#输出重要数据
print('\n背包最大容量：',cubage[i])
print('\n物品价值：',profit[i])
print('\n物品重量：',weight[i])
print('\n价值：重量比：',pw[i])

#散点图
plt.xlabel('weight')
plt.ylabel('profit')
plt.scatter(weight[i],profit[i])
plt.show()

#按价值：重量比排序
if i==0:
    d=10
else:
    d=i*100
for j in range(0,d):
    z=j*3+2
    third[j]=pw[i][z]
third=sorted(third.items(),key=lambda x:x[1],reverse=True)
print('\n按价值：重量比对项集第三项进行降序排序：\n',third)

#动态规划算法
def bag(n, c, w, v):
    # 保存状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    return value

#输出动态规划算法的结果
def show(n, c, w, value):
    print('动态规划算法：\n最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个 ', end='')
    with open('dpa.txt','w') as f:
        f.write(f'最大价值为：{value[n][c]}')
        f.write(f'\n背包中所装物品为：')
        for i in range(n):
            if x[i]:
                f.write(f'第{i+1}个 ')

#回溯算法
bestV = 0     #最大价值
currW = 0     #当前背包重量
currV = 0     #当前背包价值
bestx = None  #最优解路径
def backtrack(i):
    global bestV,bestx,currV,currW,x
    if i>= n:
        if bestV<currV:
            bestV = currV
            bestx = x[:]
    else:
        if currW+w[i]<=c:
            x[i]=1
            currW += w[i]
            currV += v[i]
            backtrack(i+1)
            currW -= w[i]
            currV -= v[i]
        x[i]=0
        backtrack(i+1)

n = 3*d        #物品数量
c = cubage[i]  #容量
w = weight[i]  #物品重量
v = profit[i]  #物品价值
a=int(input('选择算法（1、动态规划算法，2、回溯算法）：'))  #选择算法
if a==1:
    #动态规划算法
    start1=time.perf_counter()
    value = bag(n, c, w, v)
    show(n,c,w,value)
    end1=time.perf_counter()
    time1=end1-start1
    with open('dpa.txt','a') as f:
        f.write(f'\n运行时间：{time1}')
    print('\n运行时间：',time1)
elif a==2:
    #回溯算法
    start2=time.perf_counter()
    x = [0 for z in range(n)]
    backtrack(0)
    print('\n回溯算法：\n最大价值为:',bestV) #最大价值
    print('背包中所装物品为:')
    for z in range(n):
        if bestx[z]:
            print('第', z+1, '个 ', end='')
    end2=time.perf_counter()
    time2=end2-start2
    with open('ba.txt','w') as f:
        f.write(f'最大价值为：{bestV}')
        f.write(f'\n背包中所装物品为：')
        for z in range(n):
            if bestx[z]:
                f.write(f'第{z+1}个 ')
        f.write(f'\n运行时间：{time2}')
    print('\n运行时间：',time2)
