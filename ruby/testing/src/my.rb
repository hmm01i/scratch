require 'rubygems'
require 'inifile'

def getconfig(conf='my.conf')
  config = IniFile.load(conf)
  puts config['heading1']
  return config
end
def outconfig(config)
  puts 'outputing config'
  return config['head1']['opt1']
end

if ARGV[0]
  conf = ARGV[0]
else
  conf = 'my.conf'
end
config = getconfig(conf)
outconfig(config)
