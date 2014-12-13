#!/usr/bin/env python
#coding:UTF-8
'''
Created on 2014年12月3日
@author: qiu.lin
'''
import sys
import pexpect
import getpass

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

hosts = '''192.168.8.172:qiu.lin:linqiu1987:ls'''

def main():
    args = sys.argv
    if len(args)==3:
        host_file = args[1]
        cmd = args[2]
        user = raw_input("username:")
        pwd = getpass.getpass('password:')
        for line in open(host_file):
            host=line.strip('\n')
            if host:
                print "-- %s run:%s --" % (host, cmd)
                r,ret = ssh_cmd(host, user, pwd, cmd)
                print r
                print ret
    else:
        print 'illegal script arguments'

if __name__ == '__main__':
    main()

# for host in hosts.split("/n"):
#     if host:
#         ip,user,passwd,cmds = host.split(":")
#         for cmd in cmds.split(","):
#             print "-- %s run:%s --" % (ip, cmd)
#             r,ret = ssh_cmd(ip, user, passwd, cmd)
#             print r
#             print ret


