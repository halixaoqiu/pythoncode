#coding:UTF-8
'''
Created on 2014年3月31日

@author: skywalker
'''

import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen("http://www.zhihu.com/question/23177563")
soup = BeautifulSoup(page)
all_answer = soup.find("div",  {'id':'zh-question-answer-wrap'})
answer_list = all_answer.findAll("div",  {'class':'zm-item-answer'})

answer_list2 = []
for ans in answer_list:
    answer_list2.append(ans.findAll("div", {'class':'zm-editable-content'}))
    
print answer_list2