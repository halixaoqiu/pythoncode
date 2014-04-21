#!/usr/bin/env python
#coding:UTF-8

import urllib2
from sgmllib import SGMLParser
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class UrlParser(SGMLParser):
    urls = []
    def do_a(self,attrs):
        '''parse tag a'''
        for name,value in attrs:
            if name=='href':
                self.urls.append(value)
            else:
                continue
    
    def do_link(self,attrs):
        '''parse tag link'''
        for name,value in attrs:
            if name=='href':
                self.urls.append(value);
            else:
                continue

def getHtml(url,type='urllib2'):
    '''跟type用不同的方式获取html'''
    content = ''
    
    #urllib2的方式只能获取静态html
    if type=='urllib2':
        page = urllib2.urlopen(url)
        content = page.read()
        page.close()
    
    #selenium的方式可以获取动态html
    if type=='selenium':
        browser = webdriver.Firefox()
        browser.get(url)
    
    return content

def checkUrl(checkurl, isDetail):
    '''检查checkurl对应的网页源码是否有非法url'''
    parser = UrlParser()
    content = getHtml(checkurl,'selenium')
    #content = unicode(content, "gb2312").encode("utf8")
    parser.feed(content)
    urls = parser.urls
    
    dailyUrls = []
    detailUrl = ""
    for url in urls:
        if 'daily' in url:
            dailyUrls.append(url);
        if not detailUrl and not isDetail and 'detail.ju.taobao.com' in url:
            detailUrl = url
    
    parser.close()
    
    if isDetail:
        return dailyUrls
    else:
        return dailyUrls,detailUrl

def sendMail():
    '''发送提醒邮件'''
    #kelude有个发送邮件的http接口，申请了就可以调用
    pass
    
def log(content):
    '''记录执行日志'''
    logFile = 'checkdailyurl.log'
    f = open(logFile,'a')
    f.write(str(time.strftime("%Y-%m-%d %X",time.localtime()))+content+'\n')
    f.flush()
    f.close()

def main():
    '''入口方法'''
    #检查ju
    url = "http://ju.taobao.com"
    #dailyUrls保存检查到的daily链接
    #detailUrl保存一个judetail链接，用来检查judetail页面
    dailyUrls,detailUrl=checkUrl(url, False)
    if dailyUrls:
        #检查到daily链接，发送告警邮件
        sendMail()
        log('check ju: find daily url')
        print "检查到ju"
    else:
        #没检查到daily链接，不处理
        log('check ju: not find daily url')
        print "没检查到ju"

    #检查judetail
    dailyUrls=checkUrl(detailUrl, True)
    if dailyUrls:
        #检查到daily链接，发送告警邮件
        log('check judetail: find daily url')
        sendMail()
        print "检查到judetail"
    else:
        #没检查到daily链接，不处理
        log('check judetail: not find daily url')
        print "没检查到judetail"

if __name__ == '__main__':
    main()