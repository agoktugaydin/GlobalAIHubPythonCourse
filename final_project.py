import random as rnd

class Recipe():
    def __init__(self,products,times):
        self.products = products
        self.times_of_product_types = times
    def cook(self):
        cooking_time = 0
        for p in self.products:
            current_product_time = self.times_of_product_types[p]
            print("It takes", current_product_time, "minutes to add ",p)
            cooking_time += current_product_time
        print("It is ready, you can enjoy your meal. It took about",cooking_time,"minutes to prepare")
class RecipeOne(Recipe): # Recipe'den miras alır
    def __init__(self,products,times):
        super().__init__(products,times)

class RecipeTwo(Recipe): # Recipe'den miras alır
    def __init__(self,products,times):
        super().__init__(products,times)

class RecipeThree(Recipe): # Recipe'den miras alır
    def __init__(self,products,times):
        super().__init__(products,times)

def generaterndTimesDictionary():
    all_products = ["Sugar", "Flour", "Salt", "Oil", "Sauce", "Yeast"]
    times_of_product_types = {}
    for p in all_products:
        times_of_product_types[p] = rnd.randrange(0,15,1) # rnd time generation for all products
    return times_of_product_types

def generaterndProductList():
    result = []
    all_products = ["Sugar", "Flour", "Salt", "Oil", "Sauce", "Yeast"]
    num = rnd.randrange(0,len(all_products),1) # this is for how many product
    for i in range(num):
        which = rnd.randrange(0,len(all_products),1)  # this is for which product
        result.append(all_products[which])
    return result

recipe = RecipeOne(generaterndProductList(), generaterndTimesDictionary())
recipe.cook()

