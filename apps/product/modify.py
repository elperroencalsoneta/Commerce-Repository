import json
from price_parser import  Price,  parse_price

data = [
    {
        "model": "product.product",
        "pk": 0,
        "fields": {
            "name": "Leffe\u00ae Blonde 0,33 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020026",
            "description": "This is a product",
            "price": "\u20ac 0,99 * (zzgl. \u20ac 0,25 Pfand)",    
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 1,
        "fields": {
            "name": "Internationales Premium-Bier 0,33 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020033",
            "description": "This is a product",
            "price": "\u20ac 0,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 2,
        "fields": {
            "name": "LORENZ\u00ae Pommels oder Monster Munch 75 g",            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020132",
            "description": "This is a product",
            "price": "\u20ac 0,79 * (zzgl. \u20ac 0,25 Pfand)",    
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 3,
        "fields": {
            "name": "LORENZ\u00ae Snack-Hits 320 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020141",
            "description": "This is a product",
            "price": "\u20ac 0,79",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 4,
        "fields": {
            "name": "LORENZ\u00ae Crunchips 110 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020134",
            "description": "This is a product",
            "price": "\u20ac 1,11 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 5,
        "fields": {
            "name": "Stella Artois 0,33 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020109",
            "description": "This is a product",
            "price": "\u20ac 1,11",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 6,
        "fields": {
            "name": "Freundschaftsspiel QbA Rotweincuv\u00e9e 0,75 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020111",
            "description": "This is a product",
            "price": "\u20ac 2,22 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 7,
        "fields": {
            "name": "HEINEKEN\u00ae Bier 5 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020110",
            "description": "This is a product",
            "price": "\u20ac 2,22",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 8,
        "fields": {
            "name": "LORENZ\u00ae NicNac\u2019s Volles Rohr 333 g",            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020121",
            "description": "This is a product",
            "price": "\u20ac 1,19 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 9,
        "fields": {
            "name": "LORENZ\u00ae Brezel oder Party Cracker 200 g",            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020140",
            "description": "This is a product",
            "price": "\u20ac 1,19",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 10,
        "fields": {
            "name": "LORENZ\u00ae Snackspezialit\u00e4t 180 g",    
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020138",
            "description": "This is a product",
            "price": "\u20ac 0,99 * (zzgl. \u20ac 0,25 Pfand)",    
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 11,
        "fields": {
            "name": "LORENZ\u00ae Saltletts Cocktail Mix 750 g",   
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020030",
            "description": "This is a product",
            "price": "\u20ac 0,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 12,
        "fields": {
            "name": "GUT BIO Bio-Hackfleisch vom Rind 800 g",      
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020100",
            "description": "This is a product",
            "price": "\u20ac 4,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 13,
        "fields": {
            "name": "MEINE METZGEREI H\u00e4hnchen-Oberschenkel 2 kg",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020101",
            "description": "This is a product",
            "price": "\u20ac 4,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 14,
        "fields": {
            "name": "GOURMET FINEST CUISINE Neuseel\u00e4ndisches Lammkarree",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020102",
            "description": "This is a product",
            "price": "\u20ac 11,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 15,
        "fields": {
            "name": "GUT BIO Bio Forellen 500 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020103",
            "description": "This is a product",
            "price": "\u20ac 11,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 16,
        "fields": {
            "name": "CUCINA NOBILE Original Italienische Salsiccia 400 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020098",
            "description": "This is a product",
            "price": "\u20ac 3,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 17,
        "fields": {
            "name": "BERENTZEN Winter-Edition 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020020",
            "description": "This is a product",
            "price": "\u20ac 3,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 18,
        "fields": {
            "name": "ALMDUDLER Almspritz 0,75 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020115",
            "description": "This is a product",
            "price": "\u20ac 1,19 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 19,
        "fields": {
            "name": "CINZANO\u00ae Asti DOCG 0,75 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020002",
            "description": "This is a product",
            "price": "\u20ac 1,19",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 20,
        "fields": {
            "name": "JAMESON Irish Whiskey 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020021",
            "description": "This is a product",
            "price": "\u20ac 1,19 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 21,
        "fields": {
            "name": "Winterlik\u00f6r 0,5 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020004",
            "description": "This is a product",
            "price": "\u20ac 1,19",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 22,
        "fields": {
            "name": "BASTEI Eierlik\u00f6r mit Schuss 0,7 l",      
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020000",
            "description": "This is a product",
            "price": "\u20ac 3,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 23,
        "fields": {
            "name": "MUMM DRY Jahrgangssekt 0,75 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020797",
            "description": "This is a product",
            "price": "\u20ac 3,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 24,
        "fields": {
            "name": "BECK\u2019S Unfiltered 0,44 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020113",
            "description": "This is a product",
            "price": "\u20ac 6,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 25,
        "fields": {
            "name": "Talisker 10 Jahre 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020128",
            "description": "This is a product",
            "price": "\u20ac 6,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 26,
        "fields": {
            "name": "WINTERTRAUM Lebkuchen-Bausatz 1.035 g",       
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211040002",
            "description": "This is a product",
            "price": "\u20ac 6,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 27,
        "fields": {
            "name": "WINTERTRAUM Lebkuchen-Bausatz 900 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211040003",
            "description": "This is a product",
            "price": "\u20ac 6,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 28,
        "fields": {
            "name": "Tanqueray Flor des Sevilla 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020122",
            "description": "This is a product",
            "price": "\u20ac 5,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 29,
        "fields": {
            "name": "Tanqueray No. Ten 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020124",
            "description": "This is a product",
            "price": "\u20ac 5,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 30,
        "fields": {
            "name": "ASBACH\u00ae Coffee + Cream 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020120",
            "description": "This is a product",
            "price": "\u20ac 7,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 31,
        "fields": {
            "name": "Johnnie Walker Black Label 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020126",
            "description": "This is a product",
            "price": "\u20ac 7,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 32,
        "fields": {
            "name": "Baileys\u2122 Chocolat Luxe 0,5 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020127",
            "description": "This is a product",
            "price": "\u20ac 2,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 33,
        "fields": {
            "name": "Dimple Golden Selection 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020125",
            "description": "This is a product",
            "price": "\u20ac 2,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 34,
        "fields": {
            "name": "The Singleton 12 Jahre 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020129",
            "description": "This is a product",
            "price": "\u20ac 6,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 35,
        "fields": {
            "name": "Pampero Aniversario Rum 0,7 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020131",
            "description": "This is a product",
            "price": "\u20ac 6,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 36,
        "fields": {
            "name": "RON ALEGR\u00d3 Dominikanischer Rum 0,7 l",   
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020793",
            "description": "This is a product",
            "price": "\u20ac 2,49 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 37,
        "fields": {
            "name": "GARDEN GOURMET\u00ae vegane Falafel 190 g",   
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020146",
            "description": "This is a product",
            "price": "\u20ac 2,49",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 38,
        "fields": {
            "name": "MCCAIN Chef Frites 750 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020016",
            "description": "This is a product",
            "price": "\u20ac 4,69 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 39,
        "fields": {
            "name": "M\u00dcLLER\u00ae Reine Buttermilch 500 g",   
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020014",
            "description": "This is a product",
            "price": "\u20ac 4,69",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 40,
        "fields": {
            "name": "BERTOLLI Oliven\u00f6l oder Natives Oliven\u00f6l Extra 500 ml",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020005",
            "description": "This is a product",
            "price": "\u20ac 14,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 41,
        "fields": {
            "name": "ZIMBO Zwiebelmett 120 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020008",
            "description": "This is a product",
            "price": "\u20ac 14,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 42,
        "fields": {
            "name": "MEGGLE Feine Butter 250 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202210040529",
            "description": "This is a product",
            "price": "\u20ac 4,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 43,
        "fields": {
            "name": "LANDLIEBE Reibek\u00e4se 150 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020037",
            "description": "This is a product",
            "price": "\u20ac 4,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 44,
        "fields": {
            "name": "Miracel Whip 500 ml",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020143",
            "description": "This is a product",
            "price": "\u20ac 4,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 45,
        "fields": {
            "name": "ARCTICFISH \u201ePures Gr\u00fcn\u201c \u2013 R\u00e4ucherlachs 100 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020031",
            "description": "This is a product",
            "price": "\u20ac 4,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 46,
        "fields": {
            "name": "TILLMAN\u2019S\u00ae Toasty 280 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020119",
            "description": "This is a product",
            "price": "\u20ac 3,79 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 47,
        "fields": {
            "name": "M\u00dcLLER\u2019S M\u00dcHLE Tellerlinsen 500 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020118",
            "description": "This is a product",
            "price": "\u20ac 3,79",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 48,
        "fields": {
            "name": "GOURMET FINEST CUISINE Strau\u00dfensteaks 300 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020114",
            "description": "This is a product",
            "price": "\u20ac 0,79 * (zzgl. \u20ac 0,25 Pfand)",    
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 49,
        "fields": {
            "name": "CUCINA NOBILE Gnocchi 390 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020029",
            "description": "This is a product",
            "price": "\u20ac 0,79",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 50,
        "fields": {
            "name": "GOURMET FINEST CUISINE Krustenbraten 120 g",  
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020116",
            "description": "This is a product",
            "price": "\u20ac 28,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 51,
        "fields": {
            "name": "WEIHENSTEPHAN Mascarpone-Joghurt 150 g",      
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020024",
            "description": "This is a product",
            "price": "\u20ac 28,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 52,
        "fields": {
            "name": "WEIHENSTEPHAN Fruchtquark 500 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202205310305",
            "description": "This is a product",
            "price": "\u20ac 4,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 53,
        "fields": {
            "name": "ASIA GREEN GARDEN Udong-Nudel-Bowl 252 g",    
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020152",
            "description": "This is a product",
            "price": "\u20ac 4,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 54,
        "fields": {
            "name": "ASIA GREEN GARDEN Udong-Nudel-Bowl 249 g",    
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020142",
            "description": "This is a product",
            "price": "\u20ac 4,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 55,
        "fields": {
            "name": "MESSMER L\u00e4ndertee 40 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020147",
            "description": "This is a product",
            "price": "\u20ac 4,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 56,
        "fields": {
            "name": "OLD AMSTERDAM Scheibenk\u00e4se 125 g",       
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020148",
            "description": "This is a product",
            "price": "\u20ac 14,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 57,
        "fields": {
            "name": "OLD AMSTERDAM Scheibenk\u00e4se 145 g",       
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020149",
            "description": "This is a product",
            "price": "\u20ac 14,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 58,
        "fields": {
            "name": "MESSMER L\u00e4ndertee 50 g",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211020155",
            "description": "This is a product",
            "price": "\u20ac 22,99 *",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    },
    {
        "model": "product.product",
        "pk": 59,
        "fields": {
            "name": "Bio-Apfeldirektsaft 0,75 l",
            "photo": "https://s7g10.scene7.com/is/image/aldi/202211030108",
            "description": "This is a product",
            "price": "\u20ac 22,99",
            "compare_price": 0.01,
            "category": 1,
            "quantity": 2,
            "sold": 33,
            "date_created": "2022-11-19T18:42:32Z"
        }
    }
]

counter = 1

for n in data:
    n["pk"] += counter
    # n["fields"]["price"] = n["fields"]["price"].replace("\u20ac ", "")
    n["fields"]["price"] = Price.fromstring(n["fields"]["price"]).amount_text
    n["fields"]["compare_price"] = Price.fromstring(n["fields"]["price"]).amount_text
    n["fields"]["price"] = float(n["fields"]["price"].replace(',', '.'))
    n["fields"]["compare_price"] = float(n["fields"]["compare_price"].replace(',', '.'))
    n["fields"]["category"] = 1

AldiSudOffers = json.dumps(data, indent = 4)


print(AldiSudOffers)



# price = "\u20ac 0,99 * (zzgl. \u20ac 0,25 Pfand)"

# euro_price = Price.fromstring(price)
# print(euro_price.amount_text)
