import numpy as np
import matplotlib.pyplot as plt
from pylab import *


#导入matplotlib的全部


N=3
ind=np.arange(N)
width=0.4
adjust=0.1
boys=(47,427,245)
girls=(210,20,55)


(fig,ax)=plt.subplots()

#创建子图

rects1=plt.bar(ind+adjust,boys,width,color='turquoise',edgecolor='navy',linewidth=1.5)
rects2=plt.bar(ind+width+adjust,girls,width,color='salmon',edgecolor='navy',linewidth=1.5)

#创建柱状图，设置左端x坐标、高度、宽度、颜色、边框颜色及宽度

mpl.rcParams['font.sans-serif']=['SimHei']

#使matplotlib显示中文字体


plt.title('北航2016级新生男女比')
plt.xlabel('院系')
plt.ylabel('人数')

#设置标题及xy轴标签

plt.xticks(ind+width+adjust)

#设置x轴记号的位置

plt.legend((rects1,rects2),('boys','girls'))

#设置图例

ax.set_xticklabels(('知行书院','飞行学院','高等理工学院'))

#将x轴记号设置为具体文字

def autolabel(rects):
    for rect in rects:
        height=rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2,1.005*height,int(height),ha='center',va='bottom',fontsize=12,withdash=False)

#定义函数以得到柱高并显示在适当位置
        
autolabel(rects1)
autolabel(rects2)

#调用函数

plt.show()

##Let's pretend that here is the last part of the program completed by YaoJiang2 
