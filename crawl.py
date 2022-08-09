from lxml import html

def get_urls_from_string(page_content, base_url):
    doc_tree = html.fromstring(page_content, base_url)
    html.make_links_absolute(doc_tree)

    output_list = []
    for elem in doc_tree.iter():
        if elem.tag == "a":
            output_list.append(elem.get("href"))

    return output_list
