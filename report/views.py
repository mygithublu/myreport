from __future__ import  unicode_literals
from django.shortcuts import render
import math
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import cx_Oracle
import socket
import urllib.request
import urllib.error

import time

from .date import *



def index(request):

    template = loader.get_template('report/report0426.html')
    # a, b, c, d= time1()
    month=month_out()  #年度月度产量
    month1=month_m() #月数
    shift=shift_out() #当班实时产量
    cu_month=current_month()   #当月实时产量
    # T1, T2, C1, C2, C3 = downtime()
    curday=day()   #绿十字当前天
    context = dict(
        # a=a,
        # b=b,
        # c=c,
        # d=d,
        # T1=T1,
        # T2=T2,
        # C1=C1,
        # C2=C2,
        # C3=C3,
        p=pp,
        month=month,
        shift=shift,
        cu_month=cu_month,
        curday=curday,
        HPV=HPV,
        zhongzhuan=zhongzhuan,
        dazhuan = dazhuan,
        benke = benke,
        shuoshi = shuoshi,
        qita = qita,
        list=list,
        suggest=suggest,
        onepass=onepass,
        PR=PR,
        BS=BS,
        PS=PS,
        GA=GA,
        month1=month1,
        month_value=month_value,
        sumvalue=sumvalue,


    )
    return HttpResponse(template.render(context, request))

def envir(request):
    template = loader.get_template('report/envir.html')
    a, b, c, d = time1()
    m_zs11, m_zs12, m_ap31 = month_out()
    T1,T2,C1,C2,C3=downtime()
    context = dict(
        a=a,
        b=b,
        c=c,
        d=d,
        m_zs11=m_zs11,
        m_zs12=m_zs12,
        m_ap31=m_ap31,
        T1=T1,
        T2=T2,
        C1=C1,
        C2=C2,
        C3=C3,

    )
    return HttpResponse(template.render(context, request))

