import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://www.safeway.com/shop/search-results.html?q=peppermint"  # Replace with the actual URL of the Safeway page
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all product items
products = soup.find_all("product-item-al-v1", {"data-qa": "prd-itm"})

# Extract product name and price
product_data = []
for product in products:
    # Get the product name
    name_tag = product.find("a", {"data-qa": "prd-itm-pttl"})
    name = name_tag.text.strip() if name_tag else "No name"

    # Get the product price
    price_tag = product.find("span", {"data-qa": "prd-itm-prc"})
    price = price_tag.text.strip() if price_tag else "No price"

    # Store the data
    product_data.append({"name": name, "price": price})

# Print the extracted product data
for item in product_data:
    print(f"Product Name: {item['name']}, Price: {item['price']}")
