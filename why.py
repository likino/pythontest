# -*- coding: utf-8 -*-
#---------------------------------------
#   程序：spidertool.py
#   版本：0.1
#   作者：why
#   日期：2014-04-18
#   语言：Python 2.7.5
#
#   版本列表：
#   0.1：添加GET和POST
#---------------------------------------

import urllib  
import urllib2
import cookielib
import re
import string

class WhySpider:
    
    # 初始化爬虫  
    def __init__(self):
        self.cookie_jar = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie_jar))

    # 发送GET请求
    #
    def send_get(self,get_url):
        result = ""
        try:
            my_request = urllib2.Request(url = get_url)
            result = self.opener.open(my_request).read()
        except Exception,e:
            print "Exception : ",e
        return result

    # 发送POST请求
    def send_post(self,post_url,post_data):
        result = ""
        try:
            my_request = urllib2.Request(url = post_url,data = post_data)
            result = self.opener.open(my_request).read()
        except Exception,e:
            print "Exception : ",e
        return result
        

# 测试一下
if __name__ == '__main__':
    mySpider = WhySpider()  
    print mySpider.send_get('http://www.baidu.com')  