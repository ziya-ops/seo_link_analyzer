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


def crawl_page(base_url, current_url, pages):

    normalized_url = normalize_url(current_url)

    # create entry for the new normalized current_url
    if normalized_url not in pages:
        pages[normalized_url] = 0

    # if current url does not belong to the base site, skip it
    if urlparse(base_url).netloc != urlparse(current_url).netloc:
        pages[normalized_url] = None
        return pages
    
    # if we have already checked this normalized url and it is invalid, skip it
    if pages[normalized_url] is None:
        return pages
        
    # if we have already validated this normalized url then increase the count and skip
    if pages[normalized_url] > 0:
        pages[normalized_url] += 1
        return pages
    
    # make a request to current url
    resp = requests.get(current_url)
    try:
        validate_response(resp,current_url)

    # if response invlid, log it and skip
    except Exception as e:
        print(e)
        pages[normalized_url] = None
        return pages

    # increament the count for this url
    pages[normalized_url] +=1

    # get all urls available on base url page and crawl each link found
    url_list = get_urls_from_string(resp.content, base_url)
    for url in url_list:
        
        crawl_page(base_url, url, pages)
    
    return pages

