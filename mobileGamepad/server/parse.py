import re

#parse http headers and put keys and values into a dictionary
def httpParse(h):
	headers = str(h)
	header_dict = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", headers))
	return header_dict
