class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.color}, {self.weight}"

    def bite(self, eater):
        if eater == "bird":
            amount = 10
        elif eater == "worm":
            amount = 1
        elif eater == "caterpillar":
            amount = 3
        else:
            return "неизвестный едок"

        self.weight = self.weight - amount
        if self.weight >= 0:
            return f"{self.name}, {self.color}, {self.weight}g"
        else:
            return "фрукт кончился"


class Apple(Fruit):
    pass
    
class Orange(Fruit):
    def __init__(self, name, color, weight, peeled=False):
        super().__init__(name, color, weight)
        self.peeled=peeled
        if peeled:
            self.weight=weight*0.9

class Banana(Fruit):
    def __init__(self, name, color, weight, peeled=False):
        super().__init__(name, color, weight)
        self.peeled = peeled
        if peeled:
            self.weight = weight*0.8
     
class Lemon(Fruit):
    def __init__(self, name, color, weight, sourness):
        super().__init__(name, color, weight)
        self.sourness = sourness

    def bite(self, eater):
        if eater == "bird" and self.sourness <= 7:
            amount = 10
        elif eater == "bird" and self.sourness > 7:
            amount = 0
            print('Птица улетела')
        elif eater == "worm":
            amount = 1
        elif eater == "caterpillar":
            amount = 3
        else:
            return 'Неизвестный едок'

        self.weight = self.weight - amount
        if self.weight >= 0:
            return f"{self.name}, {self.color}, {self.weight}g"
        else:
            return "фрукт закончился"
    
      
      
class Grape(Fruit):
       def __init__(self, name, color, weight, cluster_size):
           super().__init__(name, color, weight)
           self.cluster_size = cluster_size
       def bite(self, eater):
           if self.cluster_size <=0 or self.weight <=0:
               return "виноград заkончился"
           berry_weight=self.weight / self.cluster_size
           self.weight = self.weight - berry_weight
           self.cluster_size = self.cluster_size -1
           return f"{self.name}, {self.color}, {self.weight}g, ягод осталось {self.cluster_size}"
           
       
       

class Watermelon(Fruit):
    def __init__(self, name, color, weight, seeds_count):
        super().__init__(name, color, weight)
        self.seeds_count = seeds_count
    def bite(self, eater):
         result =super().bite(eater)
         if self.seeds_count >0:
             self.seeds_count = self.seeds_count -1
         return f"{result},{self.seeds_count} косточек осталось"
          
          #"seeds_count количество косточек"
class Pineapple(Fruit):
     def __init__(self, name, color, weight, spikiness):
         super().__init__(name, color, weight)
         self.spikiness=spikiness   #spikiness колючесть червяк или гусеница едят плсле птицы
     
  

