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
