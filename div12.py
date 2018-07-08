"""
The Diversant game, ver. 1.2.0
"""
import random
import time

# Задаем возможные повреждения, которые в случайном порядке будут наноситься персонажу
# Как мы видим, 37,5% вероятности, что будет промах
dam = (0, 0, 0, 5, 10, 15, 20, 30)

# Создаем класс персонажа и его характеристики: позиция, здоровье, цвет
class hero():
    def __init__(self, location, health, colour):
        self.location = location
        self.health = health
        self.colour = colour

# Задаем метод движения (персонаж делает шаг и позиция увеличивается на 1)
    def move_hero(self):
        self.location += 1

# Задаем метод повреждения персонажа (уменьшается здоровье)
    def damage_hero(self):
        damage = random.choice(dam)
        self.health -= damage
        # Пишем какое повреждение получили
        print ("Demage is: ", damage)

# Изменяем цвет персонажа, в зависимости от его здоровья
    def change_color_hero(self):
        if self.health < 70 and self.health > 30:
            self.colour = 'yellow'
        elif self.health < 30:
            self.colour = 'red'

# Персонаж использует аптечку (восстанавливается здоровье до 100)
    def use_med_kit_hero(self):
        if self.location == 10:
            self.health = 100
            print("Using medicine kit!")

# Сообщение состояния персонажа (его позиция, текущее здоровье и цвет):
    def show_hero(self):
        print ("Location:", self.location, " Health:", self.health, " Colour:", self.colour)

# Создаем объект - нашего персонажа
hero1 = hero(0, 100, "green")

# Показываем его начальное состояние
hero1.show_hero()
input("press Enter to start")

print ("Go!")

# Запускаем персонажа
# Каждый ход он совершает передвижение на 1 позицию
# На каждой позиции его атакуют и он получает повреждение
# На 10 позиции его ждет аптечка

while hero1.health > 0 and hero1.location < 20:
    hero1.move_hero()
    time.sleep(1)
    hero1.damage_hero()
    hero1.use_med_kit_hero()
    hero1.change_color_hero()
    hero1.show_hero()

# Если персонаж достиг позиции №20 - победа!
if hero1.location < 20:
    print("Mission failed!")
else:
    print("Mission complete!")
