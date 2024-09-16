# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы ##(`make_sound()`, `eat()`) для всех животных.

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, wing_size):
        super().__init__(name, age)
        self.wing_size = wing_size

    def make_sound(self):
        print('Животное говорит "чик-чирик"')

    def eat(self):
        print('Животное ест пшеницу')


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print('Животное говорит "муууууууу"')

    def eat(self):
        print('Животное ест траву')


class Reptile(Animal):
    def __init__(self, name, age, scale_color):
        super().__init__(name, age)
        self.scale_color = scale_color

    def make_sound(self):
        print('Животное не говорит')

    def eat(self):
        print('Животное ест насекомых')

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

animal1 = Bird('Попугай', 2, 'большой')
animal2 = Mammal('Корова', 4, 'красная')
animal3 = Reptile('Змея', 1, 'серая')

list_animals = [animal1, animal2, animal3]


def animal_sound(list_animals):
    for animal in list_animals:
        print(f"{animal.name}")
        animal.make_sound()
        print("---------")


animal_sound(list_animals)


# 4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)


zoo1 = Zoo('Зоопарк "Мир"')

zoo1.add_animal('Кролик')
zoo1.add_animal('Кошка')
zoo1.add_animal('Собака')

print(f'Наш зоопарк называется - "{zoo1.name}".\nВ нем живут  животные: {zoo1.animals}.\n')


# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()`
# для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

# Базовый класс Staff
class Staff:
    def __init__(self, name_staff):
        self.name_staff = name_staff


# Класс ZooKeeper, наследующий от Staff
class ZooKeeper(Staff):
    zoo_keepers = []

    def __init__(self, name_staff):
        super().__init__(name_staff)
        ZooKeeper.zoo_keepers.append(self)


# Класс Veterinarian, наследующий от Staff
class Veterinarian(Staff):
    veterinarians = []

    def __init__(self, name_staff):
        super().__init__(name_staff)
        Veterinarian.veterinarians.append(self)


# Создаем сотрудников
staff1 = Staff("Вася")

# Создаем зоотехников
zoo_keeper1 = ZooKeeper('Александр')
zoo_keeper2 = ZooKeeper('Саша')

# Создаем ветеринаров
veterinarian1 = Veterinarian('Ирина')
veterinarian2 = Veterinarian('Александр')

# Проверяем список зоотехников и ветеринаров
print(f'Зоотехники: {[zk.name_staff for zk in ZooKeeper.zoo_keepers]}')
print(f'Ветеринары: {[v.name_staff for v in Veterinarian.veterinarians]}')
