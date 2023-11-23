# Scrapy is a Python framework for extracting the data you need from websites

# Définition du middleware Un middleware (ou intergiciel en français) est un logiciel qui agit comme une passerelle entre les autres applications,
# outils et bases de données pour offrir aux utilisateurs des services unifiés.

# Commande : scrapy genspider bookspider books.toscrape.com : bookspider is the name of the spider, and the url of the website is after

#Allowed domains : list the domains we want to scrape, it is very important 
#start urls : the url where the spider starts scraping 

#parse function : we put there the pieces of data we want to extract 

#ipython : different shell that is easier to read

#scrapy shell to open the shell
#fetch('urlquel'onveut)
 

#we have to inspect the html of the website to put in the shell the info we want, for example the class, the url, the product...

# In [6]: response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get() : xpath is difficult...

# scrapy crawl bookspider -O bookdata.csv to save the data to a csv or json file or scrapy crawl bookspider -o bookdata.csv to update dataset

#Scrapy items : if there is a syntax error somewhere it might not end in the database if we don't use items in items.py
#1 heure 57 vidéo



