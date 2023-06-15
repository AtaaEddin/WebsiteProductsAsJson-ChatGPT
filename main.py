import sys
from WebsiteProductsAsJson import get_products

# TODO use some quick web server library instead

def main(prompt):
    print(get_products(prompt))

if __name__ == "__main__":
    prompt = sys.argv[1]
    main(prompt)
