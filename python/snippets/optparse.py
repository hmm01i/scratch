import getpass
import optparse

# def parseCmdArgs():
cmdOpts = optparse.OptionParser(usage = '%prog [options]')
cmdOpts.add_option('-1', dest = 'o1', help = 'IP address of CIMC')
cmdOpts.add_option('-2', dest = 'o2', help = 'Username')
cmdOpts.add_option('-3', dest = 'passwd', help = 'Password (Optional. If not provided you will be prompted.)')
cmdOpts.add_option('-4', action = 'store_true', dest = 'list', help = 'Just query running firmware.')
cmdOpts.add_option('-5', action = 'store_true', dest = 'verbose', help = 'Verbose output')
cmdOpts.add_option('-6', action = 'store_true', dest = 'dry', help = 'Dry run')
(opts, args) = cmdOpts.parse_args()

def getpassword(prompt = "CIMC Password: "):
    return getpass.unix_getpass(prompt)
