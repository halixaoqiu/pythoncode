#!/usr/bin/env python
#coding:UTF-8
'''
Created on 2014年12月3日
@author: qiu.lin
'''

import urllib
import urllib2
import hashlib

# [0] = {com.dianping.tuangou.remote.common.Pair@7277}"(method, send)"
# [1] = {com.dianping.tuangou.remote.common.Pair@7278}"(mobile, 18317211633)"
# [2] = {com.dianping.tuangou.remote.common.Pair@7279}"(num, 3)"
# [3] = {com.dianping.tuangou.remote.common.Pair@7280}"(out_order_id, 266486499s916691326t71)"
# [4] = {com.dianping.tuangou.remote.common.Pair@7281}"(seller_id, 1721305230160)"
# [5] = {com.dianping.tuangou.remote.common.Pair@7282}"(sub_outer_iid, 1721402260250)"
# [6] = {com.dianping.tuangou.remote.common.Pair@7283}"(timestamp, 2014-12-04 17:05:53)"
# [7] = {com.dianping.tuangou.remote.common.Pair@7284}"(token, null)"
# [8] = {com.dianping.tuangou.remote.common.Pair@7285}"(total_fee, 180.00)"
# [9] = {com.dianping.tuangou.remote.common.Pair@7286}"(sign, EB30816DC5F573FD419B0B4FFB4BAD6B)"

# methodsendmobile18317211633num3out_order_id266486499s916691326t71seller_id1721305230160sub_outer_iid1721402260250timestamp2014-12-04 17:05:53total_fee180.00signc3fa9fc50c9bae1b0dafac11abbad33a

data = {"refundTime":"2014-10-11 00:00:00","returnCode":0,"returnCode111":0,"serialId":"123456789","voucherNumberList":[{"voucherNumber":"123321"}]}
data = urllib.urlencode(data)
url = 'http://t.51ping.com/play/servlet/refundnotify'
f = urllib2.urlopen(url, data)
rt = f.read()
print rt