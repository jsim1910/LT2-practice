import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products"]

order_management_db = myclient["order_management"]

chicosproducts_db = myclient["chilechicos_products"]


users = {
    "paul@example.com":{"password":"chua",
                         "first_name":"Paul",
                         "last_name":"Chua"},
    "joben@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joben",
                         "last_name":"Ilagan"},
    "bong@example.com":{"password":"Ch@ng3m3!",
                        "first_name":"Bong",
                        "last_name":"Olpoc"},
    "joaqs@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joaqs",
                         "last_name":"Gonzales"},
}

products = {
    100: {"name":"Beef Tapa","price":110},
    200: {"name":"Pork Sisig","price":100},
    300: {"name":"Tofu Sisg","price":100},
    400: {"name":"Pork Liempo","price":100},
    500: {"name":"El Primo","price":110},
    600: {"name":"Patatas Frita","price":100},
    700: {"name":"El Pollo","price":100},
    800: {"name":"La Carnita","price":100},
}

def get_product(code):
    return products[code]

def get_products():
        product_list = []
        
        for i,v in products.items():
            product = v
            product.setdefault("code", i)
            product_list.append(product)
            
        return product_list

def get_user(username):
    try:
       return users[username]
    except KeyError:
       return None


def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)



    
