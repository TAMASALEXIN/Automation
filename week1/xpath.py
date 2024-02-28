from lxml import etree

# Load the XML file
tree = etree.parse("ex4.html")

# Get the title of book 3
title_book_3 = tree.xpath('//book[3]/title/text()')[0]

# Get text from all author's names
authors = tree.xpath('//author/text()')

# Calculate the total amount of money to buy two of each book
prices = tree.xpath('//price/text()')
total_amount = sum([2 * float(price) for price in prices])

print(f'Title of book 3: {title_book_3}')
print(f'Authors: {authors}')
print(f'Total amount for two of each book: {total_amount}')