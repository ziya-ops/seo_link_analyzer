
import sys
from crawl import crawl_page
from report import print_report

def main():

    if len(sys.argv) != 2:
        print("No url provided")
        exit(1)
    
    base_url = sys.argv[1] 
    #print(base_url)

    url_count_dict = {}
    url_count_dict = crawl_page(base_url, base_url, url_count_dict)
    print_report(url_count_dict)

if __name__ == "__main__":
    main()