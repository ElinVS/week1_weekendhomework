# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop_name):
    return shop_name["name"]

def get_total_cash(sum_of_cash):
    return sum_of_cash["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, number):
    pet_shop["admin"]["total_cash"] += number
    pet_shop["admin"]["total_cash"] + number

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,number):
    pet_shop["admin"]["pets_sold"] += number
    
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop,type_of_breed):    
    list = []
    path_to_breed = pet_shop["pets"]
    for x in path_to_breed:
        if x["breed"] == type_of_breed:
            list.append(x["breed"])
    return list

def find_pet_by_name(pet_shop,pet_name):
    path_to_name = pet_shop["pets"]

    for pet in path_to_name:
        if pet["name"] == pet_name:
            return pet

# pet_name = "Arthur"
# pet_shop = cc_pet_shop

# def remove_pet_by_name(pet_shop,pet_name):
#     path_to_name =  pet_shop["pets"]

#     for pet in path_to_name:
#         if pet["name"] == pet_name:
#             path_to_name.pop(pet["name"])
    
 
def add_pet_to_stock(pet_shop, new_pet):
    new_pet = {"name": "Billy",
                    "pet_type": "dog",
                    "breed": "Dachshund",
                    "price": 2000,}
    path_to_dict = pet_shop["pets"]

    path_to_dict.append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]     


def remove_customer_cash(person,number):
    person["cash"] -= number

def get_customer_pet_count(customer):
    customer["pets"].append(0)
    for x in customer["pets"]:
        if x == 0:
            return x

# def add_pet_to_customer(person,new_pet):







   




    




