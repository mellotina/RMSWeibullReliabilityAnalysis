#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 18:43:37 2022

@author: zhangtian
"""

import numpy as np
import matplotlib.pyplot as plt
#x,y=symbols('x y')
from math import e
font1={'family':'Times New Roman','weight':'normal','size':13}
#%%
def calculateRF(xmin,xmax,step,shape,scale,n,c):
    x=[[1 for i in range(step)] for j in range(n)]
    for j in range(n):
        x[j]=list(np.linspace(xmin[j],xmax[j],step))
    R=[[1 for i in range(step)] for j in range(n)]
    F=[[1 for i in range(step)] for j in range(n)]
    for j in range(n):
        for i in range(step):
            R[j][i]=e**(-((x[j][i]-xmin[j])/scale[j])**shape[j])
            F[j][i]=1-e**(-((x[j][i]-xmin[j])/scale[j])**shape[j])
        plt.plot(x[j],R[j],color=c[j])
        #plt.plot(x[j],F[j],color=c[j])
        plt.legend(["config.1",'config.2','config.3'])
        plt.grid()
        plt.xlabel("Time (day)",font1)
        plt.ylabel("Reliability",font1)
        
    return R,F