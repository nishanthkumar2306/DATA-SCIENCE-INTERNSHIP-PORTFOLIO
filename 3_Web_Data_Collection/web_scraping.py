import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "http://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Lists to store data
quotes_list = []
authors_list = []
tags_list = []

# Find all quote blocks
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]
    
    quotes_list.append(text)
    authors_list.append(author)
    tags_list.append(", ".join(tags))

# Create DataFrame
df = pd.DataFrame({
    "Quote": quotes_list,
    "Author": authors_list,
    "Tags": tags_list
})

# Save to CSV
df.to_csv("quotes.csv", index=False)

print("Data scraped successfully and saved to quotes.csv")
