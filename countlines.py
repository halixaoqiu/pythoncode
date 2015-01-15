#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

FORMATE = '%-80s%0s'

def count_current_dir_files(path):
    print FORMATE %('code file','counts')
    total_lines = 0;
    for parent,dirnames,filenames in os.walk(path):
        if('.git' in parent or '.settings' in parent or 'site-packages' in parent):
            continue
        for filename in filenames:
            if '.pydevproject' in filename:
                continue
            if '.sh' in filename or '.py' in filename or '.htm' in filename or '.txt' in filename or '.sql' in filename:
                path = parent+'/'+filename
                lines = sum([1 for line in open(path)])
                total_lines += lines
                print FORMATE %(path,lines)
    print FORMATE %('total lines',total_lines)
    
def main():
    root = os.path.dirname(__file__)
    if root:
        count_current_dir_files(root)
    pass

if __name__ == '__main__':
    main()
