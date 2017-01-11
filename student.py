class Student:
    def __init__(self,name,hometown,age,height,favoriteIceCream):
        self.name = name
        self.hometown = hometown
        self.age = age
        self.height = height
        self.favoriteIceCream = favoriteIceCream
    def print_summary(self):
        print("Name: " + self.name + "Age: " + str(self.age) + "Height: "
              + str(self.height) + "Hometown:" + self.hometown + " Favorite Ice Cream: "
              + self.favoriteIceCream)
    def get_giraffe_gap(self):
        return (500 - int(self.height))
        
