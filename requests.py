import requests

domain = 'http://www.ford.co.uk/'

def get_web_content(identifier):
    identifier = ''
	url = '{}{}'.format(domain, identifier)
