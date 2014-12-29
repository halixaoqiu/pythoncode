#!/usr/bin/env python
#coding:UTF-8
'''
Created on 2014年12月29日

@author: qiu.lin
'''
import sys

def split_cities(cities):
    if cities:
        cities = cities.strip('\n')
        city_list = cities.split('/');
        ret = [];
        for city in city_list:
            ret.append(city.strip())
    return ret

def main():
    args = sys.argv
    if len(args)==3:
        deal_file = args[1]
        city_list = split_cities(args[2])
        str = ""
        for line in open(deal_file):
            deal=line.strip('\n')
            if deal:
                for city in city_list:
                    str += deal+"."+city+'\n'
        
        f = open('target.txt', 'w')
        f.write(str)
        f.close()
        print str
    else:
        print 'illegal script arguments'
        
if __name__ == '__main__':
    main()