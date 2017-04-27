require 'my'

describe 'configs' do
let(:config) { {'head1'=>{'opt1'=>'1','opt2'=>'2'}}}
  it 'outputs opt1 value' do
    getconfig
    outconfig(config)
  end
end
