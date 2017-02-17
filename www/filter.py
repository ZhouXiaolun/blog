# coding: utf-8

from datetime import datetime
import time


def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%d分钟前' % (delta // 60)  # 整数除法
    if delta < 86400:
        return u'%d小时前' % (delta // 3600)
    if delta < 604800:
        return u'%d天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)
