import time
import re
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import wx
import random
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

i = 0
j = 0
d = 0
fileNum = 0
line = {}
cubage = {}
profit = {}
weight = {}
pw = {}
third = {}
    
# 创建人机交互界面
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '读取文件', size=(600, 300))
        # 创建面板
        panel = wx.Panel(self)

        # 创建“确定”和“取消”按钮,并绑定事件
        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)
        # 创建文本，左对齐        
        self.title = wx.StaticText(panel, label="1、idkp1-10.txt    2、sdkp1-10.txt    3、udkp1-10.txt    4、wdkp1-10.txt\n")
        self.label_file = wx.StaticText(panel, label="希望读取的文件（1~4）：")
        self.text_file = wx.TextCtrl(panel, style=wx.TE_LEFT)
        # 添加容器，容器中控件按横向并排排列
        hsizer_file = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_file.Add(self.label_file, proportion=0, flag=wx.ALL, border=5)
        hsizer_file.Add(self.text_file, proportion=1, flag=wx.ALL, border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        # 添加容器，容器中控件按纵向并排排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,border=30)
        vsizer_all.Add(hsizer_file, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=20)
        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self,event):
        """ 点击确定按钮，执行方法 """
        message = ""
        global fileNum
        fileNum = int(self.text_file.GetValue())     # 获取输入的文件序号
        if self.text_file.GetValue() == '':    # 判断文件序号是否为空
            message = '输入不能为空'
        elif fileNum == 1 or fileNum == 2 or fileNum == 3 or fileNum == 4: # 文件序号正确
            #i=0
            global i
            if (fileNum==1):
                with open('idkp1-10.txt') as f:
                    for line[i] in f:
                        i=i+1
            if (fileNum==2):
                with open('sdkp1-10.txt') as f:
                    for line[i] in f:
                        i=i+1
            if (fileNum==3):
                with open('udkp1-10.txt') as f:
                    for line[i] in f:
                        i=i+1
            if (fileNum==4):
                with open('wdkp1-10.txt') as f:
                    for line[i] in f:
                        i=i+1
            message = '读取成功'    
        else:
            message = '输入序号不存在，请重新输入'    # 文件序号错误   
        wx.MessageBox(message)                        # 弹出提示框
        
        if (message == '读取成功'):
            frame2 = MyFrame2(parent=None,id=-1)  # 实例MyFrame2类，并传递参数
            frame2.Show() 

    def OnclickCancel(self,event):
        """ 点击取消按钮，执行方法 """
        self.text_file.SetValue("")     # 清空输入的文件序号

class MyFrame2(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '读取数据', size=(600, 300))
        # 创建面板
        panel = wx.Panel(self)

        # 创建“确定”和“取消”按钮,并绑定事件
        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnclickCancel)
        # 创建文本，左对齐        
        self.title = wx.StaticText(panel, label="除文件1外其他文件没有第0组数据")
        self.label_file = wx.StaticText(panel, label="希望查找第几组数据（0~10）：")
        self.text_file = wx.TextCtrl(panel, style=wx.TE_LEFT)
        # 添加容器，容器中控件按横向并排排列
        hsizer_file = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_file.Add(self.label_file, proportion=0, flag=wx.ALL, border=5)
        hsizer_file.Add(self.text_file, proportion=1, flag=wx.ALL, border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        hsizer_button.Add(self.bt_cancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        # 添加容器，容器中控件按纵向并排排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,border=30)
        vsizer_all.Add(hsizer_file, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=20)
        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self,event):
        """ 点击确定按钮，执行方法 """
        message = ""
        global i
        i = int(self.text_file.GetValue())      # 获取输入的文件序号
        if self.text_file.GetValue() == "" :    # 判断文件序号是否为空
            message = '输入不能为空'
        else:
            global fileNum
            global d
            if (fileNum == 1):
                if (i > -1 and i <= 10):
                    message = '读取成功'
                    if (i==0):
                        d=3*10
                    else:
                        d=i*100*3
                else:
                    message = '输入序号不存在，请重新输入'
            else:
                if (i >= 1 and i <= 10):
                    message = '读取成功'
                    d=i*100*3
                    i=i-1
                else:
                    message = '输入序号不存在，请重新输入'  
        wx.MessageBox(message)                        # 弹出提示框
        
        if (message == '读取成功'):
            frame3 = MyFrame3(parent=None,id=-1)      # 实例MyFrame3类，并传递参数
            frame3.Show()

    def OnclickCancel(self,event):
        """ 点击取消按钮，执行方法 """
        self.text_file.SetValue("")                   # 清空输入的文件序号

class MyFrame3(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '有效数据', size=(800, 800))
        
        # 创建面板
        self.panel = wx.Panel(self)
        title = wx.StaticText(self.panel, label='编号 价值 重量', pos=(100,20))
        font = wx.Font(14,wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)
        
        result = self.CreateDataBase()
        global d
        height = 30
        for j in range(0,d):
            height = height + 20
            wx.StaticText(self.panel,label='%8d  %8d  %8d'%(result[j][0],result[j][1],result[j][2]), pos=(100,height))
        #价值：重量比排序
        global third
        wx.StaticText(self.panel,label='按价值：重量比排序：', pos=(300,20))
        wx.StaticText(self.panel,label='编号  价值：重量比', pos=(300,50))
        global i
        for j in range(0,int(d/3)):
            z=j*3+2
            third[j]=pw[i][z]
        third=sorted(third.items(),key=lambda x:x[1],reverse=True)
        height = 50
        for j in range(0,int(d/3)):
            height = height + 20
            wx.StaticText(self.panel,label='%4d     %f'%(third[j][0],third[j][1]), pos=(300,height))
        #动态规划算法
        start1 = time.perf_counter()
        global cubage
        global profit
        global weight
        global heigh
        n = d          #物品数量
        c = cubage[i]  #容量
        w = weight[i]  #物品重量
        v = profit[i]  #物品价值
        value = self.bag(n, c, w, v)
        wx.StaticText(self.panel,label='动态规划算法：', pos=(500,20))
        self.show(n, c, w , value)
        end1 = time.perf_counter()
        time1 = end1 - start1
        with open('dpa.txt','a') as f:
            f.write(f'\n运行时间：{time1}')
        wx.StaticText(self.panel,label='\n运行时间：%f'%(time1), pos=(500,heigh))

        # 散点图
        plt.xlabel('weight')
        plt.ylabel('profit')
        plt.scatter(weight[i],profit[i])
        plt.show()

        # 遗传算法
        start2 = time.perf_counter()
        heigh = heigh+70
        m = 32      # 规模
        N = 500     # 迭代次数
        Pc = 0.8    # 交配概率
        Pm = 0.05   # 变异概率
        V =profit[i]
        W =weight[i]
        n = len(W)  # 染色体长度
        w = cubage[i]

        C = self.init(m, n)
        S,F  = self.fitness(C,m,n,W,V,w)
        B ,y = self.best_x(F,S,m)
        Y =[y]
        for i in range(N):
            p = self.rate(F)
            C = self.chose(p, C, m, n)
            C = self.match(C, m, n, Pc)
            C = self.vari(C, m, n, Pm)
            S, F = self.fitness(C, m, n, W, V, w)
            B1, y1 = self.best_x(F, S, m)
            if y1 > y:
                y = y1
            Y.append(y)
            
        wx.StaticText(self.panel,label='遗传算法：', pos=(500,heigh))
        
        heigh = heigh+30
        wx.StaticText(self.panel,label='最大价值为：%d'%(y), pos=(500,heigh))
        heigh = heigh+20
        wx.StaticText(self.panel,label='背包中所装物品编号为：', pos=(500,heigh))
        for i in range(len(S[0])):
            heigh = heigh+20
            wx.StaticText(self.panel,label='%d'%(S[0][i]), pos=(500,heigh))
            
        end2 = time.perf_counter()
        time2 = end2 - start2
        with open('dpa.txt','a') as f:
            f.write(f'\n运行时间：{time2}')
        height = height+40
        wx.StaticText(self.panel,label='\n运行时间：%f'%(time2), pos=(500,heigh))
            
        plt.plot(Y)
        plt.show()
        

    # 创建数据库
    def CreateDataBase(self):
        global i
        global d
        global cubage
        global profit
        global weight
        global pw
        conn = sqlite3.connect('mrsoft.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS user')
        cursor.execute('create table if not exists user (num int(10) primary key,profit int(20), weight int(20))')
        cubage[i] = max(list(map(int,re.findall(r'\d+',line[i*8+3]))))
        profit[i] = list(map(int,re.findall(r'\d+',line[i*8+5])))
        weight[i] = list(map(int,re.findall(r'\d+',line[i*8+7])))
        pw[i] = list(map(lambda x:x[0]/x[1],zip(profit[i],weight[i])))
        for j in range(0,d):
            cursor.execute('insert into user (num,profit,weight) values ("%d","%d","%d")'%(j,profit[i][j],weight[i][j]))
        cursor.execute('select * from user')
        result=cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        return result

    # 动态规划算法
    def bag(self,n,c,w,v):
        # 保存状态
        value = [[0 for j in range(c + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, c + 1):
                value[i][j] = value[i - 1][j]
                if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                    value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
        return value

    # 展示结果
    def show(self, n, c, w, value):
        global heigh
        heigh = 50
        wx.StaticText(self.panel,label='最大价值为：%d'%(value[n][c]), pos=(500,heigh))
        heigh = heigh + 20
        x = [False for i in range(n)]
        j = c
        for i in range(n, 0, -1):
            if value[i][j] > value[i - 1][j]:
                x[i - 1] = True
                j -= w[i - 1]
        wx.StaticText(self.panel,label='背包中所装物品编号为：', pos=(500,heigh))
        heigh = heigh + 20
        for i in range(n):
            if x[i]:
                wx.StaticText(self.panel,label='%d'%(i), pos=(500,heigh))
                heigh = heigh + 20
        with open('dpa.txt','w') as f:
            f.write(f'最大价值为：{value[n][c]}')
            f.write(f'\n背包中所装物品为：')
            for i in range(n):
                if x[i]:
                    f.write(f'第{i+1}个 ')
                    
    ##初始化,N为种群规模，n为染色体长度
    def init(self,N,n):
        C = []
        for i in range(N):
            c = []
            for j in range(n):
                a = np.random.randint(0,2)
                c.append(a)
            C.append(c)
        return C


    ##评估函数
    # x(i)取值为1表示被选中，取值为0表示未被选中
    # w(i)表示各个分量的重量，v（i）表示各个分量的价值，w表示最大承受重量
    def fitness(self,C,N,n,W,V,w):
        S = []##用于存储被选中的下标
        F = []## 用于存放当前该个体的最大价值
        for i in range(N):
            s = []
            h = 0  # 重量
            f = 0  # 价值
            for j in range(n):
                if C[i][j]==1:
                    if h+W[j]<=w:
                        h=h+W[j]
                        f = f+V[j]
                        s.append(j)
            S.append(s)
            F.append(f)
        return S,F

    ## 适应值函数,B位返回的种族的基因下标，y为返回的最大值
    def best_x(self,F,S,N):
        y = 0
        x = 0
        B = [0]*N
        for i in range(N):
            if y<F[i]:
                x = i
            y = F[x]
            B = S[x]
        return B,y

    ## 计算比率
    def rate(self,x):
        p = [0] * len(x)
        s = 0
        for i in x:
            s += i
        for i in range(len(x)):
            p[i] = x[i] / s
        return p

    ## 选择
    def chose(self,p, X, m, n):
        X1 = X
        r = np.random.rand(m)
        for i in range(m):
            k = 0
            for j in range(n):
                k = k + p[j]
                if r[i] <= k:
                    X1[i] = X[j]
                    break
        return X1

    ## 交配
    def match(self,X, m, n, p):
        r = np.random.rand(m)
        k = [0] * m
        for i in range(m):
            if r[i] < p:
                k[i] = 1
        u = v = 0
        k[0] = k[0] = 0
        for i in range(m):
            if k[i]:
                if k[u] == 0:
                    u = i
                elif k[v] == 0:
                    v = i
            if k[u] and k[v]:
                # print(u,v)
                q = np.random.randint(n - 1)
                # print(q)
                for i in range(q + 1, n):
                    X[u][i], X[v][i] = X[v][i], X[u][i]
                k[u] = 0
                k[v] = 0
        return X

    ## 变异
    def vari(self,X, m, n, p):
        for i in range(m):
           for j in range(n):
                q = np.random.rand()
                if q < p:
                    X[i][j] = np.random.randint(0,2)

        return X
        
if __name__ == '__main__':
    app = wx.App()                      # 初始化
    frame = MyFrame(parent=None,id=-1)  # 实例MyFrame类，并传递参数    
    frame.Show()                        # 显示窗口  
    app.MainLoop()                      # 调用主循环方法
