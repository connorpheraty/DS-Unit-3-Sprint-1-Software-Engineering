#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in list(range(num_products)):

        samp_adj = sample(ADJECTIVES, k=1)
        samp_noun = sample(NOUNS, k=1)

        product = Product(name= (str(samp_adj) + ' ' + str(samp_noun)), price = randint(5, 100),
                          weight = randint(5, 100), flammability=uniform(.5, 2.5))
        products.append(product)
    return products

def inventory_report(products):

    #-------Unique List ---------#

    # Function to identify unique values in a list
    def unique(list1): 
  
        # intilize a null list 
        unique_list = [] 
      
        # traverse for all elements 
        for x in list1: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
        # print list 
        return unique_list
    
    # Applying function to list of product objects
    product_list = []

    for product in products:
        product_list.append(product.name)
    
    num_unique = len(unique(product_list))

    #---------Average Price-----------#

    price_lst = []
    for product in products:
        price_lst.append(product.price)
    average_price = sum(price_lst) / len(price_lst)
    
    #---------Average Weight----------#

    weight_lst = []
    for weight in products:
        weight_lst.append(product.weight)
    average_weight = sum(weight_lst) / len(weight_lst)
    
    #------Average Flammability-------#
    flam_lst = []
    for flam in products:
        flam_lst.append(flam.flammability)
    average_flam = sum(flam_lst) / len(flam_lst)
    
    #------------Report---------------#
    print('ACME CORPORATION OFFICIAL INVECNTORY REPORT')
    print("Unique Product Names: ", num_unique)
    print("Average Price: ", average_price)
    print('Average Weight: ', average_weight)
    print("Average Flammability ", average_flam)
    

if __name__ == '__main__':
    inventory_report(generate_products())