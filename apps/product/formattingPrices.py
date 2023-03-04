from price_parser import  Price,  parse_price

price = "\u20ac 0,99 * (zzgl. \u20ac 0,25 Pfand)"

euro_price = Price.fromstring(price)
print(euro_price.amount_float)


# for n in price:
#     if n != 