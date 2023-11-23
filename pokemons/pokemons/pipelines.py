# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PokemonsPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        print(adapter)

        # Tags and categories types => switch to lowercase
        lowercase_keys = ['categories', 'tags']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            if isinstance(value, str):  # Check if the value is a string
                adapter[lowercase_key] = value.lower()
            elif isinstance(value, list):  # Check if the value is a list
                # Assuming you want to lowercase each element in the list
                adapter[lowercase_key] = [element.lower() for element in value]
            elif value is not None:
                # Handle other types as needed
                adapter[lowercase_key] = str(value).lower()



        #Price => convert to float
        price_keys = ['prix']
        for price_key in price_keys:
            value_price = adapter.get(price_key)
            adapter[price_key] = float(value_price)

        poids_key = 'poids'
        value_poids = adapter.get(poids_key)
        if value_poids is not None:
        # Remove 'kg' from the value and convert to float
            numeric_value = float(value_poids.replace('kg', '').strip())
            adapter[poids_key] = numeric_value

        # Stock => extract number of pokemon in stock
        stock_key = 'stock'
        value_stock = adapter.get(stock_key)
        if value_stock is not None:
            numeric_value_stock = int(value_stock.replace('in stock', '').strip())
            adapter[stock_key] = numeric_value_stock

        #Put the string values in int values
        int_keys = ['stock', 'sku', 'longueur', 'largeur', 'hauteur']
        for int_key in int_keys:
            value_string = adapter.get(int_key)
            if value_string is not None:
                if isinstance(value_string, list):
                    # Handle the case where the value is a list
                    adapter[int_key] = [int(element) for element in value_string]
                else:
                    # Convert the value to int for non-list cases
                    adapter[int_key] = int(value_string)

        # sku_string = adapter.get('sku')
        # adapter['sku'] = int(sku_string)

        # longueur_string = adapter.get('longueur')
        # adapter['longueur'] = int(longueur_string)



    
        # #Strip all whitespaces from strings
        # field_names = adapter.field_names()
        # for field_name in field_names:
        #     if field_name != 'description':
        #         value = adapter.get(field_name)
        #         adapter[field_name] = value.strip()

        return item

import sqlite3

class SaveToSqlitePipeline:

    def __init__(self):
        # Utilize self to make con an instance variable
        self.con = sqlite3.connect("pokemons.db")
        self.cur = self.con.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS pokemons(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            titre TEXT,
            prix DECIMAL,
            description TEXT,
            stock INTEGER,
            tags TEXT,
            categories TEXT,
            sku INTEGER,
            poids DECIMAL,
            longueur INTEGER,
            largeur INTEGER,
            hauteur INTEGER
        )
        """)

    def process_item(self, item, spider):
        item["titre"] = str(item["titre"])
        item["description"] = str(item["description"])
        item["tags"] = str(item["tags"])
        item["categories"] = str(item["categories"])
        # Define insert statement
        self.cur.execute("""
        INSERT INTO pokemons (
            url,
            titre,
            prix,
            description,
            stock,
            tags,
            categories,
            sku,
            poids,
            longueur,
            largeur,
            hauteur
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            item["url"],
            item["titre"],
            item["prix"],
            item["description"],
            item["stock"],
            item["tags"],
            item["categories"],
            item["sku"],
            item["poids"],
            item["longueur"],
            item["largeur"],
            item["hauteur"],
        ))

        # Execute insert of data into the database
        self.con.commit()
        return item

    def close_spider(self, spider):
        # Close cursor & connection to the database
        self.cur.close()
        self.con.close()
