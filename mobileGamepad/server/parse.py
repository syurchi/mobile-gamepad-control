#class to parse http headers
import re

def httpParse(h):
	headers = str(h)
	header_dict = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", headers))
	return header_dict
