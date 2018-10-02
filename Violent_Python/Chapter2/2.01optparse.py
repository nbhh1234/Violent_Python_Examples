# _*_coding:utf8-

'''
This code we need know what is optparse package
'''
import optparse
# Create option parser
parser = optparse.OptionParser('usage %prog -H' + '<target host> -p <target port>')
# add option in parser
# -H or -P: parameters name in terminal, dest: full parameter name
parser.add_option('-H',dest = 'tgtHost',type='string',help='specify target host')
parser.add_option('-p',dest = 'tgtPort',type='int',help='specify target port')

(options,args) = parser.parse_args()  # get para in option
tgtHost = options.tgtHost
tgtPort = options.tgtPort

if (tgtHost == None) and (tgtPort == None):
    print parser.usage
    exit(0)
else:
    print tgtHost,tgtPort






