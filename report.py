def remove_none_values(dict):
    # out_dict = {}
    # for key in dict:
    #     if dict[key] != None:
    #         out_dict[key] = dict[key]

    # return out_dict

    keys_to_delete = []
    for key, val in dict.items():
        if val is None:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del dict[key]
    
    return dict

def return_value(tup):
    return tup[1]

def sort_pages(dict):
    sorted_list = []
    for key,val in dict.items():
        sorted_list.append((key,val))

    sorted_list.sort(reverse=True, key=return_value)
    return sorted_list

def print_report(pages):
    pages_without_none = remove_none_values(pages)
    pages_sorted_list = sort_pages(pages_without_none)

    for link_count in pages_sorted_list:
        print(f"Found {link_count[1]} internal links to {link_count[0]}")



