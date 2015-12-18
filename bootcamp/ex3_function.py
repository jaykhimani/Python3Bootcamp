__author__ = 'jay'


def cheapest_paperback(mybooks):
    lowest_price = -1
    lowest_price_book = None
    for book, value in mybooks.items():
        paperback = value['formats']['paperback']
        consumer_price = paperback['price'] + paperback['shipping']
        if lowest_price == -1:
            lowest_price = consumer_price
            lowest_price_book = book
        if consumer_price < lowest_price:
            lowest_price = consumer_price
            lowest_price_book = book
    return {"book": lowest_price_book, "consumer_price": consumer_price}


books = {'The Hitchhikers Guide to the Galaxy':
             {'author': 'Douglas Adams',
              'formats': {'ebook': {'price': 12.30,
                                    'shipping': 0.00},
                          'hardcopy': {'price': 20.00,
                                       'shipping': 2.50},
                          'paperback': {'price': 15.75,
                                        'shipping': 1.50}}},
         '211 The Hitchhikers Guide to the Galaxy':
             {'author': '211 Douglas Adams',
              'formats': {'ebook': {'price': 12.30,
                                    'shipping': 0.00},
                          'hardcopy': {'price': 20.00,
                                       'shipping': 2.50},
                          'paperback': {'price': 15.74,
                                        'shipping': 0.50}}},
         'The Three Musketeers': {'author': 'Alexandre Dumas',
                                  'formats': {'ebook': {'price': 19.90,
                                                        'shipping': 0.00},
                                              'hardcopy': {'price': 38.00,
                                                           'shipping': 3.00},
                                              'paperback': {'price': 24.10,
                                                            'shipping':
                                                                2.00}}},
         '12 The Three Musketeers': {'author': '12 Alexandre Dumas',
                                     'formats':
                                         {'ebook': {'price': 19.90,
                                                    'shipping': 0.00},
                                          'hardcopy': {'price': 38.00,
                                                       'shipping': 3.00},
                                          'paperback': {'price': 24.10,
                                                        'shipping': 2.00}}}}

result = cheapest_paperback(books)
print("%s is the cheapest book priced at %f" %
      (result['book'], result['consumer_price']))
