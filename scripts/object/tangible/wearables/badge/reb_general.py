import sys

def setup(core, object):
	object.setStringAttribute('condition', '100/100')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('required_faction', 'Rebel')
	return