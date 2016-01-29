import requests

domain = 'http://www.ford.co.uk/'

def get_web_content(identifier):
    identifier = ''
    url = '{}{}'.format(domain, identifier)
    
    response = requests.get(url)
    print response.status_code
    print len(response.text) # or response.content

