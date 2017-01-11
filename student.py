class Student:
    def __init__(self,name,hometown,age,height,favoriteIceCream):
        name = self.name
        hometown = self.hometown
        age = self.age
        height = self.height
        favoriteIceCream = self.favoriteIceCream
    def print_summary(self):
        print("This is " + self.name + ". " self.name + "is " + self.age + "years old. " + self.name + " is from " + self.hometown + ". " self.name + "'s height is " + self.height + ". " + self.name + "'s favorite Ice Cream is " + self.favoriteIceCream

    def get_giraffe_gap(self):
        return(500 - int(self.height))          
