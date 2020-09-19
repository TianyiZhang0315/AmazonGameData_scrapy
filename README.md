# AmazonGameData_scrapy
This is a practice project of scrapy on Python. Data are crawled from Amazon.com with user agents.
# Project Structure

|-ps4_game/ <br/>
&emsp;|-spiders/ <br/>
&emsp;&emsp;|-__init__.py <br/>
&emsp;&emsp;|-game_spider.py <br/>
&emsp;|-__init__.py <br/>
&emsp;|-items.py <br/>
&emsp;|-middlewares.py <br/>
&emsp;|-pipelines.py <br/>
&emsp;|-settings.py <br/>
    
# Data Features and Storage
Each product is described by six features for further analyze: name, price, star, n_sale, year and platform. "Platform" field is used to make
sure than the data only contains products from PS4 platform. All features missing from Amazon.com contains a string placeholder "Not Available".
Each entry of product is stored in local Mongodb as a document under the collection named "PS4_Games" inside "AmazonSpider" database.
# Running the Spider
 ```
  $ cd ps4_game
  $ scrapy crawl game_spider
```
