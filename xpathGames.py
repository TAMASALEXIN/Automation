from lxml import etree

# Load the XML file
tree = etree.parse("ex11.xml")

# Retrieve the titles of all games
game_titles = tree.xpath('//game/title/text()')

# Select the developer of the game with the highest price
highest_price_game_developer = tree.xpath('//game[not(price < ../game/price)]/developer/text()')[0]

# Get the average price of games
game_prices = tree.xpath('//game/price/text()')
average_price_games = sum(float(price) for price in game_prices) / len(game_prices)

# Select the titles of games in the "First-Person Shooter" genre
fps_game_titles = tree.xpath('//game[genre="First-Person Shooter"]/title/text()')

# Retrieve the title and price of the cheapest game
cheapest_game = tree.xpath('//game[not(price > ../game/price)]')
cheapest_game_title = cheapest_game[0].find('title').text
cheapest_game_price = cheapest_game[0].find('price').text

# Select the names of developers for games priced between 20.00 and 30.00
developers_in_price_range = tree.xpath('//game[price>20 and price<30]/developer/text()')

# Get the total number of games in the game store
total_games = len(tree.xpath('//game'))

# Retrieve the genre of the game with the lowest price
lowest_price_game_genre = tree.xpath('//game[not(price > ../game/price)]/genre/text()')[0]

# Select the title of the game with the longest title
longest_title_game = max(tree.xpath('//game/title/text()'), key=len)

# Get the distinct genres available in the game store
distinct_genres = set(tree.xpath('//game/genre/text()'))