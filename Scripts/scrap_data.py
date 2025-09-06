from lxml import html
from pathlib import Path

data = []


p = Path('data')
for pf in p.rglob('*.html'):
     page = ''
     with open(pf, 'r', encoding='utf-8') as f:
          page = f.read()
     
     rating = ''
     sold = ''
     title = ''
     price = ''

     tree = html.fromstring(page)

     try:
          title = tree.xpath('//h2/span')[0].text
     except:
          title = "NILL"
     title = title.replace('  ', '').replace('\n', '').strip()


     try:
          price = tree.xpath('//span[@class="a-price"]/span[@class="a-offscreen"]')[0].text
     except:
          price = "NILL"
     price = price.replace('  ', '').replace('\n', '').strip()

     try:
          rating = tree.xpath('//i[@data-cy="reviews-ratings-slot"]/span')[0].text
     except:
          rating = "NILL"
     rating = rating.replace('  ', '').replace('\n', '').strip()

     try:
          sold = tree.xpath('//div/span[@class="a-size-base a-color-secondary"]')[0].text
     except:
          sold = "NILL"
     sold = sold.replace('  ', '').replace('\n', '').strip()

     dict = {}
     dict['title'] = title
     dict['rating'] = rating
     dict['price'] = price
     dict['sold'] = sold

     data.append(dict)

import json

with open('data.json', 'w', encoding='utf-8') as f:
     f.write(json.dumps(data))

