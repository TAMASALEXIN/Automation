from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
# print(tbody)

trs = tbody.contents

# print(trs[0].prettify())
# print(trs[0].next_sibling.prettify())
# print(trs[1].previous_sibling)
# print(list(trs[0].next_siblings))



# print(trs[0].parent)
# print(trs[0].parent.name)
# print(list(trs[0].descendants))
# print(list(trs[0].contents))
# print(list(trs[0].children))  # check for yourself


prices = {}
for tr in trs[:10]:
	name, price = tr.contents[2:4]
	print(name)
	print(name.p.string)
	

	fixed_name = name.p.string

	print(price.a.string)
	print(price.span.string)
	fixed_price = price.span.string

	prices[fixed_name] = fixed_price

print(prices)

gains = {}
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.span.string

    weekly_gain = tr.contents[6].span.text   

    gains[fixed_name] = weekly_gain
     

print(gains)