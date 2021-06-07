class AppleTree:
    def __init__(self, height, age):
        self.height = height
        self.age    = age
    
    def height_tree(self):
        return self.height
        
    def age_tree(self):
        self.age += 1
        return self.age
   
    def is_dead(self):
        if self.age == 100:
            return True
        else:
            return False
    
    def any_apples(self):
        pass

    def pick_an_apple(self):
        raise Exception('No apples on your tree')
        # Read the tests before coding.
