class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class MIDEA_AC(AC):
    def cool_wind(self):
        print("美的空调核心制冷科技")

    def hot_wind(self):
        print("美的空调电热丝加热")

    def swing_l_r(self):
        print("美的空调无风感左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调变频制冷")

    def hot_wind(self):
        print("格力空调电热丝加热")

    def swing_l_r(self):
        print("格力空调静音左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = MIDEA_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)
