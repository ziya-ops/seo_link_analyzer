
import sys

def main():

    if len(sys.argv) != 2:
        print("No url provided")
        exit(1)
    
    base_url = sys.argv[1] 
    print(base_url)

if __name__ == "__main__":
    main()