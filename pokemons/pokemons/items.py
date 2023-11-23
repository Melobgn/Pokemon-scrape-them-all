# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class PokemonItem(scrapy.Item):
    url = scrapy.Field()
    titre = scrapy.Field()
    prix = scrapy.Field()
    description = scrapy.Field()
    stock = scrapy.Field()
    tags = scrapy.Field()
    categories = scrapy.Field()
    sku = scrapy.Field()
    poids = scrapy.Field()
    longueur = scrapy.Field()
    largeur = scrapy.Field()
    hauteur = scrapy.Field()

