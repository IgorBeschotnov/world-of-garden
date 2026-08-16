class Eaters:
    def __init__(self, name, bite_size):
        self.name=name
        self.bite_size= bite_size
        
class Bird(Eater):
        def __init__(self):
            super().__init__( "bird", 10 )
 
class Worm(Eater):
        def __init__(self):
            super().__init__("worm", 1)
 
class Caterpillar(Eater):
        def __init__(self):
            super().__init__("caterpillar", 3)