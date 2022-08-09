from lxml import html

def get_urls_from_string(page_content, base_url):
    doc_tree = html.fromstring(page_content)
    doc_tree.make_links_absolute(base_url=base_url)

    output_urls_list = []
    for elem in doc_tree.iter():
        if elem.tag == "a":
            output_urls_list.append(elem.get("href"))

    return output_urls_list
