from Fruit import Apple, Orange, Banana, Lemon, Grape, Watermelon

my_banana = Banana( "banana","yellow",120, peeled=True)

my_apple = Apple("green apple", "green", 150)

my_orange= Orange("orange", "orange", 200, peeled=True)

my_lemon=Lemon("lemon","yellow",150, 8)

my_grape=Grape("grape",'red', 200, 8)

my_watermelon=Watermelon("арбуз", "зеленый", 1000, 200)

fruits = [my_apple, my_orange, my_banana, my_lemon, my_grape, my_watermelon]

for fruit in fruits:
    print(fruit.bite("worm"))
    print(fruit.bite("bird"))
    print(fruit.bite("caterpillar"))
    

