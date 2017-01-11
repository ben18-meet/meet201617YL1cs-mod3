import time
class Student:
    def __init__(self,name,hometown,age,height,favoriteIceCream):
        name = self.name
        hometown = self.hometown
        age = self.age
        height = self.height
        favoriteIceCream = self.favoriteIceCream
    def print_summary(self):
        print("Name: " + self.name + "Age: " + str(self.age) + "Height: " + str(self.height) + "Hometown:" + self.hometown + " Favorite Ice Cream: " + self.favoriteIceCream)
        

    def get_giraffe_gap(self):
        return(500 - int(self.height))
    def get_days_till_birthday(self):
        
