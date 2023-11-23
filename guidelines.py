# First step : pip install scrapy
# Create a project : scrapy startproject pokemons (name of the current project)
# Create a scrapy spider : go into spider folder : pokemons/pokemons/spiders, then type this command to create the spider : scrapy genspider pokemonspider https://scrapeme.live/shop/ (name of the url)
# pip install ipython : different shell that is easier to read, go to scrapy.cfg and add the shell in a separate line
# scrapy shell
# fetch("https://scrapeme.live/shop/") (name of the url to access, practice the code we want into our spider)
# response.css('li[class^="post-"]').get() to get all the pokemon items
# put them in a variable pokemon_items = response.css('li[class^="post-"]').get()
# pokemon.css("h2 ::text").get() => Bulbasaur, the name of the first pokemon of the pokemon items
# pokemon.css("span.woocommerce-Price-amount.amount::text").get() : get the price of the pokemon
# pokemon.css('a').attrib['href'] : get the link of the pokemon page
# go to pokemonspider.py and in parse add pokemon_items
# then create a loop to fetch all the datas for each pokemon of the first page
# exit the scrapy shell
# cd ../ to go back to bookscraper 
# scrapy crawl pokemonspider
# before the loop to fetch all the pokemons on the next pages : scrapy shell and fetch('url')
# response.css('a.next.page-numbers ::attr(href)').get() to get the url for next pages
# response.css('a.woocommerce-LoopProduct-link::attr(href)').get() : get the url for the pokemon page itself
#fetch('https://scrapeme.live/shop/Bulbasaur/') to fetch the pokemon page itself
#search for all the data that we need for the scrapeeee
