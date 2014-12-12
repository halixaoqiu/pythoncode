#!/usr/bin/env python
#coding:UTF-8
'''
Created on 2014年12月3日
@author: qiu.lin
'''
import pexpect

def ssh_cmd(ip,user,pwd,cmd):
    ssh = pexpect.spawn('ssh %s@%s "%s"' %(user, ip, cmd))
    r = ""
    ret = -1
    try:
        i = ssh.expect(["password: ",'continue connecting (yes/no)?'])
        if i==0:
            ssh.sendline(pwd)
        elif i==1:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(pwd)
        if cmd=='1':
            ssh_cmd('10.1.102.147', 'qiu.lin', 'linqiu1987', 'ls')
        else:
            ssh.sendline(cmd)
        r = ssh.read()
        ret = 0
    except pexpect.EOF:
        ssh.close()
        ret = -3
    except pexpect.TIMEOUT:
        ssh.close()
        ret = -2
    else:
        ssh.close()
    return r,ret

hosts = '''192.168.8.172:qiu.lin:linqiu1987:1'''

for host in hosts.split("/n"):
    if host:
        ip,user,passwd,cmds = host.split(":")
        for cmd in cmds.split(","):
            print "-- %s run:%s --" % (ip, cmd)
            r,ret = ssh_cmd(ip, user, passwd, cmd)
            print r
            print ret


