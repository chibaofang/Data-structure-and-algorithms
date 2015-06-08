#-*- coding: utf-8 -*-  
#!/usr/bin/python  
import random
''''
生成一系列随机数,minNum/maxNum确定随机数的生成范围；
N限定数组长度
''''
list = [random.randint(minNum, maxNum) for i in xrange(N)]

''''' 
算法思想：每次从最后开始往前滚，邻接元素两两相比，小元素交换到前面 
第一轮循环把最小的元素上浮至第一个位置，第二小的元素上浮至第二个位置，依次类推 
''''  
def bubbleSort(list):  
    l=len(a)-2  
    i=0  
    while i<l:  
        j=l  
        while j>=i:  
            if(a[j+1]<a[j]):  
                a[j],a[j+1]=a[j+1],a[j]  
            j-=1  
        i+=1  
