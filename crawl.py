from lxml import html
from urllib.parse import urlparse
import requests

# get_urls_from_string parses the web page content and
# returns all the urls available on the page in the form of a list
def get_urls_from_string(page_content, base_url):
    doc_tree = html.fromstring(page_content)
    doc_tree.make_links_absolute(base_url=base_url)

    output_urls_list = []
    for elem in doc_tree.iter():
        if elem.tag == "a":
            output_urls_list.append(elem.get("href"))

    return output_urls_list

# normalize_url returs the base path of a url
# its used to avoid dupllicate urls
def normalize_url(url):
    parsed_url_obj = urlparse(url)
    normalized_url = parsed_url_obj.netloc + parsed_url_obj.path
    normalized_url = normalized_url.lower()
    normalized_url = normalized_url.rstrip('/')
    return normalized_url

def validate_response(resp, url):
    if resp.status_code != 200:
        raise Exception(f"{url} didn't result in Status code 200, got {resp.status_code}")

    if "text/html" not in resp.headers["content-type"].lower():
        raise Exception(f"{url} didn't result in HTML response")


def crawl_page(base_url, pages):
    
    resp = requests.get(base_url)
    try:
        validate_response(resp,base_url)

    except Exception as e:
        print(e)

    return pages


    url_list = get_urls_from_string(resp.content, base_url)
    for url in url_list:
        pages[url] = 1
    
    return pages

