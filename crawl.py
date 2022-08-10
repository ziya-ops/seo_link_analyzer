from lxml import html
from urllib.parse import urlparse
import requests

def get_urls_from_string(page_content, base_url):
    doc_tree = html.fromstring(page_content)
    doc_tree.make_links_absolute(base_url=base_url)

    output_urls_list = []
    for elem in doc_tree.iter():
        if elem.tag == "a":
            output_urls_list.append(elem.get("href"))

    return output_urls_list

def normalize_url(url):
    parsed_url_obj = urlparse(url)
    normalized_url = parsed_url_obj.netloc + parsed_url_obj.path
    normalized_url = normalized_url.lower()
    normalized_url = normalized_url.rstrip('/')
    return normalized_url

def crawl_page(base_url, pages):
    resp  = requests.get(base_url)
    url_list = get_urls_from_string(resp.content, base_url)
    for url in url_list:
        pages[url] = 1
    
    return pages

