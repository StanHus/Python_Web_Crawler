from urllib.parse import urlparse


# Get domain name (ex.co.uk)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
    # this is an area for improvement
    except:
        return ''


# Get sub domain name (name.ex.co.uk)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''