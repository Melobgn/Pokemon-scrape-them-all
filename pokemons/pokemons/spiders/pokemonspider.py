import scrapy
import re
from pokemons.items import PokemonItem

class PokemonspiderSpider(scrapy.Spider):
    name = "pokemonspider"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop/"]

    custom_settings = {
        'FEEDS' : {
    'pokemons.json' : {'format' : 'json', 'overwrite' : True},
    'pokemons.csv' : {'format' : 'csv', 'overwrite' : True}
        }
    }

    def parse(self, response):
        pokemon_items = response.css('li[class^="post-"]')

        for pokemon in pokemon_items:
            pokemon_url = pokemon.css('a.woocommerce-LoopProduct-link::attr(href)').get()
            yield response.follow(pokemon_url, callback=self.parse_pokemon_page)

        next_page_url = response.css('a.page-numbers.next::attr(href)').get()
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)

        
    def parse_pokemon_page(self, response):
        table_rows = response.css("table tr")
        pokemon_item = PokemonItem()

        # Appliquer une expression régulière pour extraire les dimensions
        dimension_text = response.css('.product_dimensions ::text').get()
        dimensions_match = re.match(r'(\d+)\s*x\s*(\d+)\s*x\s*(\d+)\s*cm', dimension_text) if dimension_text else None


        if dimensions_match:
            longueur, largeur, hauteur = dimensions_match.group(1), dimensions_match.group(2), dimensions_match.group(3)
        else:
            longueur = largeur = hauteur = None

    
        pokemon_item['url'] = response.url
        pokemon_item['titre'] = response.css('h1 ::text').get()
        pokemon_item['prix'] = response.css('p.price span.woocommerce-Price-amount::text').get()
        pokemon_item['description'] = response.css('div.woocommerce-product-details__short-description p::text').get()
        pokemon_item['stock'] = response.css('p.stock.in-stock ::text').get()
        pokemon_item['tags'] = response.css('.tagged_as  a::text').getall()
        pokemon_item['categories'] = response.css('.posted_in  a::text').getall()
        pokemon_item['sku'] = response.css('span.sku ::text').get()
        pokemon_item['poids'] = table_rows[0].css('td ::text').get()
        pokemon_item['longueur'] = longueur.strip() if longueur else None
        pokemon_item['largeur'] = largeur.strip() if largeur else None
        pokemon_item['hauteur'] = hauteur.strip() if hauteur else None
    
        yield pokemon_item




