class Flower:
    def __init__(self, breed, color, season):
        self.breed = breed
        self.color = color
        self.season = season

    def set_breed(self, breed):
        self.breed = breed

    def set_color(self, color):
        self.color = color

    def set_season(self, season):
        self.season = season

while True:
    info = input("Enter information: ")
    if info == '0':
        print("Program finished.")
        break

    info_list = info.split()
    flower = Flower(info_list[0], info_list[1], info_list[2])
    print(f"New object is: name: {flower.breed} - color: {flower.color} - season: {flower.season}")
